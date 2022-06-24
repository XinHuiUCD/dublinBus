<template>
    <GoogleMap api-key="AIzaSyCrhyaaRpjY62Rs5XiT91Vfwv50ySu-FNo" style="height: 700px;" :center="center" :zoom="15">
        <Marker :options="{ position: center }">
            <InfoWindow>
                <div id="contet">
                    <div id="siteNotice"></div>
                    <h1 id="firstHeading" class="firstHeading">Dublin Bus</h1>
                    <div id="bodyContent">
                        <p><b>Bus Stop Info: </b>123</p>
                    </div>
                </div>
            </InfoWindow>
        </Marker>
    </GoogleMap>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import {
    GoogleMap,
    Marker,
    InfoWindow
} from 'vue3-google-map'

export default defineComponent({
    components: {
        GoogleMap,
        Marker,
        InfoWindow
    },
    setup() {
        const center = {
            lat: 53.349723,
            lng: -6.260278
        }

        return {
            center
        }
    },
})
</script>

<style scoped>
</style>
