<template>
    <ContentBase>
        <MapDisplay />
    </ContentBase>
</template>

<script lang="ts">
import ContentBase from '../components/ContentBase.vue'
import MapDisplay from '../components/MapDisplay.vue'

export default {
    name: "HomeView",
    components: {
        ContentBase,
        MapDisplay,
    }
}
</script>

<style scoped>
</style>