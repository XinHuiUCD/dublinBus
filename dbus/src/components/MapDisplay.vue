<template>
  <div class="row">
    <div class="top" id="Menu">
      <div id="title">
        <h1>
          <span style="color: black">Plan Your Journey</span>&nbsp;
          <span style="color: gray">With DublinBus</span>
        </h1>

        <div id="functions">

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

          <!-- Your Position -->
          <div class="grid text-center">
            <div class="g-col-6">
              <GMapAutocomplete placeholder="Enter your starting point" @place_changed="setPlace" v-model="address"
                style="width:75%; border-radius: 4px;">
              </GMapAutocomplete>
              <button class="btn" @click="addMarkerStart()"><img style="width: fit-content; height: fit-content;"
                  src="https://img.icons8.com/color/48/000000/place-marker--v1.png" /></button>
            </div>

            <!-- Your Destination -->

            <div class="g-col-6">
              <GMapAutocomplete placeholder="Enter your destination" @place_changed="setPlace" v-model="addresstwo"
                id="enterYourDestionation" style="width:75%; border-radius: 4px;">
              </GMapAutocomplete>
              <button id="endMarkerBtn" class="btn" @click="addMarkerEnd()"><img
                  style="width: fit-content; height: fit-content;"
                  src="https://img.icons8.com/color/48/000000/place-marker--v1.png" /></button>
            </div>
            <div class="g-col-6">
              <!-- Select date and time -->
              <div class="block">
                <el-date-picker v-model="pickdate" type="datetime" placeholder="Select date and time"
                  style="height: 40px; width: 81.77%" />
              </div>
            </div>

          </div>
          <el-divider border-style="dashed" />


          <!-- fare calculator -->
          <el-button @click="fareCalculation(); showFareInfo();" class="btn btn-outline-secondary" id="fareButton"
            type="submit" style="
              margin-top: 10px;
              margin-left: 20px;
              width: 60px;
              height: 60px;
              display:none;
            ">
            €️<br />Fare
          </el-button>
          <div class="form-popup" id="myForm">
            <div class="form-container">
              <h2>Fare Estimation</h2>
              <div v-if="this.journey == 'long'">
                <h4>Long Zone</h4>
                <table id="realTimeTable" style="margin: 0 auto 7px; ">
                  <tr>
                    <th>Type</th>
                    <th>Leap Card</th>
                    <th>Cash Fare</th>

                  </tr>

                  <tr>
                    <td>Adult</td>
                    <td>€2.00</td>
                    <td>€2.60</td>

                  </tr>
                  <tr>
                    <td>Student</td>
                    <td>€1.00</td>
                    <td>€2.60</td>

                  </tr>
                  <tr>
                    <td>Child</td>
                    <td>€0.65</td>
                    <td>€0.90</td>

                  </tr>
                </table>
              </div>
              <div v-else-if="this.journey == 'short'">
                <h4>Short Zone</h4>
                <table id="realTimeTable" style="margin: 0 auto 7px; ">
                  <tr>
                    <th>Type</th>
                    <th>Leap Card</th>
                    <th>Cash Fare</th>

                  </tr>

                  <tr>
                    <td>Adult</td>
                    <td>€1.30</td>
                    <td>€1.70</td>

                  </tr>
                  <tr>
                    <td>Student</td>
                    <td>€0.65</td>
                    <td>€1.70</td>

                  </tr>
                  <tr>
                    <td>Child</td>
                    <td>€0.65</td>
                    <td>€0.90</td>

                  </tr>
                </table>
              </div>
              <button type="button" class="btn cancel" @click="closeFareInfo();">Close</button>
            </div>
          </div>


          <el-button class="btn btn-outline-secondary" id='resetButton' type="submit" style="
              margin-top: 10px;
              margin-left: 20px;
              width: 60px;
              height: 60px;
            " @click="resetSearch()">
            Reset
          </el-button>

          <!-- submit -->
          <el-button :plain="true" class="btn btn-outline-secondary" type="submit" id='submitButton'
            @click="errorAlert(); showDiv(); getDirection();  showFareButton(); fareCalculation();  " style="
              margin-top: 10px;
              margin-left: 20px;
              width: 70px;
              height: 60px;
              background-color: chartreuse;
            ">
            Submit
          </el-button>
          <el-divider border-style="dashed"/>
          <!-- ml result -->
          <div id="MlResult" v-if="this.check_if_marker_pressed == true"
            style=" margin-left: 20px; margin-top: 10px; width: 160px; height: 60px; display:none; box-shadow: 3px 3px 3px lightblue;">
            Our predicted travel time is: <strong>{{ Number(this.durationResult).toFixed(2) }} minutes</strong>
          </div>

          <!-- text direction -->
          <div class="sidebar-collapse" id="sidebarTextdirections" style="display:none;">
            <el-collapse v-model="activeName" accordion>
              <el-collapse-item title="Show/Hide Text Directions" name="1">
                <div id="sidebar"></div>
              </el-collapse-item>
            </el-collapse>
          </div>
        </div>
      </div>
    </div>

    <div id="container">

      <div class="button" id="map" style="align-items: center; margin-top: 1%;">
        <GMapMap :center="center" :zoom="15" :options="options" map-type-id="terrain" style="width: 100%; height: 700px"
          ref="mapTheme">
          <div style="padding-top: 10px; margin-left: auto; margin-right: auto;">
            <el-button type="button" id="hideMarkers" @click="hideAllMarkers()" class="btn btn-outline-info"
              style="color: #1dc1ec">
              Hide/Show Markers
            </el-button>

          </div>
          <GMapMarker v-for="marker in All_stops" :key="marker.stop_id"
            :position="{ lat: marker.stop_lat, lng: marker.stop_lon }" :visible="marker.visibility"
            :title="marker.stop_name" :clickable="true" :icon='{
              url: "https://img.icons8.com/fluency/48/000000/bus.png",
              scaledSize: { width: 40, height: 40 }
            }' @click="openMarker(marker.stop_id); realTimeBusData(marker.stop_num)">
            <GMapInfoWindow :closeclick="true" @closeclick="openMarker(null)"
              :opened="openedMarkerID === marker.stop_id">
              <div style="text-align: center;  height:200px; overflow:auto">
                <h5>Real Time Information</h5>
                <div>
                  <div v-if="loading" style="margin: 0 auto;">
                    <div class="loader" style="margin: 10px auto;"></div>
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
          <GMapMarker :position="this.coords" />
          <GMapMarker :position="this.destination" />

        </GMapMap>
      </div>
    </div>
  </div>
