<template>
	<div id="map" style="align-items: center;">
		<GMapMap :center="center" :zoom="15" map-type-id="terrain" style="width: 100%; height: 700px" ref="mapTheme">
		
		

			<div style="padding-top: 10px;">
				<button type="button" @click="hideAllMarkers()" class="btn btn-outline-info">Hide/Show Makers</button>
				<button  class="btn btn-outline-info" @click="getDirection">show route</button>
			</div>
			<GMapMarker
			
				v-for="marker in Hellodata " :key="marker.stop_id"
				:position="{ lat: marker.stop_lat, lng: marker.stop_lon}" 
				:visible="marker.visibility"
				:title="marker.stop_name" :clickable="true" 
				:icon="'https://img.icons8.com/fluency/48/000000/bus.png'"
				@click="openMarker(marker.stop_id)">

				<GMapInfoWindow :closeclick="true" @closeclick="openMarker(null)"
					:opened="openedMarkerID === marker.stop_id">

					<div style="text-align: center;">
						<h5>Real Time Information</h5>
						<div>Stop Name: {{ marker.stop_name }} </div>
						<table style=" margin: 0 auto;">
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
			<GMapMarker :position="this.coords">
    </GMapMarker>
    <GMapMarker :position="this.destination">
    </GMapMarker>
	
		</GMapMap>

	</div>
	<div id="Menu">
		<div id="title">
	<div class="input-group mb-3">
	<GMapAutocomplete
       placeholder="Enter your starting Point"
       @place_changed="setPlace"
    >
  </GMapAutocomplete><button class="btn" @click="addMarkerStart()">Add Marker</button>
	</div>


	<div class="input-group mb-3">
	<GMapAutocomplete
       placeholder="Enter your destination"
       @place_changed="setPlace"
    >
  </GMapAutocomplete><button class="btn" @click="addMarkerEnd()">Add Marker</button>
	</div>
	</div>
</div>
</template>



<script>
	import store from "@/store/index";
	import markerLocations from "./json/BusStopsLongLatCSV.json"
	// importing journey planner so I can use results from input fields in map
    // import JourneyPlan from './JourneyPlan.vue'
	// import DirectionsRenderer from "@/components/DirectionsRenderer";




// variable for toggle switch 
	var clicked = true;


	export default {
		name: "DrawGoogleMap",
		// components: {
        //   DirectionsRenderer
        // },
		store,

		data() {
			return {
				center: {
					lat: 53.349722,
					lng: -6.260278
				},
				// for current location marker
				coords: {
				lat: null,
				lng: null
      },
      destination: {
        lat: null,
        lng:  null
      },

				currentLocation: null,
				Hellodata: markerLocations,
				openedMarkerID: null,

				infoWindow: {
					position: {
						lat: 0,
						lng: 0
					},
					open: false,
					template: ''
				}

			};
		},

		mounted() {
			this.setLocationLatLng();
			this.getDirection();
			this.$refs.mapTheme.$mapPromise.then((mapObject) => {
      console.log('map is loaded now', mapObject);
    });
		},

		methods: {

			setPlace(place) {
      this.currentPlace = place;
    },
			setLocationLatLng: function() {
				navigator.geolocation.getCurrentPosition(geolocation => {
					this.center = {
						lat: geolocation.coords.latitude,
						lng: geolocation.coords.longitude
					};
					this.coords = {
						lat: geolocation.coords.latitude,
						lng: geolocation.coords.longitude

					};
				});


			},
			addMarkerStart() {
			console.log("add maker")
       this.coords = {
        lat: this.currentPlace.geometry.location.lat(),
        lng: this.currentPlace.geometry.location.lng(),
      };
      
    },
		addMarkerEnd() {
			console.log("add maker")
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
				this.openedMarkerID = id
			},
			getDirection: function() {
// eslint-disable-next-line
      var directionsService = new google.maps.DirectionsService;
// eslint-disable-next-line
      var directionsDisplay = new google.maps.DirectionsRenderer;
      directionsDisplay.setMap(this.$refs.mapTheme.$mapObject);

      function calculateAndDisplayRoute(directionsService, directionsDisplay, start, destination) {
        directionsService.route({
          origin: start,
          destination: destination,
          travelMode: 'TRANSIT',
		
		transitOptions: {
			// eslint-disable-next-line
    modes: [google.maps.TransitMode.BUS]
  }
        }, function(response, status) {
          if (status === 'OK') {
            directionsDisplay.setDirections(response);
          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });
      }

      calculateAndDisplayRoute(directionsService, directionsDisplay, this.coords, this.destination);
    }

		}

	};

	// code ref: https://jsfiddle.net/irhamkim/20pegws2/2/  https://developers.google.com/maps/documentation/javascript/directions#TransitOptions
</script>

<style scoped>

.pac-target-input {
  padding: 10px;
  width: 100%;
}
</style>