<template>
    <ContentBase>
        <!-- go up -->
        <el-backtop :bottom="100">
            <div style="
        height: 100%;
        width: 100%;
        background-color: var(--el-bg-color-overlay);
        box-shadow: var(--el-box-shadow-lighter);
        text-align: center;
        line-height: 40px;
        color: #1989fa;
      ">
                UP
            </div>
        </el-backtop>
        <div id="Menu">
            <h2 style="text-align:center">
                <span style="color: black">Bus Routes</span>&nbsp;
                <span style="color: gray">and Real Time Info</span>
            </h2>
            <div id="title">

                <div class="grid text-center" id="function">
                    <div class="g-col-6">
                        <label type="danger" plain disabled id="texts"
                            style="padding-right:5px; font-weight: bolder; font-size: large; margin-bottom: 2%;">Choose
                            a
                            route to display on the map<br />Click the stop to view
                            the real time data</label>
                        <el-divider border-style="dashed" />

                        <el-input list="browsers" name="browser" id="browser" v-model="routeId"
                            placeholder="Choose a route" clearable style="width:70%" />
                        <datalist id="browsers">
                            <div v-for="(route, index) in busRoutes" :key="route">
                                <option :value="busRoutes[index]"></option>
                            </div>
                        </datalist>
                        <button class="btn btn-outline-secondary" type="submit" id="button-addon1"
                            @click="submit">🔍</button>
                    </div>


                    <div class="g-col-6" id="addFavourite" style="margin-top:2%">
                        <p>
                            <el-input id="addFavourite" v-model="newFavourite" list="browsers"
                                placeholder="Add Favourite Route" style="width:70%" clearable />
                            <datalist id="browsers">
                                <div v-for="(favourite, index) in favourites" :key="favourite">
                                    <option :value="favourites[index]"></option>

                                </div>
                            </datalist>
                            <button class="btn btn-outline-secondary" type="submit" id="button-addon1"
                                @click="addFavourite">❤️</button>
                        </p>
                        <el-collapse v-model="activeName" accordion>
                            <el-collapse-item title="Your Favourite Routes" name="1">
                                <div v-for="(favourite, index) in favourites" :key="favourite">
                                    <p>
                                        <span class="favourite" style="font-weight:bolder" type="submit"
                                            @click="showFavoriteRoute($event)">{{ favourite }}</span>
                                        <button class="btn btn-outline-secondary" type="submit" id="button-addon1"
                                            @click="removeFavourite(index)">✖️</button>
                                    </p>
                                </div>
                            </el-collapse-item>
                        </el-collapse>
                    </div>




                </div>
            </div>
            <div class="button" id="map" style="align-items: center; margin-top: 1%">
                <GMapMap :center="center" :zoom="12" map-type-id="terrain" style="width: 100%; height: 700px"
                    ref="mapTheme">
                    <GMapMarker v-for="(marker, index) in stops.stops" :key="marker"
                        :position="{ lat: stops.stops[index].latitude, lng: stops.stops[index].longitude }"
                        :visible="marker.visibility" :title="marker.searchname" :clickable="true" :icon='{
                            url: "https://img.icons8.com/fluency/48/000000/bus.png",
                            scaledSize: { width: 40, height: 40 }
                        }' @click="openMarker(stops.stops[index].stopid); realTimeBusData(stops.stops[index].stopid)">

                        <GMapInfoWindow :closeclick="true" @closeclick="openMarker(null)"
                            :opened="openedMarkerID === stops.stops[index].stopid">
                            <div style="text-align: center;  height:200px; overflow:auto">
                                <h5>Real Time Information</h5>
                                <div>Stop Name: {{ stops.stops[index].searchname }}</div>
                                <div>
                                    <div v-if="loading" style="margin: 0 auto;">
                                        <div class="loader" style="margin: 0 auto;"></div>
                                        <div>Loading Real Time Data</div>
                                    </div>
                                    <div v-else>

                                        <table id="realTimeTable" style="margin: 0 auto;">
                                            <tr>
                                                <th>Bus Route</th>
                                                <th>Destination</th>
                                                <th>Arrival</th>

                                            </tr>

                                            <tr v-for="busInfo in resultBusTimesSched" :key="busInfo">
                                                <td>{{ busInfo.Route }}</td>
                                                <td>{{ busInfo.Destination }}</td>
                                                <td>{{ busInfo.Arrival }}</td>

                                            </tr>
                                        </table>
                                    </div>
                                </div>

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
import { ref } from 'vue';
import $ from 'jquery';

const activeName = ref('1')

export default {
    name: "RouteStopInfoView",
    components: {
        ContentBase,
    },

    data() {
        return {
            openedMarkerID: null,
            currentLocation: null,
            busRoutes: busRoutesJson,
            realTimeResults: null,
            resultBusTimesSched: {},
            loading: false,
            favourites: [],
            newFavourite: null,
            activeName,
        }
    },


    setup() {
        let stops = ref([]);
        let routeId = ref('');
        const submit = () => {
            $.ajax({
                url: "http://ipa-011.ucd.ie:80/getinfo",
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

        const showFavoriteRoute = (e) => {
            $.ajax({
                url: "http://ipa-011.ucd.ie:80/getinfo",
                type: "GET",
                data: {
                    routeId: e.currentTarget.innerText,
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
            showFavoriteRoute,
            center: {
                lat: 53.349722,
                lng: -6.260278,
            },
        }
    },
    mounted() {
        if (localStorage.getItem('favourites')) {
            try {
                this.favourites = JSON.parse(localStorage.getItem('favourites'));
            } catch (e) {
                localStorage.removeItem('favourites');
            }
        }
    },
    methods: {
        openMarker(id) {
            this.openedMarkerID = id;
        },
        realTimeBusData(busstopNO) {
            this.loading = true
            fetch('http://ipa-011.ucd.ie:80/getRealTime/' + busstopNO)
                .then(response => response.json())
                .then(data => this.resultBusTimesSched = data)
                .finally(() => (this.loading = false))


        },
        addFavourite() {

            if (!this.favourites.includes(this.newFavourite)) {
                // console.log('true')
                this.favourites.push(this.newFavourite);
            } else {
                console.log('already added')
            }

            this.newFavourite = '';
            this.saveFavourite();
            // console.log("add favourite complete")
            console.log(this.favourites)
        },
        removeFavourite(x) {
            this.favourites.splice(x, 1);
            this.saveFavourite();
            // console.log("remove favourite complete")
        },
        saveFavourite() {
            const parsed = JSON.stringify(this.favourites);
            localStorage.setItem('favourites', parsed);
            // console.log("save favourite complete")
        },

    }
}
</script>

<style scoped>
#realTimeTable tr:nth-child(even) {
    background-color: #f2f2f2;
}

#realTimeTable tr:hover {
    background-color: #ddd;
}

#realTimeTable th {
    background-color: #009B77;
}

#realTimeTable td,
#realTimeTable th {
    border: 1px solid #ddd;
}

.loader {
    border: 16px solid #f3f3f3;
    border-radius: 50%;
    border-top: 16px solid #3498db;
    width: 30px;
    height: 30px;
    -webkit-animation: spin 2s linear infinite;
    /* Safari */
    animation: spin 2s linear infinite;
}

/* Safari */
@-webkit-keyframes spin {
    0% {
        -webkit-transform: rotate(0deg);
    }

    100% {
        -webkit-transform: rotate(360deg);
    }
}

@keyframes spin {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}
</style>