</template>



<script>
import markerLocations from "./json/BusStopsLongLatCSVComma.json";

// eslint-disable-next-line
import { ref } from "vue";
import $ from 'jquery';
// eslint-disable-next-line
import { variableDeclarator } from "@babel/types";
import { ElMessage } from 'element-plus';

const activeName = ref('1')
const pickdate = ref("");
const submit = ref("");

// variable for toggle switch
var clicked = true;


const directionRenderers = [];


let busDistance = 0;
let direction = ref('');
let routeId = ref('');
let month = ref('');
let dayOfWeek = ref('');
let hour = ref('');
let temp = ref(0.0);
let wind_speed = ref(0.0);
let start_location = ref({});
let end_location = ref({});
let diff = ref(0.0);
let duration = ref(0);

let durationDuration = 0;
let loadedDirections = false;



const submitPredict = (routeId) => {
  // preprocess weather data
  $.ajax({
    url: "https://api.openweathermap.org/data/2.5/onecall?lat=53.344&lon=-6.2672&units=metric&exclude=minutely,daily&appid=d6e328f404504a98d4be6d3942d42e9e",
    type: "GET",
    async: false,
    success(resp) {
      //console.log(resp);
      month.value = pickdate.value.toString().substring(4, 7);
      dayOfWeek.value = pickdate.value.toString().substring(0, 3);
      hour.value = pickdate.value.toString().substring(16, 18);
      temp.value = resp.current.temp;
      wind_speed.value = resp.current.wind_speed;
      $.ajax({
        url: "http://ipa-011.ucd.ie:80/getPredict",
        type: "GET",
        async: false,
        data: {
          routeId: routeId,
          direction: direction.value,
          month: month.value,
          dayOfWeek: dayOfWeek.value,
          hour: hour.value,
          temp: temp.value,
          wind_speed: wind_speed.value,
        },
        success(resp) {
          diff.value = resp.result;
          console.log("resp:", diff.value);
        }
      });
    }
  });
}

