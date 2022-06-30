<template>
  <div class="open-weather-widget" :view="state.settings.view">
    <!-- loading screen -->
    <div id="open-weather-widget__loading-screen"></div>
    <!-- views -->
    <transition name="fade-200ms" mode="out-in">
      <template v-if="state.settings.view === 'main'">
        <main-view 
          :formattedWeatherData="formattedWeatherData" 
          :state="state" 
          :loadPreviousLocation="loadPreviousLocation"
          :loadNextLocation="loadNextLocation"
        />
      </template>
      <template v-else>
        <settings-view 
          v-if="state.settings.view === 'settings'" 
          :state="state"
          :removeLocation="removeLocation"
          :addLocation="addLocation"
          :loadLocationById="loadLocationById"
        />
      </template>
    </transition>
  </div>
</template>

<script>
import SettingsView from './SettingsView.vue'
import MainView from './MainView.vue'
import utils from '../utils/utils.js'
import '@mdi/font/css/materialdesignicons.css'
import '../icons/weather-icons-master/css/weather-icons.css'
import '../icons/weather-icons-master/css/weather-icons-wind.css'

export default {
  name: 'OpenWeatherWidget',
  props: {
    apiKey: {
      type: String,
      default: process.env.NODE_ENV === 'development' 
        ? process.env.VUE_APP_WEATHER_API_KEY 
        : ''
    }
  },
  components: {
    SettingsView,
    MainView
  },
  data () {
    return {
      state: {
        apiUrl: '',
        apiUrlBase: 'https://api.openweathermap.org/data/2.5/weather',
        userData: {
          geoLocation: {
            latitude: null,
            longitude: null,
            accuracy: null
          }
        },
        weatherData: {},
        defaultNoDataValue: 'no data',
        weatherAutoUpdateInterval: null,
        userLocationPermission: null,
        settings: {
          view: 'main',
          tempUnit: 'celsius',
          tempUnitList: ['celsius', 'fahrenheit'],
          autoUpdatePeriod: {
            value: true,
            selected: {
              text: 'Every 1 minute',
              value: 60000
            },
            items: [
              {
                text: 'Every 1 minute',
                value: 60000
              },
              {
                text: 'Every 5 minutes',
                value: 300000
              },
              {
                text: 'Every 15 minutes',
                value: 900000
              }
            ]
          },
          selectedLocation: {
            id: 1,
            isDefault: false,
            city: 'London',
            countryCode: 'UK'
          },
          savedLocations: [
            {
              id: 0,
              isDefault: true,
              city: '',
              countryCode: ''
            },
            {
              id: 1,
              isDefault: false,
              city: 'London',
              countryCode: 'UK'
            },
            {
              id: 2,
              isDefault: false,
              city: 'New York',
              countryCode: 'US'
            }
          ]
        }
      }
    }
  },
  created () {
    this.fetchLocalStorageData()
    this.updateWeather()
      .then(() => {
        this.initCurrentLocation()
      })
  },
  mounted () {
    this.removeLoadingScreen()
  },
  watch: {
    'state.settings.selectedLocation': {
      handler (newValue, oldValue) {
        this.updateWeather()
        this.updateLocalStorage()
      },
      deep: true
    },
    'state.settings.view': {
      handler (newValue, oldValue) {
        this.updateLocalStorage()
      },
      deep: true
    },
    'state.settings': {
      handler (newValue, oldValue) {
        this.updateLocalStorage()
      },
      deep: true
    }
  },
  computed: {
    previousSavedLocation () {
      const selectedLocation = this.state.settings.selectedLocation
      const savedLocations = this.state.settings.savedLocations
      const previousLocationIdClamped = Math.max(selectedLocation.id - 1, 0)
      return savedLocations.find(location => location.id === previousLocationIdClamped)
    },
    nextSavedLocation () {
      const selectedLocation = this.state.settings.selectedLocation
      const savedLocations = this.state.settings.savedLocations
      const nextLocationIdClamped = Math.min(selectedLocation.id + 1, savedLocations.length - 1)
      return savedLocations.find(location => location.id === nextLocationIdClamped)
    },
    formattedWeatherTempUnit () {
      if (this.state.settings.tempUnit === 'fahrenheit') {
        return '°F'
      }
      else {
        return '°C'
      }
    },
    formattedWeatherInfoTemp () {
      try {
        const temp = this.formattedWeatherInfoTempValue
        const tempUnit = this.formattedWeatherTempUnit
        return `${temp}${tempUnit}`
      }
      catch (error) {
        return this.state.defaultNoDataValue
      }
    },
    formattedWeatherInfoTempValue () {
      try {
        const tempKelvin = this.state.weatherData.main.temp
        const tempUnit = this.state.settings.tempUnit
        return utils.convertDegrees('kelvin', tempUnit, tempKelvin).toFixed(0)
      }
      catch (error) {
        return ''
      }
    },
    formattedWeatherInfoTempFeelsLikeValue () {
      try {
        const tempKelvin = this.state.weatherData.main.feels_like
        const tempUnit = this.state.settings.tempUnit
        return utils.convertDegrees('kelvin', tempUnit, tempKelvin).toFixed(0)
      }
      catch (error) {
        return ''
      }
    },
    formattedWeatherInfoTempFeelsLike () {
      try {
        const temp = this.formattedWeatherInfoTempFeelsLikeValue
        const tempUnit = this.formattedWeatherTempUnit
        return `Feels like ${temp}${tempUnit}`
      }
      catch (error) {
        return this.state.defaultNoDataValue
      }
    },
    formattedWeatherInfoWindSpeed () {
      try { return `${this.state.weatherData.wind.speed} m/s` }
      catch (error) {
        return this.state.defaultNoDataValue
      }
    },
    formattedWeatherInfoWindDeg () {
      try { return `${this.state.weatherData.wind.deg} deg` }
      catch (error) {
        return this.state.defaultNoDataValue
      }
    },
    formattedWeatherInfoWindDirection () {
      try {
        const deg = this.state.weatherData.wind.deg
        if (deg === 0) { return 'E' }
        else if (deg === 90) { return 'N' }
        else if (deg === 180) { return 'W' }
        else if (deg === 270) { return 'S' }
        else if (deg > 0 && deg < 90) { return 'NE' }
        else if (deg > 90 && deg < 180) { return 'NW' }
        else if (deg > 180 && deg < 270) { return 'SW' }
        else if (deg > 270 && deg < 360) { return 'SE' }
        return ''
      }
      catch (error) {
        return this.state.defaultNoDataValue
      }
    },
    formattedWeatherInfoWeatherDescription () {
      try {
        const desc = this.state.weatherData.weather[0].description
        return desc.replace(/^\p{CWU}/u, char => char.toLocaleUpperCase('en'))
      }
      catch (error) {
        return this.state.defaultNoDataValue
      }
    },
    formattedWeatherInfoWeatherIcon () {
      try {
        return this.state.weatherData.weather[0].icon
      }
      catch (error) {
        return this.state.defaultNoDataValue
      }
    },
    formattedWeatherInfoPressure () {
      try {
        return `${this.state.weatherData.main.pressure} hPa`
      }
      catch (error) {
        return this.state.defaultNoDataValue
      }
    },
    formattedWeatherInfoHumidity () {
      try {
        return `${this.state.weatherData.main.humidity} %`
      }
      catch (error) {
        return this.state.defaultNoDataValue
      }
    },
    formattedWeatherInfoVisibility () {
      try {
        const value = (this.state.weatherData.visibility / 1000).toFixed(1)
        if (isNaN(value)) {
          throw Error()
        }
        return `${value} km`
      }
      catch (error) {
        return this.state.defaultNoDataValue
      }
    },
    formattedWeatherInfoCity () {
      try {
        return this.state.weatherData.name
      }
      catch (error) {
        return this.state.defaultNoDataValue
      }
    },
    formattedWeatherInfoCountry () {
      try {
        return this.state.weatherData.sys.country
      }
      catch (error) {
        return this.state.defaultNoDataValue
      }
    },
    formattedWeatherData () {
      return {
        temp: this.formattedWeatherInfoTemp,
        tempValue: this.formattedWeatherInfoTempValue,
        tempUnit: this.formattedWeatherTempUnit,
        tempFeelsLike: this.formattedWeatherInfoTempFeelsLike,
        windSpeed: this.formattedWeatherInfoWindSpeed,
        windDeg: this.formattedWeatherInfoWindDeg,
        windDirection: this.formattedWeatherInfoWindDirection,
        weatherDescription: this.formattedWeatherInfoWeatherDescription,
        weatherIcon: this.formattedWeatherInfoWeatherIcon,
        pressure: this.formattedWeatherInfoPressure,
        humidity: this.formattedWeatherInfoHumidity,
        visibility: this.formattedWeatherInfoVisibility,
        city: this.formattedWeatherInfoCity,
        country: this.formattedWeatherInfoCountry
      }
    }
  },
  methods: {
    removeLoadingScreen () {
      const loadingScreenNode = document.querySelector('#open-weather-widget__loading-screen')
      loadingScreenNode.animate(
        [
          { opacity: 1 },
          { opacity: 0 }
        ],
        {
          easing: 'ease',
          duration: 2000,
          fill: 'forwards'
        }
      )
    },
    fetchLocalStorageData () {
      const stateData = localStorage.getItem('state')
      if (stateData) {
        this.state.settings = JSON.parse(stateData)
      }
    },
    updateLocalStorage () {
      localStorage.setItem('state', JSON.stringify(this.state.settings))
    },
    initCurrentLocation () {
      this.loadLocationById(0)
      this.updateWeather()
    },
    updateWeather () {
      return new Promise((resolve, reject) => {
        this.fetchDataForWeatherUpdate()
          .then(() => {
            this.fetchWeather()
              .then((data) => {
                this.state.weatherData = data
                this.updateDefaultLocationData(data)
                resolve()
                this.initWeatherAutoUpdateInterval()
              })
          })
          .catch((error) => {
            console.log(error)
            reject(error)
          })
      })
    },
    updateDefaultLocationData (data) {
      if (data === 'placeholder') {
        this.state.settings.selectedLocation.city = 'Current location'
        this.state.settings.selectedLocation.countryCode = ''
      }
      else if (data !== 'placeholder' && this.state.settings.selectedLocation.isDefault) {
        const defaultLocation = this.state.settings.savedLocations
          .find(location => location.isDefault)
        // Update default location on the savedLocations list
        defaultLocation.city = data.name
        defaultLocation.countryCode = data.sys.country
        // Update selected location data
        this.state.settings.selectedLocation.city = data.name
        this.state.settings.selectedLocation.countryCode = data.sys.country
      }
    },
    fetchDataForWeatherUpdate () {
      return new Promise((resolve, reject) => {
        if (this.state.settings.selectedLocation.isDefault) {
          this.fetchUserLocation()
            .then((event) => {
              this.state.userLocationPermission = true
              this.setUserLocation({
                latitude: event.coords.latitude, 
                longitude: event.coords.longitude,
                accuracy: event.coords.accuracy
              })
              this.fetchApiUrl({locationType: 'geo-coord'})
              resolve()
            })
            .catch((error) => {
              // User denied location permission
              if (error.code === 1) {
                this.state.userLocationPermission = false
                this.updateDefaultLocationData('placeholder')
              }
            })
        }
        else {
          this.fetchApiUrl({locationType: 'selected-location'})
          resolve()
        }
      })
    },
    fetchApiUrl (payload) {
      this.state.apiUrl = this.getWeatherApiUrl(payload)
    },
    fetchWeather () {
      return new Promise((resolve, reject) => {
        fetch(this.state.apiUrl)
          .then(response => response.json())
          .then(data => {
            resolve(data)
          })
          .catch(error => console.error(error))
      })
    },
    initWeatherAutoUpdateInterval () {
      clearInterval(this.state.weatherAutoUpdateInterval)
      this.state.weatherAutoUpdateInterval = setInterval(() => {
        this.updateWeather()
      }, this.state.settings.autoUpdatePeriod.selected.value)
    },
    fetchUserLocation () {
      return new Promise((resolve, reject) => {
        if (window.navigator.geolocation) {
          const options = {
            enableHighAccuracy: true,
            timeout: 5000,
            maximumAge: 0
          }
          window.navigator.geolocation.getCurrentPosition(
            resolve,
            reject,
            options
          )
        }
        else {
          reject(new Error('cannot-get-user-location'))
        }
      })
    },
    setUserLocation (payload) {
      this.state.userData.geoLocation.latitude = payload.latitude
      this.state.userData.geoLocation.longitude = payload.longitude
      this.state.userData.geoLocation.accuracy = payload.accuracy
    },
    getWeatherApiUrl (payload) {
      let query = ''
      if (payload.locationType === 'geo-coord') {
        const latitude = this.state.userData.geoLocation.latitude
        const longitude = this.state.userData.geoLocation.longitude
        query = `lat=${latitude}&lon=${longitude}&appid=${this.apiKey}`
      }
      else if (payload.locationType === 'selected-location') {
        const city = this.state.settings.selectedLocation.city
        const countryCode = this.state.settings.selectedLocation.countryCode
        query = `q=${city},${countryCode}&appid=${this.apiKey}`
      }
      return `${this.state.apiUrlBase}?${query}`
    },
    loadPreviousLocation () {
      this.state.settings.selectedLocation = this.previousSavedLocation
    },
    loadNextLocation () {
      this.state.settings.selectedLocation = this.nextSavedLocation
    },
    loadLocationById (id) {
      this.state.settings.selectedLocation = this.state.settings.savedLocations
        .find(location => location.id === id)
    },
    removeLocation (locationItem) {
      if (!locationItem.isDefault) {
        const itemIndex = this.state.settings.savedLocations.findIndex(item => item.id === locationItem.id)
        if (itemIndex !== -1) {
          this.state.settings.savedLocations.splice(itemIndex, 1)
        }
        // Get weather for the default location on the list
        this.loadLocationById(0)
        this.updateWeather()
      }
    },
    addLocation (item) {
      const id = this.state.settings.savedLocations.length
      this.state.settings.savedLocations.push({
        id,
        isDefault: false,
        city: item.city,
        countryCode: item.code
      })
      // Get weather for the added location
      this.loadLocationById(id)
      this.updateWeather()
    }
  }
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400&display=swap');

:root {
  --voww-bg-color-1: #fff;
  --voww-accent-color-value: 112, 130, 245;
  --voww-divider-color-1: rgba(0, 0, 0, 0.1);
  --voww-disabled-color-1: rgba(0, 0, 0, 0.3);
}

hr {
  border-top-color: var(--voww-divider-color-1);
  max-width: 200px;
  margin: 16px auto;
}

#open-weather-widget {
  &__main-view, &__settings-view {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
  }
}

