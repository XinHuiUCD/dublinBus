<template>
    <ContentBase>
        <div id="Menu">
            <div id="title">
                <div id="function">
                    <!-- Your Position -->
                    <!-- <div class="input-group mb-3">
                        <button class="btn btn-outline-secondary" type="button" id="button-addon1">🔍</button>
                        <input type="text" class="form-control" placeholder="RouteID" v-model="routeId" show-clear>
                    </div> -->
                    <div>
                      <label for="browser">Choose a route to display on the map</label>
                      <input list="browsers" name="browser" id="browser" v-model="routeId">
                      <datalist id="browsers">
                        <div v-for="(route, index) in busRoutes" :key="route">
                        <option :value="busRoutes[index]"></option>
                        </div>
                      </datalist>
                        <button class="btn btn-outline-secondary" type="submit" id="button-addon1" @click="submit">🔍</button>
                    </div>
<!-- <div v-for="(route, index) in busRoutes" :key="route">
{{busRoutes[index]}}
</div> -->

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
          :title="marker.searchname"
          :clickable="true"
          :icon='{url: "https://img.icons8.com/fluency/48/000000/bus.png",
          scaledSize: {width: 40, height: 40}}'
          @click="openMarker(stops.stops[index].stopid)"

        >

        <GMapInfoWindow
            :closeclick="true"
            @closeclick="openMarker(null)"
            :opened="openedMarkerID === stops.stops[index].stopid"
          >
            <div style="text-align: center">
              <h5>Real Time Information</h5>
              <div>Stop Name: {{ stops.stops[index].searchname }}</div>
              <table style="margin: 0 auto">
                <tr>
                  <th>Bus Route</th>
                  <th>Arrival</th>
                </tr>
                <tr>
                  <td>145</td>
                  <td>6 mins</td>
                </tr>
                <tr>
                  <td>46a</td>
                  <td>12 mins</td>
                </tr>
              </table>
            </div>
          </GMapInfoWindow>
        </GMapMarker>
      </GMapMap>
    </div>
          
        </div>
    </ContentBase>
</template>

<script>
import ContentBase from '../components/ContentBase.vue'
import busRoutesJson from "../assets/json/route.json";

// import VueGoogleAutocomplete from "vue-google-autocomplete"
import { ref } from 'vue';
import $ from 'jquery';

export default {
    name: "RouteStopInfoView",
    components: {
        ContentBase,
    },

    data() {
        return {

              openedMarkerID: null,
              busRoutes: busRoutesJson,


        }
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
    },
    methods: {
         openMarker(id) {
      this.openedMarkerID = id;
    },

    }
}
</script>

<style scoped>
</style>