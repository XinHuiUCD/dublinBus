# Vue 3 + OpenWeather

[![vue3](https://img.shields.io/badge/vuejs-3.x-brightgreen.svg)](https://vuejs.org/)
[![npm](https://img.shields.io/npm/v/vue-openweather)](http://npmjs.com/package/vue-openweather)
[![npm download per month](https://img.shields.io/npm/dm/vue-openweather)](http://npmjs.com/package/vue-openweather)

<img src="https://user-images.githubusercontent.com/58784686/162488946-1d0f1ffc-633f-45c4-8fdd-f64b6e46919d.png">

Inspired by [vue-weather-widget](https://github.com/dipu-bd/vue-weather-widget)

## Install

### NPM

```
npm i vue-openweather
```

## OpenWeatherAPI

Get an OpenWeatherAPI key by signing up an account at the OpenWeather website

## Usage
```html
<script setup lang="ts">
  import { ref } from 'vue'
  import { VueOpenWeather, convertTimeZone, utcToDate, utcToTime } from "vue-openweather";
  import "vue-openweather/style.css";

  const weatherData = ref<any>('')
  const updateWeatherData = (event: any) => weatherData.value = event[0]

  // convertTimeZone takes the dt value returned from the OpenWeather API, and the timezone offset
  // to convert the correct time based on the coordinates regardless of the computer's actual timezone
  const getAdjustedTime = () => {
    return convertTimeZone(weatherData.value.hourly[0].dt, weatherData.value.timezone_offset)
  }
</script>

<template>
  <VueOpenWeather 
    apiKey="your-open-weather-api-key"
    lat="your-latitude"
    long="your-longitude"
    hourly
    @weatherData="updateWeatherData"
  />
</template>


```

## Props

| Props       | Type               | Default Value                     | Description                                                  |
|-------------|--------------------|-----------------------------------|--------------------------------------------------------------|
| apiKey      | string (required)  | -                                 | Your API key                                                 |
| lat         | string (required)  | -                                 | Your latitude                                                |
| long        | string (required)  | -                                 | Your longitude                                               |
| hourly      | boolean            | false                             | Hourly data for 48 hours                                     |
| daily       | boolean            | false                              | Daily data for 3 days                                       |
| units       | string             | metric                            | Metric or Imperial units                                     |
| excludes    | Array<string>      | ['minutely', 'alerts', 'current'] | Customize data to be excluded from API call                  |

## Events
### @weatherData returns the JSON data from the API call

```html
<script setup lang="ts">
  import VueOpenWeather from "vue-openweather";
  import "vue-openweather/style.css";

  const logWeatherData = (event: any) => console.log(event)
</script>

<template>
  <VueOpenWeather 
    apiKey="your-open-weather-api-key"
    lat="your-latitude"
    long="your-longitude"
    hourly
    @weatherData="logWeatherData"
  />
</template>


```