export default {
  name: "DrawGoogleMap",

  return: {
    routeId,
    direction,
    month,
    hour,
    temp,
    wind_speed,
    start_location,
    end_location,
    diff,
    duration,
    submitPredict,

  },

  data() {
    return {
      check_if_marker_pressed: false,
      pickdate,
      address: "",
      addresstwo: "",
      submit,
      activeName,
      distanceJourney: "",
      zone: null,
      routIdArray: [],
      journey: "",
      durationResult: 0,
      options: {
        styles: [
          {
            featureType: "transit",
            stylers: [{ visibility: "off", }],
          },
        ],
      },

      center: {
        lat: 53.349722,
        lng: -6.260278,
      },
      // for current location marker
      coords: {
        lat: null,
        lng: null,
      },
      destination: {
        lat: null,
        lng: null,
      },
      currentLocation: null,
      All_stops: markerLocations,
      openedMarkerID: null,
      infoWindow: {
        position: {
          lat: 0,
          lng: 0,
        },
        open: false,
        template: "",
      },
      resultBusTimesSched: {},
      loading: false,

      //for cluster marker
      clusterIcon: [
        {
          textColor: '#00CCFF',
          textSize: 20,
          url: 'https://github.com/googlemaps/v3-utility-library/raw/bd55f49fc8492207d30e179d280c00aa8b5016e0/markerclusterer/images/m1.png',
          height: 52,
          width: 53,
          // offset:(100,100),
        },
        {
          textColor: 'yellow',
          textSize: 20,
          url: 'https://github.com/googlemaps/v3-utility-library/raw/bd55f49fc8492207d30e179d280c00aa8b5016e0/markerclusterer/images/m2.png',
          height: 55,
          width: 56
        },
        {
          textColor: 'red',
          textSize: 20,
          url: 'https://github.com/googlemaps/v3-utility-library/raw/bd55f49fc8492207d30e179d280c00aa8b5016e0/markerclusterer/images/m3.png',
          height: 65,
          width: 66
        },
        {
          textColor: '#FF33CC',
          textSize: 20,
          url: 'https://github.com/googlemaps/v3-utility-library/raw/bd55f49fc8492207d30e179d280c00aa8b5016e0/markerclusterer/images/m4.png',
          height: 77,
          width: 78
        },
      ],


    };
  },

  mounted() {
    this.setLocationLatLng();
    this.getDirection();
    this.hideMarkers_onload();

    this.$refs.mapTheme.$mapPromise.then((mapObject) => {
      console.log("map is loaded now", mapObject);
    });



  },
  methods: {
    setPlace(place) {
      this.currentPlace = place;
    },

    errorAlert() {
      console.log("error alert")
      if (this.check_if_marker_pressed == false) {
        ElMessage({
          message: 'Make Sure to enter an address and click the marker icon',
          type: 'error',
        })

      }
    },

    hideMarkers_onload() {
      for (let i = 0; i < this.All_stops.length; i++) {
        this.All_stops[i]["visibility"] = false;
      }

    },

    showDiv() {
      console.log("show ddiv", durationDuration);
      if(this.check_if_marker_pressed == true){
        document.getElementById('sidebarTextdirections').style.display = "inline";


      }

      document.getElementById('MlResult').style.display = "inline";
    },
    showFareButton() {
      document.getElementById('fareButton').style.display = "inline";
    },

    setLocationLatLng: function () {
      navigator.geolocation.getCurrentPosition((geolocation) => {
        this.center = {
          lat: geolocation.coords.latitude,
          lng: geolocation.coords.longitude,
        };
        this.coords = {
          lat: geolocation.coords.latitude,
          lng: geolocation.coords.longitude,
        };
      });
    },

    addMarkerStart() {
      console.log("add maker");
      this.coords = {
        lat: this.currentPlace.geometry.location.lat(),
        lng: this.currentPlace.geometry.location.lng(),
      };
    },

    addMarkerEnd() {
      this.check_if_marker_pressed = true;

      console.log("add maker");
      this.destination = {
        lat: this.currentPlace.geometry.location.lat(),
        lng: this.currentPlace.geometry.location.lng(),
      };
    },

    hideAllMarkers() {
      if (clicked) {
        for (let i = 0; i < this.All_stops.length; i++) {
          this.All_stops[i]["visibility"] = true;
        }
        clicked = false;
      } else {
        for (let i = 0; i < this.All_stops.length; i++) {
          this.All_stops[i]["visibility"] = false;
        }
        clicked = true;
      }
    },
    openMarker(id) {
      this.openedMarkerID = id;
    },
    realTimeBusData(busstopNO) {
      this.loading = true
      fetch('http://127.0.0.1:9000/getRealTime/' + busstopNO)
        .then(response => response.json())
        .then(data => this.resultBusTimesSched = data)
        .finally(() => (this.loading = false))


    },

    getDirection() {
      // eslint-disable-next-line
      var directionsService = new google.maps.DirectionsService();
      // eslint-disable-next-line
      const self = this;
      // eslint-disable-next-line
      var directionsDisplay = new google.maps.DirectionsRenderer();
      directionsDisplay.setMap(this.$refs.mapTheme.$mapObject);
      directionRenderers.push(directionsDisplay);
      directionsDisplay.setPanel(document.getElementById("sidebar"));
      function calculateAndDisplayRoute(
        directionsService,
        directionsDisplay,
        start,
        destination
      ) {
        directionsService.route(
          {
            origin: start,
            destination: destination,
            travelMode: "TRANSIT",

            transitOptions: {
              // eslint-disable-next-line
              modes: [google.maps.TransitMode.BUS],
            },
          },
          (response, status) => {
            if (status === "OK") {
              loadedDirections = true;

              console.log("response", response);
              // for loop to get rout ids of mutli bus trips and add to an array
              for (var journeyStep of response.routes[0].legs[0].steps) {
                if (journeyStep.travel_mode == "TRANSIT") {
                  console.log("bus Routess short name", journeyStep.transit.line.short_name);
                  self.routIdArray.push(journeyStep.transit.line.short_name);

                }

              }
              console.log("routeId array", self.routIdArray)

              busDistance = (response.routes[0].legs[0].steps[1].distance.value);
              console.log("bus Distance", busDistance)
              // preprocess location
              start_location.value = response.routes[0].legs[0].start_location;
              end_location.value = response.routes[0].legs[0].end_location;
              //console.log("start", start_location.value);
              //console.log("end", end_location.value);
              let dx = ref(0), dy = ref(0);
              dy.value = (end_location.value.lat() - start_location.value.lat()) * 100;
              dx.value = (end_location.value.lng() - start_location.value.lng()) * 100;
              if (dy.value > 0 || dx.value > 0)
                direction.value = '2';
              else if (dy.value < 0 || dx.value < 0)
                direction.value = '1';
              //console.log("x", dx.value);
              //console.log("y", dy.value);
              //console.log(direction.value);
              duration.value = response.routes[0].legs[0].duration.value;
              for (var i = 0; i < self.routIdArray.length; i++) {
                console.log("i: ", i);
                submitPredict(self.routIdArray[i]);
                console.log("duration difference", diff.value);
                duration.value += diff.value;
                console.log("duration: ", duration.value);
              }


              durationDuration = duration.value / 60;
              self.durationResult = durationDuration;
              console.log("durationDuration: ", durationDuration);

              directionsDisplay.setDirections(response);
            } else {
              window.alert("Directions request failed due to " + status);
            }
            return {
              busDistance,
              durationDuration,
              loadedDirections
            }
          }


        );
      }

      calculateAndDisplayRoute(
        directionsService,
        directionsDisplay,
        this.coords,
        this.destination
      );

    },

    togglefav: function () {
      this.$emit("togglefav", !this.is_fav);
    },
    resetSearch() {
      console.log("reset");
      this.routIdArray = [];
      directionRenderers.forEach(directionsDisplay => {
        directionsDisplay.setMap(null)
        directionsDisplay.setPanel(null)

      });
      directionRenderers.length = 0;
      document.getElementById('MlResult').style.display = "none";
      document.getElementById('fareButton').style.display = "none";
      document.getElementById("myForm").style.display = "none";
      document.getElementById('sidebarTextdirections').style.display = "none";


    },

    fareCalculation() {
      console.log("this is the array", busDistance)
      if (busDistance < 3000) {
        this.journey = "short"
      }
      else {
        this.journey = "long"
      }
    },
    showFareInfo() {
      document.getElementById("myForm").style.display = "block";


    },
    closeFareInfo() {
      document.getElementById("myForm").style.display = "none";

    },
  },
  showUserLocationOnTheMap(latitude, longitude) {
    // eslint-disable-next-line
    let map = new google.maps.Map(document.getElementById("map"), {
      zoom: 15,
      // eslint-disable-next-line
      center: new google.maps.LatLng(latitude, longitude),
      // eslint-disable-next-line
      mapTypeId: google.maps.MapTypeID.ROADMAP,
    });
    // eslint-disable-next-line
    new google.maps.Marker({
      // eslint-disable-next-line
      position: new google.maps.LatLng(latitude, longitude),
      map: map,
    });
  },

};

