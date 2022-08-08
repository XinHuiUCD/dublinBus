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
