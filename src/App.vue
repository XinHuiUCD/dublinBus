<template>
  <NavBar />
  <router-view />
</template>


<script lang="ts">
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap'
import 'element-plus/dist/index.css'
import NavBar from './components/NavBar.vue'

export default {
  name: "App",
  components: {
    NavBar
  }
}
</script>

<style>
</style>
