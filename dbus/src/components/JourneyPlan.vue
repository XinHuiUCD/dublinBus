<template>
	<div id="Menu">
		<div id="title">
			<h1>
				<span style="color: black">Plan Your Journey</span>&nbsp;
				<span style="color: gray">With DublinBus</span>
			</h1>

			<div id="function">

				<!-- Your Position -->
				<div class="input-group mb-3">
					<button class="btn btn-outline-secondary" type="button" id="button-addon1"
						@click="locatorButtonPressed">🔍</button>
					<input type="text" class="form-control" placeholder="Your Position" v-model="address"
						id="AIzaSyCrhyaaRpjY62Rs5XiT91Vfwv50ySu-FNo" ref="autocomplete"
						aria-label="Example text with button addon" aria-describedby="button-addon1" show-clear>
				</div>


				<!-- Your Destination -->
				<div class="input-group mb-3">
					<button class="btn btn-outline-secondary" type="button" id="button-addon2"
						@click="locatorButtonPressedTwo">🔍</button>

					<input type="text" class="form-control" placeholder="Your Destination" v-model="addresstwo"
						ref="autocomplete2">

				</div>

				<!-- Select date and time -->
				<div class="block">
					<el-date-picker v-model="pickdate" type="datetime" placeholder="Select date and time"
						style="height: 40px; width: 100%;" />
				</div>

				<!-- swap address -->
				<button class="btn btn-outline-secondary" type="submit" @click="swapAddress(address,addresstwo)"
					style="margin-top: 10px; width: 60px;height: 60px;">↕️<br />Swap</button>

				<!-- fare calculator -->
				<button class="btn btn-outline-secondary" type="submit"
					style="margin-top: 10px;margin-left: 20px;width: 60px;height: 60px;">€️<br />Fare</button>

				<!-- submit -->
				<!-- Gus route planner Add button -->
				<button class="btn btn-outline-secondary" type="submit"
					style="margin-top: 10px;margin-left: 20px;width: 70px;height: 60px;background-color: chartreuse;">Submit️</button>

				<!-- schedule -->
				<!-- <div style="height: 300px; margin-top: 20px;">
					<el-steps direction="vertical" :active="1">
						<el-step title="Start" description="39A" />
						<el-step title="Futher Info" description="" />
						<el-step title="End" />
					</el-steps>
				</div> -->
				<!-- favorite bus stop maybe -->
			</div>
		</div>
	</div>

</template>

<script>
	import axios from 'axios'
	// import VueGoogleAutocomplete from "vue-google-autocomplete"
	import {
		ref
	} from 'vue'
	
	const pickdate = ref('')

	export default {

		data() {
			return {
				pickdate,
				address: "",
				addresstwo: ""
			}
			// this.address = this.addresstwo
		},

		mounted() {
			// eslint-disable-next-line
			const autocomplete = new google.maps.places.Autocomplete(
				this.$refs["autocomplete"], {
					// eslint-disable-next-line
					bounds: new google.maps.LatLngBounds(
						// eslint-disable-next-line
						new google.maps.LatLng(53.3498, -6.2603)
					),

				}

			);

			autocomplete.addListener("place_changed", () => {
				this.address=autocomplete.getPlace().formatted_address;
				console.log(autocomplete.getPlace());
			});

			// eslint-disable-next-line
			const autocomplete2 = new google.maps.places.Autocomplete(
				this.$refs["autocomplete2"], {
					// eslint-disable-next-line
					bounds: new google.maps.LatLngBounds(
						// eslint-disable-next-line
						new google.maps.LatLng(53.3498, -6.2603)
					),

				}

			);
			autocomplete2.addListener("place_changed", () => {
				this.addresstwo=autocomplete2.getPlace().formatted_address;
				console.log(autocomplete2.getPlace());
			});
		},
		
		methods: {
			togglefav: function() {
				this.$emit('togglefav', !this.is_fav);
			},

			swapAddress() {
				const tempAddress = this.address;
				this.address = this.addresstwo;
				this.addresstwo = tempAddress;
			},

			locatorButtonPressed() {
				if (navigator.geolocation) {
					navigator.geolocation.getCurrentPosition(position => {
							this.getAddressFrom(position.coords.latitude, position.coords.longitude);

							this.showUserLocationOnTheMap(
								position.coords.latitude, position.coords.longitude
							);

						},
						error => {
							console.log(error.message);
						}
					);

				} else {
					console.log('your browser does not support geolocation')
				}
			},
			locatorButtonPressedTwo() {
				if (navigator.geolocation) {
					navigator.geolocation.getCurrentPosition(position => {
							this.getAddressFromTwo(position.coords.latitude, position.coords.longitude);

							this.showUserLocationOnTheMap(
								position.coords.latitude, position.coords.longitude
							);

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
					});

			},
			getAddressFromTwo(lat, long) {
				axios.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat + "," + long +
						"&key=AIzaSyC9SSiHS7Va-YfYv3RojyCeVva48AHKSqQ").then(response => {
						if (response.data.error_message) {
							console.log(response.data.error_message);
						} else {
							this.addresstwo = response.data.results[0].formatted_address
							// console.log(response.data.results[0].formatted_address);

						}

					})
					.catch(error => {
						console.log(error.message);
					});

			}
		},
		showUserLocationOnTheMap(latitude, longitude) {
			// eslint-disable-next-line
			let map = new google.maps.Map(document.getElementById("map"), {
				zoom: 15,
				// eslint-disable-next-line
				center: new google.maps.LatLng(latitude, longitude),
				// eslint-disable-next-line
				mapTypeId: google.maps.MapTypeID.ROADMAP
			});
			// eslint-disable-next-line
			new google.maps.Marker({
				// eslint-disable-next-line
				position: new google.maps.LatLng(latitude, longitude),
				map: map,
			});

		},



	};
</script>

<style scoped>

</style>
