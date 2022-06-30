<template>
  <div id="open-weather-widget__settings-view">
    <!-- main toolbar -->
    <div class="open-weather-widget__main-toolbar">
      <!-- main toolbar::title -->
      <div class="open-weather-widget__main-toolbar__title">
        Settings
      </div>
      <!-- main toolbar::action buttons -->
      <div class="open-weather-widget__main-toolbar__action-buttons">
        <i 
          @click="state.settings.view = 'main'"
          class="mdi mdi-close" 
          style="font-size: 20px"
        ></i>
      </div>
    </div>
    <!-- content area -->
    <div class="open-weather-widget__content-area">
      <!-- content area::section-->
      <div class="open-weather-widget__content-area__section">
        <div class="open-weather-widget__title">
          Saved locations
        </div>
        <Container
          v-if="state.settings.savedLocations.length > 0"
          @drop="handleEventSortableOnDrop"
          class="open-weather-widget__sortable-list"
          drag-class="open-weather-widget__sortable-list__item--drag-active" 
          :animation-duration="250"
          :get-ghost-parent="getGhostParent" 
          drag-handle-selector=".column-drag-handle" 
          lock-axis="y" 
        >            
          <Draggable 
            v-for="(item, index) in state.settings.savedLocations" 
            :key="'item-' + index" 
            class="open-weather-widget__sortable-list__item"
            border
          >
            <div 
              @click="loadLocationById(item.id)"  
              :is-active="isActiveItem(item)" 
              class="open-weather-widget__saved-location-item" 
            >
              <i 
                :class="{
                  'mdi mdi-crosshairs-gps': item.isDefault,
                  'mdi mdi-drag-horizontal column-drag-handle': !item.isDefault
                }" 
                style="font-size: 20px"
                drag
              ></i>
              <div>
                {{getLocationTitle(item)}}
              </div>
              <div class="open-weather-widget__saved-location-item__action-buttons">
                <i 
                  v-if="!item.isDefault"
                  @click.stop="removeLocation(item)"
                  class="mdi mdi-trash-can-outline" 
                  style="font-size: 20px"
                ></i>
              </div>
            </div>
          </Draggable>
        </Container>
      </div>
      <!-- content area::section-->
      <div class="open-weather-widget__content-area__section">
        <div class="open-weather-widget__title">
          Add location
        </div>
        <div class="open-weather-widget__input-element">
          <label>Enter city name</label>
          <input 
            @input="handleInputEventLocation($event)"
            @keydown="handleInputKeydownLocation($event)"
            @keydown.enter="addEnteredLocation()"
            class="open-weather-widget__input"
            placeholder="City name" 
            type="text" 
          >
        </div>
        <!-- suggestion hint text -->
        <div 
          v-if="showLocationSuggestionList"
          class="open-weather-widget__input-hint"
        >Select location from the list [ArrowUp, ArrowDown] and press [Enter]
        </div>
        <!-- suggestion list container -->
        <div 
          v-if="showLocationSuggestionList"
          class="open-weather-widget__location-suggestions-list" 
          :has-items="showLocationSuggestionList"
        >
          <div 
            v-for="(item, index) in matchingLocations" 
            @click="addLocation(item)"
            :key="index"
            class="open-weather-widget__location-suggestions-list__item"
            :is-selected="locationIsSelected(item)"
          >
            {{ item.city }}, {{ item.code }}
            <i 
              v-if="locationIsSelected(item)"
              @click="addEnteredLocation()"
              class="mdi mdi-subdirectory-arrow-left" 
              style="font-size: 16px; margin-left: 8px"
            ></i>
          </div>
        </div>
      </div>
      <!-- content area::section-->
      <div class="open-weather-widget__content-area__section">
        <!-- options -->
        <div class="open-weather-widget__title">
          Options
        </div>
        <!-- option::auto update -->
        <div class="open-weather-widget__option-item">
          <toggle 
            v-model="state.settings.autoUpdatePeriod.value"
            :checked="state.settings.autoUpdatePeriod.value"
            label="Auto update weather"
            style="margin-bottom: 16px"
          />
          <div 
            v-if="state.settings.autoUpdatePeriod.value"
            class="open-weather-widget__input-element"
          >
            <label>Update interval</label>
            <select 
              class="open-weather-widget__input-select"
              name="autoUpdatePeriodSelect"
              @change="handleChangeEvenrAutoUpdatePeriod"
            >
              <option 
                v-for="(option, index) in state.settings.autoUpdatePeriod.items"
                :key="index"
              >
                {{option.text}}
              </option>
            </select>
          </div>
        </div>
        <!-- option::temp unit -->
        <div class="open-weather-widget__option-item open-weather-widget__input-element">
          <label>Temperature units</label>
          <select 
            class="open-weather-widget__input-select"
            name="autoUpdatePeriodSelect"
            v-model="state.settings.tempUnit"
          >
            <option 
              v-for="(option, index) in state.settings.tempUnitList"
              :key="index"
            >
              {{option}}
            </option>
          </select>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { countries } from 'countries-list'
import { Container, Draggable } from 'vue-smooth-dnd'
import Toggle from './Toggle.vue'
import utils from '../utils/utils.js'

