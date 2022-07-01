<template>
    <GoogleMap api-key="AIzaSyCrhyaaRpjY62Rs5XiT91Vfwv50ySu-FNo" style="height: 700px;" :center="center" :zoom="15">
        <Marker :options="{ position: center }">
            <InfoWindow>
                <div id="content">
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

import BusStopLongLat from './json/BusStopsLongLatCSV.json'

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
    data(){
        return{
			
			}
        }
        
    
})
</script>

<style scoped>
</style>

<!-- <template>
	<GoogleMap api-key="AIzaSyCrhyaaRpjY62Rs5XiT91Vfwv50ySu-FNo" :center="center" :zoom="15" :styles="theme" style="height: 700px;" />
	<label for="theme">Theme</label>
	<select v-model="theme" id="theme">
		<option value="">-- None --</option>
		<option v-for="theme in themes" :value="theme" :key="theme">{{ theme }}</option>
	</select>
</template>

<script>
	import {
		defineComponent,
		ref
	} from 'vue'
	import {
		GoogleMap
	} from 'vue3-google-map'
	import * as themes from './Theme/index.ts'

	export default defineComponent({
		components: {
			GoogleMap
		},
		setup() {
			const center = {
				lat: 53.349722,
				lng: -6.260278
			}
			const themes = ['dark']
			const theme = ref('')

			return {
				center,
				themes,
				theme
			}
		},
	})
</script>

<style scoped>
	select {
		width: 200px;
		margin-top: 20px;
		margin-left: 10px;
	}
</style>
 -->