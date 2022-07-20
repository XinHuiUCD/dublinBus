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
					<div>
						<div class="col-8">
							<div class="input-group mb-3">
								<GMapAutocomplete placeholder="Enter your starting Point" @place_changed="setPlace"
									ref="address">
								</GMapAutocomplete>
								<button class="btn" @click="addMarkerStart()">Add Marker</button>
							</div>

							<!-- Your Destination -->
							<div class="input-group mb-3">
								<GMapAutocomplete placeholder="Enter your destination" @place_changed="setPlace"
									ref="addresstwo">
								</GMapAutocomplete>
								<button class="btn" @click="addMarkerEnd()">Add Marker</button>
							</div>
						</div>

						<div class="col-4" style="overflow:scroll;">
							<div id="textDirections"></div>
						</div>
					</div>


					<!-- Select date and time -->
					<div class="block">
						<el-date-picker v-model="pickdate" type="datetime" placeholder="Select date and time"
							style="height: 40px; width: 100%" />
					</div>

					<!-- swap address -->
					<button class="btn btn-outline-secondary" @click="swapAddress(address, addresstwo)"
						style="margin-top: 10px; width: 60px; height: 60px">
						↕️<br />Swap
					</button>

					<!-- fare calculator -->
					<button class="btn btn-outline-secondary" @click="fareCalcutor()" type="submit" style="
              margin-top: 10px;
              margin-left: 20px;
              width: 60px;
              height: 60px;
            ">
						€️<br />Fare
					</button>

					<!-- submit -->
					<button class="btn btn-outline-secondary" type="submit" @click="getDirection" style="
              margin-top: 10px;
              margin-left: 20px;
              width: 70px;
              height: 60px;
              background-color: chartreuse;
            ">
						Submit
					</button>

					<!-- schedule -->


					<!-- <div style="height: 300px; margin-top: 20px;">
					<el-steps direction="vertical" :active="1">
						<el-step title="Start" description="39A" />
						<el-step title="Futher Info" description="" />
						<el-step title="End" />
					</el-steps>
				</div> -->
				</div>
			</div>
		</div>
		<div class="button" id="map" style="align-items: center; margin-top: 1%">
			<GMapMap :center="center" :zoom="15" map-type-id="terrain" style="width: 100%; height: 700px"
				ref="mapTheme">
				<div style="padding-top: 10px">
					<button type="button" @click="hideAllMarkers()" class="btn btn-outline-info">
						Hide/Show Makers
					</button>
				</div>

				<GMapMarker v-for="marker in Hellodata" :key="marker.stop_id"
					:position="{ lat: marker.stop_lat, lng: marker.stop_lon }" :visible="marker.visibility"
					:title="marker.stop_name" :clickable="true"
					:icon="'https://img.icons8.com/fluency/48/000000/bus.png'" @click="openMarker(marker.stop_id)">
					<GMapInfoWindow :closeclick="true" @closeclick="openMarker(null)"
						:opened="openedMarkerID === marker.stop_id">
						<div style="text-align: center">
							<h5>Real Time Information</h5>
							<div>Stop Name: {{ marker.stop_name }}</div>
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
				<GMapMarker :position="this.coords" />
				<GMapMarker :position="this.destination" />
			</GMapMap>
		</div>
	</div>
</template>



<script>
// import store from "@/store/index";
import markerLocations from "./json/BusStopsLongLatCSV.json";
// import JourneyPlan from "./JourneyPlan.vue";
// importing journey planner so I can use results from input fields in map
import axios from "axios";
import { ref } from "vue";
// import { ElButton, ElDrawer } from 'element-plus';
// import { CircleCloseFilled } from '@element-plus/icons-vue';

// const visible = ref(false)
const pickdate = ref("");

// variable for toggle switch
var clicked = true;

export default {
	name: "DrawGoogleMap",

	data() {
		return {
			pickdate,
			address: "",
			addresstwo: "",

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
		};
	},
	mounted() {
		this.setLocationLatLng();
		this.getDirection();
		this.$refs.mapTheme.$mapPromise.then((mapObject) => {
			console.log("map is loaded now", mapObject);
		});

		// // eslint-disable-next-line
		// const autocomplete = new google.maps.places.Autocomplete(
		// 	this.$refs["autocomplete"],
		// 	{
		// 		// eslint-disable-next-line
		// 		bounds: new google.maps.LatLngBounds(
		// 			// eslint-disable-next-line
		// 			new google.maps.LatLng(53.3498, -6.2603)
		// 		),
		// 	}
		// );
		// this.$autocomplete.addListener('place_changed', () => {
		// 	this.$emit('place_changed', this.$autocomplete.getPlace())
		// });

		// // eslint-disable-next-line
		// // const autocomplete2 = new google.maps.places.Autocomplete(
		// // 	this.$refs["autocomplete2"],
		// // 	{
		// // 		// eslint-disable-next-line
		// // 		bounds: new google.maps.LatLngBounds(
		// // 			// eslint-disable-next-line
		// // 			new google.maps.LatLng(53.3498, -6.2603)
		// // 		),
		// // 	}
		// // );
		// this.addresstwo.addListener("place_changed", () => {
		//   this.addresstwo = this.addresstwo.getPlace().formatted_address;
		//   console.log(this.addresstwo.getPlace());
		// });
	},
	methods: {
		setPlace(place) {
			this.currentPlace = place;
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
			console.log("add start maker");
			this.coords = {
				lat: this.currentPlace.geometry.location.lat(),
				lng: this.currentPlace.geometry.location.lng(),
			};
		},

		addMarkerEnd() {
			console.log("add end maker");
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

		getDirection: function () {
			// eslint-disable-next-line
			var directionsService = new google.maps.DirectionsService();
			// eslint-disable-next-line
			var directionsDisplay = new google.maps.DirectionsRenderer();
			directionsDisplay.setMap(this.$refs.mapTheme.$mapObject);
			directionsDisplay.setPanel(document.getElementById("textDirections"));
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
							directionsDisplay.setDirections(response);
						} else {
							window.alert("Directions request failed due to " + status);
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
		// Journey Plan

		togglefav: function () {
			this.$emit("togglefav", !this.is_fav);
		},

		swapAddress() {
			const tempAddress = this.address;
			this.address = this.addresstwo;
			this.addresstwo = tempAddress;
			console.log("trying to swap");
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
	width: 70%;
}
</style>