export default {
  name: 'SettingsView',
  components: {
    Container, 
    Draggable,
    Toggle
  },
  props: {
    state: Object,
    removeLocation: Function,
    addLocation: Function,
    loadLocationById: Function
  },
  data () {
    return {
      countriesData: [],
      matchingLocations: [],
      selectedSuggestionIndex: 0,
      selectedSuggestion: {},
      locationInputValue: ''
    }
  },
  mounted () {
    this.getCountriesData()
  },
  computed: {
    enteredLocationValidation () {
      const someLocationSelected = this.selectedSuggestion?.city
      if (!someLocationSelected) {
        return {
          isValid: false,
          error: 'Select a location from the list'
        }
      }
      else {
        return {
          isValid: true
        }
      }
    },
    showLocationSuggestionList () {
      return this.matchingLocations.length > 0 &&
        this.locationInputValue.length > 0
    }
  },
  methods: {
    getLocationTitle (item) {
      return utils.locationTitle(item)
    },
    locationIsSelected (item) {
      return item.city === this.selectedSuggestion.city &&
        item.code === this.selectedSuggestion.code
    },
    handleChangeEvenrAutoUpdatePeriod (event) {
      const selectedIndex = event.target.options.selectedIndex
      this.state.settings.autoUpdatePeriod.selected = this.state.settings.autoUpdatePeriod.items[selectedIndex]
    },
    handleInputKeydownLocation (event) {
      if (event.code === 'ArrowUp') {
        this.selectPreviousSuggestion()
      }
      else if (event.code === 'ArrowDown') {
        this.selectNextSuggestion()
      }
    },
    handleInputEventLocation (event) {
      this.locationInputValue = event.target.value
      this.matchingLocations = []
      this.countriesData.forEach((dataObject) => {
        const someCityMatches = dataObject.cities.find(city => {
          return city.toLowerCase().includes(this.locationInputValue.toLowerCase())
        })
        if (someCityMatches) {    
          for (const [countryCode, countryData] of Object.entries(countries)) {
            if (countryData.name.toLowerCase() === dataObject.country.toLowerCase()) {
              this.matchingLocations.push({country: dataObject.country, city: someCityMatches, code: countryCode})
              this.selectFirstSuggestion()
            }
          }
        }
      })
    },
    async getCountriesData () {
      const urlBase = 'https://countriesnow.space/api/v0.1/countries'
      const response = await fetch(`${urlBase}`).then(response => response.json())
      const { data } = response
      this.countriesData = data
    },
    isActiveItem (item) {
      return this.state?.settings?.selectedLocation?.id === item?.id
    },
    getGhostParent () {
      return document.querySelector('#open-weather-widget__settings-view')
    },
    handleEventSortableOnDrop (dropResult) {
      // Move item to new index within array
      const { removedIndex, addedIndex } = dropResult
      if (removedIndex && addedIndex) { 
        const list = [...this.state.settings.savedLocations]
        const itemToAdd = list.splice(removedIndex, 1)[0]
        list.splice(addedIndex, 0, itemToAdd)
        this.state.settings.savedLocations = list
        this.updateSavedLocationsIds()
      }
    },
    addEnteredLocation () {
      if (this.enteredLocationValidation.isValid) {
        this.addLocation(this.selectedSuggestion)
      }
      else {
        alert(this.enteredLocationValidation.error)
      }
    },
    selectFirstSuggestion () {
      this.selectedSuggestion = this.matchingLocations[0]
    },
    selectPreviousSuggestion () {
      const indexToSelect = Math.max(this.selectedSuggestionIndex - 1, 0)
      this.selectedSuggestion = this.matchingLocations[indexToSelect]
      this.selectedSuggestionIndex = indexToSelect
    },
    selectNextSuggestion () {
      const indexToSelect = Math.min(this.selectedSuggestionIndex + 1, this.matchingLocations.length - 1)
      this.selectedSuggestion = this.matchingLocations[indexToSelect]
      this.selectedSuggestionIndex = indexToSelect
    },
    updateSavedLocationsIds () {
      this.state.settings.savedLocations.forEach((location, index) => {
        location.id = index
      })
    }
  }
}
</script>

<style lang="scss">
#open-weather-widget {
  &__settings-view {
    text-align: left;
    .open-weather-widget {
      &__content-area {
        display: flex;
        flex-direction: column;
        gap: 16px;
        overflow-y: auto;
      }
    }
  }
}

.open-weather-widget {
  &__location-suggestions-list[has-items] {
    border: 1px solid var(--voww-divider-color-1);
    padding: 8px;
  }
  &__location-suggestions-list {
    max-height: 100px;
    overflow: auto;
    &__item {
      position: relative;
      display: flex;
      align-content: center;
      width: 100%;
      cursor: pointer;
      padding: 4px;
      overflow-x: hidden;
      &:hover {
        background-color: rgba(0, 0, 0, 0.02);
      }
    }
    &__item[is-selected] {
      background-color: rgba(var(--voww-accent-color-value), 0.7);
      color: #fff
    }
  }
  &__input-select, &__input:not([type="checkbox"]) {
    width: 100%;
    font-size: 16px;
    padding: 12px 10px 8px 10px;
    border-radius: 4px;
    border: 1px solid var(--voww-divider-color-1);
    background-color: transparent;
    color: rgba(0, 0, 0, 0.6);
    box-sizing: border-box;
    &:focus {
      border-bottom: 2px solid rgba(var(--voww-accent-color-value), 0.8);
      outline: none;
      color: rgba(var(--voww-accent-color-value), 0.8);
      &::placeholder {
        color: rgba(var(--voww-accent-color-value), 0.8);
      }
    }
    &::placeholder {
      color: rgba(0, 0, 0, 0.3);
    }
  }
  &__input-select {
    text-transform: capitalize;
  }
  &__input-hint {
    font-size: 13px;
    padding: 8px;
  }
  &__option-item {
    margin-bottom: 16px
  }
  &__input-element {
    position: relative;
    margin-top: 10px;
    & label {
      font-size: 13px;
      color: rgba(0, 0, 0, 0.5);
      padding: 0px 4px;
      background-color: #fff;
      position: absolute;
      top: -10px;
      left: 8px;
    }
  }
}
</style>
