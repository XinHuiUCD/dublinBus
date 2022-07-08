<template>
	<section class="ui two column centered grid">
		<div class="column">
			<form class="ui segment large form">
				<div class="field">
					<div class="ui right icon input large">
						<input type="text" placeholder="Enter your address" v-model="address" id="autocomplete"
							ref="autocomplete" />
						<i class="dot circle link icon" @click="locatorButtonPressed"></i>
					</div>
				</div>
			</form>
		</div>
	</section>
</template>


<script>
	import axios from 'axios'


	export default {
		data() {
			return {
				address: ""
			}
		},

		mounted() {
			// eslint-disable-next-line
			var autocomplete = new google.maps.places.Autocomplete(
				this.$refs["autocomplete"], {
					// eslint-disable-next-line
					bounds: new google.maps.LatLngBounds(
						// eslint-disable-next-line
						new google.maps.LatLng(53.3498, -6.2603)
					),

				}

			);
		},
		methods: {
			locatorButtonPressed() {
				if (navigator.geolocation) {
					navigator.geolocation.getCurrentPosition(position => {
							this.getAddressFrom(position.coords.latitude, position.coords.longitude)

						},
						error => {
							console.log(error.message);
						}
					);

				} else {
					console.log('your browser does not support geolocation')
				}
			},
			getAddressFrom(lat, long) {
				axios.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat + "," + long +
						"&key=AIzaSyC9SSiHS7Va-YfYv3RojyCeVva48AHKSqQ").then(response => {
						if (response.data.error_message) {
							console.log(response.data.error_message);
						} else {
							this.address = response.data.results[0].formatted_address
							// console.log(response.data.results[0].formatted_address);

						}

					})
					.catch(error => {
						console.log(error.message);
					})

			}
		}
	}
</script>

<!-- <template>
  <div id="app">
    <h2>Routes Google Maps</h2>
    <div>
      <table>
        <tr>
          <th>Start Location</th>
          <th><GmapAutocomplete @place_changed="setPlace" /></th>
          <th style="width: 50%;"><button class="btn" @click="addMarker(0)">Add</button></th>
        </tr>
        <tr>
          <th>End Location</th>
          <th><GmapAutocomplete @place_changed="setPlace" /></th>
          <th style="width: 50%;"><button class="btn" @click="addMarker(1)">Add</button></th>
        </tr>
      </table>
    </div>
    <br />
    <GmapMap :zoom="7" :center="center" style="width: 100%; height: 400px">
      <DirectionsRenderer
        travelMode="DRIVING"
        :origin="startLocation"
        :destination="endLocation"
      />
    </GmapMap>
  </div>
</template>
<script>
import DirectionsRenderer from "@/components/DirectionsRenderer";
export default {
  name: "App",
  components: {
    DirectionsRenderer,
  },
  data() {
    return {
      center: { lat: 45.508, lng: -73.587 },
      currentPlace: null,
      markers: [],
      places: [],
      startLocation: null,
      endLocation: null,
    };
  },
  methods: {
    setPlace(place) {
      this.currentPlace = place;
    },
    addMarker(index) {
      const marker = {
        lat: this.currentPlace.geometry.location.lat(),
        lng: this.currentPlace.geometry.location.lng(),
      };
      if (index === 0) this.startLocation = marker;
      if (index === 1) this.endLocation = marker;
      this.center = marker;
    },
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.pac-target-input {
  padding: 10px;
  width: 100%;
}
.btn {
  margin-left: 20px;
  padding: 10px 20px;
  background-color: greenyellow;
}
</style>  -->
