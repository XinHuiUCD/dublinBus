<template>
    <ContentBase>
        <div id="Menu">
            <div id="title">
                <div id="function">
                    <!-- Your Position -->
                    <div class="input-group mb-3">
                        <input type="text" class="form-control" placeholder="Route ID" v-model="routeId" show-clear>
                        <button class="btn btn-outline-secondary" type="submit" @click="submit"
                        style="width: fit-content; height: fit-content;background-color: chartreuse;">Search</button>
                    </div>
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
          v-for="marker in stops"
          :key="marker.stopid"
          :position="{ lat: marker.latitude, lng: marker.longitude }"
          :visible="marker.visibility"
          :clickable="true"
        >
        </GMapMarker>
      </GMapMap>
    </div>
            <div>
                {{ stops }}
            </div>
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