<template>
       <ContentBase>
            <WeatherDisplay />
    </ContentBase>
</template>

<script lang="ts">
import ContentBase from '../components/ContentBase.vue'
import WeatherDisplay from '../components/WeatherDisplay.vue'

export default {
    name: "WeatherView",
    components: {
        ContentBase,
        WeatherDisplay,
    }
}
</script>

<style scoped>
</style>