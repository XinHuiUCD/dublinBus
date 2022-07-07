<template>
  <div id="open-weather-widget__main-view">
    <!-- main toolbar -->
    <div class="open-weather-widget__main-toolbar">
      <!-- main toolbar::title -->
      <div class="open-weather-widget__main-toolbar__title">
        {{mainToolbarTitle}}
      </div>
      <!-- main toolbar::action buttons -->
      <div class="open-weather-widget__main-toolbar__action-buttons">
        <template v-if="state.settings.savedLocations.length > 1">
          <i 
            @click="loadPreviousLocation()"
            class="mdi mdi-chevron-left" 
            style="font-size: 20px"
          ></i>
          <i 
            @click="loadNextLocation()"
            class="mdi mdi-chevron-right" 
            style="font-size: 20px"
          ></i>
        </template>
        <i 
          @click="state.settings.view = 'settings'"
          class="mdi mdi-cog-outline" 
          style="font-size: 20px"
        ></i>
      </div>
    </div>
    <!-- content area -->
    <div class="open-weather-widget__content-area">
      <!-- section::geo location denied placeholder -->
      <div
        v-if="showGeoLocationDeniedPlaceholder"
        class="open-weather-widget__content-area__geo-location-denied-placeholder"
      >
        <i 
          class="mdi mdi-map-marker" 
          style="font-size: 32px;"
        ></i>
        <div class="open-weather-widget__content-area__geo-location-denied-placeholder__title">
          No data
        </div>
        <div>
          Allow geo location persmission to show the weather for your location.
        </div>
      </div>
      <!-- section::content -->
      <div 
        v-else-if="!showGeoLocationDeniedPlaceholder"
        class="open-weather-widget__content-area__content"
      >
        <!-- info::temp -->
        <div 
          @click="switchTempUnit()"
          class="open-weather-widget__weather-info__temp"
        >
          {{formattedWeatherData.temp}}
        </div>
        <i 
          :class="getWeatherIcon()" 
          style="font-size: 32px;"
          class="open-weather-widget__weather-icon"
        ></i>
        <!-- info::weather description -->
        <div>
          <div class="open-weather-widget__weather-info__weather-description">
            {{formattedWeatherData.weatherDescription}}
          </div>
          <div class="open-weather-widget__weather-info__temp-feels-like">
            {{formattedWeatherData.tempFeelsLike}}
          </div>
          <hr>
        </div>
        <!-- info::weather properties -->
        <div class="open-weather-widget__weather-info__properties">
          <div 
            v-for="(item, index) in weatherInfoItems" 
            :key="index"
            :class="item.class"
          >
            <i 
              :class="item.icon" 
              style="font-size: 22px;"
            ></i>
            {{ item.text }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import utils from '../utils/utils.js'

export default {
  name: 'MainView',
  props: {
    formattedWeatherData: Object,
    state: Object,
    loadPreviousLocation: Function,
    loadNextLocation: Function
  },
  computed: {
    showGeoLocationDeniedPlaceholder () {
      return this.state.userLocationPermission === false && 
        this.state.settings.selectedLocation.isDefault
    },
    mainToolbarTitle () {
      const city = this.state.settings.selectedLocation.city
      const countryCode = this.state.settings.selectedLocation.countryCode
      return utils.locationTitle({
        city,
        countryCode
      })
    },
    weatherInfoItems () {
      return [
        {
          class: 'open-weather-widget__weather-info__pressure',
          icon: 'mdi mdi-gauge-full',
          text: this.formattedWeatherData.pressure
        },
        {
          class: 'open-weather-widget__weather-info__wind-speed',
          icon: 'mdi mdi-windsock',
          text: this.windSpeedDescription
        },
        {
          class: 'open-weather-widget__weather-info__visibility',
          icon: 'mdi mdi-eye-outline',
          text: this.formattedWeatherData.visibility
        },
        {
          class: 'open-weather-widget__weather-info__humidity',
          icon: 'mdi mdi-water-percent',
          text: this.formattedWeatherData.humidity
        }
      ]
    },
    weatherDescription () {
      const tempFeelsLike = this.formattedWeatherData.tempFeelsLike
      const weatherDescription = this.formattedWeatherData.weatherDescription
      const showValue = tempFeelsLike !== this.state.defaultNoDataValue && 
        weatherDescription !== this.state.defaultNoDataValue
      if (showValue) {
        return `${tempFeelsLike}. ${weatherDescription}`
      }
      else {
        return this.state.defaultNoDataValue
      }
    },
    windSpeedDescription () {
      const windSpeed = this.formattedWeatherData.windSpeed
      const windDirection = this.formattedWeatherData.windDirection
      const showValue = windSpeed !== this.state.defaultNoDataValue && 
        windDirection !== this.state.defaultNoDataValue
      if (showValue) {
        return `${windSpeed} ${windDirection}`
      }
      else {
        return this.state.defaultNoDataValue
      }
    }
  },
  methods: {
    getWeatherIcon () {
      const iconMap = {
        'wi wi-day-sunny': ['01d'],
        'wi wi-day-cloudy': ['02d', '03d', '04d'],
        'wi wi-day-rain': ['09d', '10d'],
        'wi wi-day-thunderstorm': ['11d'],
        'wi wi-day-snow-wind': ['13d'],
        'wi wi-day-fog': ['50d'],
        'wi wi-night-clear': ['01n'],
        'wi wi-night-cloudy': ['02n', '03n', '04n'],
        'wi wi-night-rain': ['09n', '10n'],
        'wi wi-night-thunderstorm': ['11n'],
        'wi wi-night-snow-wind': ['13n'],
        'wi wi-night-fog': ['50n']
      }
      let icon = 'wi wi-na'
      // Set matching icon 
      for (const [key, value] of Object.entries(iconMap)) {
        if (value.includes(this.formattedWeatherData.weatherIcon)) {
          icon = key
        }
      }
      return icon
    },
    switchTempUnit () {
      this.state.settings.tempUnit = this.state.settings.tempUnit === 'celsius'
        ? 'fahrenheit'
        : 'celsius'
    }
  }
}
</script>

<style scoped lang="scss">
.open-weather-widget {
  &__content-area { 
    &__geo-location-denied-placeholder {
      width: 100%;
      height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background-color: var(--voww-bg-color-1);
      &__title {
        font-size: 36px;
        margin-bottom: 8px;
      }
    }
  }
  &__weather-info__properties {
    display: flex; 
    flex-wrap: wrap;
    justify-content: center; 
    column-gap: 12px;
    row-gap: 4px;
    & > div {
      display: flex;  
      align-items: center;
      gap: 4px;
    }
  }
  &__weather-info__temp {
    font-size: 48px;
    font-weight: 300;
    user-select: none;
    cursor: pointer;
  }
  &__weather-icon {
    margin-top: 16px;
    margin-bottom: 16px;
  }
}
</style>
