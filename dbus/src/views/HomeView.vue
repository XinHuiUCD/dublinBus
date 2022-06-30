<template>
    <ContentBase>
        <div class="row">
            <div class="col-3">
                <JourneyPlan />
            </div>
            <div class="col-7">
                <MapDisplay />
            </div>
            <div class="col-2">
                <WeatherDisplay />
            </div>
        </div>
    </ContentBase>
</template>

<script lang="ts">
import ContentBase from '../components/ContentBase.vue'
import MapDisplay from '../components/MapDisplay.vue'
import JourneyPlan from '../components/JourneyPlan.vue'
import WeatherDisplay from '../components/WeatherDisplay.vue'

export default {
    name: "HomeView",
    components: {
        ContentBase,
        MapDisplay,
        JourneyPlan,
        WeatherDisplay,
    }
}
</script>

<style scoped>
</style>