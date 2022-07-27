<template>
  <div class="row">
    <div class="top" id="Menu">
      <div id="title">
        <h1>
          <span style="color: black">Plan Your Journey</span>&nbsp;
          <span style="color: gray">With DublinBus</span>
        </h1>

        <div id="functions">
          <!-- Your Position -->

          <div class="grid text-center">
            <div class="g-col-6">
              <GMapAutocomplete placeholder="Enter your starting point" @place_changed="setPlace" v-model="address"
                style="width:75%">
              </GMapAutocomplete>
              <button class="btn" @click="addMarkerStart()"><img style="width: fit-content; height: fit-content;"
                  src="https://img.icons8.com/color/48/000000/place-marker--v1.png" /></button>
            </div>

            <!-- Your Destination -->

            <div class="g-col-6">
              <GMapAutocomplete placeholder="Enter your destination" @place_changed="setPlace" v-model="addresstwo"
                style="width:75%">
              </GMapAutocomplete>
              <button class="btn" @click="addMarkerEnd()"><img style="width: fit-content; height: fit-content;"
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

          <!-- swap address -->
          <button class="btn btn-outline-secondary" @click="swapAddress(address, addresstwo)"
            style="margin-top: 10px; width: 60px; height: 60px">
            ↕️<br />Swap
          </button>

          <!-- fare calculator -->
          <button @click="fareCalculation(); showFareInfo();" class="btn btn-outline-secondary" id="fareButton"
            type="submit" style="
              margin-top: 10px;
              margin-left: 20px;
              width: 60px;
              height: 60px;
              display:none;
            ">
            €️<br />Fare
          </button>
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


          <button class="btn btn-outline-secondary" type="submit" style="
              margin-top: 10px;
              margin-left: 20px;
              width: 60px;
              height: 60px;
            " @click="resetSearch()">
            Reset
          </button>

          <!-- submit -->

          <button class="btn btn-outline-secondary" type="submit"
            @click="getDirection(); showDiv(); showFareButton(); fareCalculation();" style="
              margin-top: 10px;
              margin-left: 20px;
              width: 70px;
              height: 60px;
              background-color: chartreuse;
            ">
            Submit
          </button>
          <div id="MlResult" class="btn btn-outline-secondary"
            style=" margin-left: 200px; margin-top: 10px; width: 160px; height: 60px; display:none; box-shadow: 3px 3px 3px lightblue;">
            Your predicted travel time is: <strong>20 minutes</strong>
          </div>
        </div>
      </div>
    </div>

    <div id="container">
      <div id="sidebar"></div>
      <div class="button" id="map" style="align-items: center; margin-top: 1%">
        <GMapMap :center="center" :zoom="15" map-type-id="terrain" style="width: 100%; height: 700px" ref="mapTheme">
          <div style="padding-top: 10px; margin-left: auto; margin-right: auto;">
            <button type="button" @click="hideAllMarkers()" class="btn btn-outline-info" style="color: #1dc1ec">
              Hide/Show Makers
            </button>

          </div>
          <GMapMarker v-for="marker in Hellodata" :key="marker.stop_id"
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
import axios from "axios";
import { ref } from "vue";

const pickdate = ref("");
const submit = ref("");

// variable for toggle switch
var clicked = true;


const directionRenderers = [];


let busDistance = 0;



export default {
  name: "DrawGoogleMap",

  data() {
    return {
      pickdate,
      address: "",
      addresstwo: "",
      submit,
      distanceJourney: "",
      zone: null,
      journey: "",

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
      Hellodata: markerLocations,
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


    };
  },

  mounted() {
    this.setLocationLatLng();
    this.getDirection();

    this.$refs.mapTheme.$mapPromise.then((mapObject) => {
      console.log("map is loaded now", mapObject);
    });
  },
  methods: {
    setPlace(place) {
      this.currentPlace = place;
    },

    showDiv() {
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
      console.log("add maker");
      this.destination = {
        lat: this.currentPlace.geometry.location.lat(),
        lng: this.currentPlace.geometry.location.lng(),
      };
    },

    hideAllMarkers() {
      if (clicked) {
        for (let i = 0; i < this.Hellodata.length; i++) {
          this.Hellodata[i]["visibility"] = false;
        }
        clicked = false;
      } else {
        for (let i = 0; i < this.Hellodata.length; i++) {
          this.Hellodata[i]["visibility"] = true;
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

    getDirection: function () {
      // eslint-disable-next-line
      var directionsService = new google.maps.DirectionsService();
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
          function (response, status) {
            if (status === "OK") {
              console.log("response", response);
              console.log("the numbers of stops", response.routes[0].legs[0].steps[1].transit.num_stops);
              busDistance = (response.routes[0].legs[0].steps[1].distance.value);

              console.log("bus Distance", busDistance)
              directionsDisplay.setDirections(response);
            } else {
              window.alert("Directions request failed due to " + status);
            }
            return {
              busDistance
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
      console.log("reset")
      directionRenderers.forEach(directionsDisplay => {
        directionsDisplay.setMap(null)
        directionsDisplay.setPanel(null)

      });
      directionRenderers.length = 0;
      document.getElementById('MlResult').style.display = "none";
      document.getElementById('fareButton').style.display = "none";
      document.getElementById("myForm").style.display = "none";

    },

    swapAddress() {
      const tempAddress = this.address;
      this.address = this.addresstwo;
      this.addresstwo = tempAddress;
      console.log("trying to swap")
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
.pac-target-input {
  padding: 10px;
  width: 90%;
}

/* reference for side pannel of text directions: https://developers.google.com/maps/documentation/javascript/examples/directions-panel */
#container {
  display: flex;
}

#sidebar {
  flex-basis: 15rem;
  flex-grow: 1;
  padding: 1rem;
  max-width: 30rem;
  height: 55%;
  box-sizing: border-box;
  overflow: auto;
}

#map {
  flex-basis: 0;
  flex-grow: 4;
  height: 100%;
}

#map {
  flex: auto;
}

#sidebar {
  flex: 0 1 auto;
  padding: 0;
}

#sidebar>div {
  padding: 0.5rem;
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
h4 {
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