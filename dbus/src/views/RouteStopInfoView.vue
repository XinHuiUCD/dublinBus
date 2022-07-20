<template>
    <ContentBase>
        <div id="Menu">
            <div id="title">
                <div id="function">
                    <!-- Your Position -->
                    <div class="input-group mb-3">
                        <button class="btn btn-outline-secondary" type="button" id="button-addon1">🔍</button>
                        <input type="text" class="form-control" placeholder="RouteID" v-model="routeId" show-clear>
                    </div>



                    <!-- submit -->
                    <button class="btn btn-outline-secondary" type="submit" @click="submit"
                        style="margin-top: 10px;margin-left: 20px;width: 70px;height: 60px;background-color: chartreuse;">Submit</button>
                </div>
            </div>
                <div class="button" id="map" style="align-items: center; margin-top: 1%">
      <GMapMap
        :center="center"
        :zoom="15"
        map-type-id="terrain"
        style="width: 100%; height: 700px"
        ref="mapTheme"
      >
        <GMapMarker
          v-for="(marker, index) in stops.stops" :key="marker"
          :position="{ lat: stops.stops[index].latitude, lng: stops.stops[index].longitude }"
          :visible="marker.visibility"
          :clickable="true"
        >
        </GMapMarker>
      </GMapMap>
    </div>
            <!-- <div v-for="marker in stops.stops" :key="marker.stop_id">
                {{ stops.stops[marker].latitude }}
            </div> -->
            <!-- <div v-if="stops.stops">
                <div v-for="(marker, index) in stops.stops" :key="marker">
                {{stops.stops[index].latitude}}
                </div>
            </div> -->
        </div>
    </ContentBase>
</template>

<script lang="ts">
import ContentBase from '../components/ContentBase.vue'
// import VueGoogleAutocomplete from "vue-google-autocomplete"
import { ref } from 'vue';
import $ from 'jquery';

export default {
    name: "RouteStopInfoView",
    components: {
        ContentBase,
    },
    setup() {
        let stops = ref([]);
        let routeId = ref('');
        const submit = () => {
            $.ajax({
                url: "http://127.0.0.1:9000/getinfo",
                type: "GET",
                data: {
                    routeId: routeId.value,
                },
                success(resp) {
                    stops.value = resp;
                    console.log(stops.value)
                }
            });
        };

        return {
            stops,
            routeId,
            submit,
            center: {
                lat: 53.349722,
                lng: -6.260278,
            },
        }
    }
}
</script>

<style scoped>
</style>