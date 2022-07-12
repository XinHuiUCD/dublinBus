<template>
	<div id="map" style="align-items: center;">
		<GMapMap :center="center" :zoom="15" map-type-id="terrain" style="width: 100%; height: 700px" ref="mapTheme">


			<div style="padding-top: 10px;">
				<button type="button" @click="hideAllMarkers()" class="btn btn-outline-info">Hide/Show Makers</button>
				<button class="btn btn-outline-info" @click="getDirection">show route</button>
			</div>
			<GMapMarker v-for="marker in Hellodata " :key="marker.stop_id"
				:position="{ lat: marker.stop_lat, lng: marker.stop_lon }" :visible="marker.visibility"
				:title="marker.stop_name" :clickable="true" :icon="'https://img.icons8.com/fluency/48/000000/bus.png'"
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

</template>



<script>
import store from "@/store/index";
import markerLocations from "./json/BusStopsLongLatCSV.json"
// importing journey planner so I can use results from input fields in map
import JourneyPlan from './JourneyPlan.vue'



// variable for toggle switch 
var clicked = true;


export default {
	name: "DrawGoogleMap",
	components: {
	},
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
				lat: 53.4072,
				lng: -6.1238
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

		initMap() {
			const map = new window.google.maps.Map(document.getElementById("map"));
			this.$store.commit("initMap", map);
		},

		setPlace(loc) {
			this.currentLocation = loc;
		},
		setLocationLatLng: function () {
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
		getDirection: function () {
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
				}, function (response, status) {
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
</style>