.open-weather-widget {
  font-family: 'Open Sans', sans-serif;
  font-weight: 400;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
  text-align: center;
  color: #3e464e;
  transition: all 0.2s;
  &__title {
    font-size: 14px;
    text-transform: uppercase;
    padding-bottom: 12px;
    color: rgb(172, 172, 172)
  }
  &__main-toolbar {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    padding: 12px 20px;
    &__title {
      font-size: 18px;
    }
    &__action-buttons {
      display: flex;
      gap: 16px;
      i {
        cursor: pointer;
      }
    }
  }
  &__content-area {
    padding: 24px;
    padding-top: 8px;
    width: 100%;
    height: 100%;
    box-sizing: border-box;
  }
  &__saved-location-item {
    display: grid;
    grid-template-columns: 32px 1fr 32px;
    gap: 4px;
    align-items: center;
    &__action-buttons {
      display: flex;
      justify-self: end;
      gap: 16px;
      i {
        cursor: pointer;
      }
      i[is-disabled] {
        cursor: default;
        color: var(--voww-disabled-color-1)
      }
    }
    &__title {
      text-align: left;
    }
  }
  &__sortable-list {
    &__item {
      position: relative;
      display: flex;
      align-content: center;
      width: 100%;
      cursor: pointer;
      user-select: none;
      border-bottom: 1px solid var(--voww-divider-color-1);
      padding: 8px;
      background-color: var(--voww-bg-color-1);
      &:hover {
        background-color: rgba(0, 0, 0, 0.02);
      }
      & [is-active] {
        color: rgba(var(--voww-accent-color-value), 1);
      }
    }
  }
}

#open-weather-widget__loading-screen {
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  z-index: 10;
  user-select: none;
  pointer-events: none;
  background-color: var(--voww-bg-color-1);
  opacity: 1;
}

.fade-200ms-enter-active, 
.fade-200ms-leave-active {
  transition: all 0.2s;
}

.fade-200ms-enter, 
.fade-200ms-leave-to {
  opacity: 0;
}
</style>