// code ref: https://jsfiddle.net/irhamkim/20pegws2/2/  https://developers.google.com/maps/documentation/javascript/directions#TransitOptions
</script>

<style scoped>
#clusterIcon {
  position: absolute;
  margin-left: -20px;
  margin-top: -20px;
}

.pac-target-input {
  padding: 10px;
  width: 90%;
}

/* reference for side pannel of text directions: https://developers.google.com/maps/documentation/javascript/examples/directions-panel */
#container {
  display: flex;
}



#map {
  flex-basis: 0;
  flex-grow: 4;
  height: 100%;
}

#map {
  flex: auto;
}


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

/* Loader adapted from https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_loader */
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


@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');

h1,
h2,
h4,
#fareButton,
#submitButton,
#resetButton {
  font-family: 'Roboto', sans-serif;

}

/* reference for fare pop-up https://www.w3schools.com/howto/howto_js_popup_form.asp */
.form-popup {
  display: none;
  position: fixed;
  bottom: 10px;
  right: 120px;
  border: 3px solid #f1f1f1;
  z-index: 9;
}

/* Add styles to the form container */
.form-container {
  max-width: 300px;
  padding: 10px;
  background-color: white;
}



/* Set a style for the submit/login button */
.form-container .btn {
  background-color: #04AA6D;
  color: white;
  padding: 8px 12px;
  border: none;
  cursor: pointer;
  width: 50%;
  margin-bottom: 10px;
  opacity: 0.8;
}

/* Add a red background color to the cancel button */
.form-container .cancel {
  background-color: red;
}

/* Add some hover effects to buttons */
.form-container .btn:hover,
.open-button:hover {
  opacity: 1;
  cursor: pointer;
}



</style>