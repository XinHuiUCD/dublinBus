<template>
    <ContentBase>
        <div class="top">
                <JourneyPlan />
            <div class="button">
                <MapDisplay />
            </div>
        </div>
    </ContentBase>
</template>

<script lang="ts">
import ContentBase from '../components/ContentBase.vue'
import MapDisplay from '../components/MapDisplay.vue'
import JourneyPlan from '../components/JourneyPlan.vue'

export default {
    name: "HomeView",
    components: {
        ContentBase,
        MapDisplay,
        JourneyPlan,
    }
}
</script>

<style scoped>
</style>