<template>
    <div className="App">
      <Header />
      <div className='main-content'>
        <Menu />
		<Weather />
		<Map />
      </div>
    </div>
</template>

<script lang="ts">
import Header from './components/HeaderItem/HeaderItem.vue'
import Menu from './components/MenuItem/MenuItem.vue'
import Map from './components/MapItem/MapItem.vue'
import Weather from './components/WeatherItem/WeatherItem.vue'
/* eslint-disable */
export default {
  name: 'App',
  components: {
    Header,
	Menu,
	Map,
	Weather
  }
}
</script>

<style>
/* Screen size */
#app {
	width: 100%;
	height: 100%;
}
</style>

