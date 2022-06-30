<template>
	<div id="Menu" style="height: 700px;">
		<div id="title">
			<h1>
				<span style="color: black">Plan Your Journery</span>&nbsp;
				<span style="color: gray">With DublinBus</span>
			</h1>
			<div id="function">
				<!-- Your Position -->
				<div class="input-group mb-3">
					<button class="btn btn-outline-secondary" type="button" id="button-addon1" @click="locatorButtonPressed">🔍</button>
					<input type="text" class="form-control" placeholder="Your Position" v-model="address"
                id="autocomplete"
                ref="autocomplete"
						aria-label="Example text with button addon" aria-describedby="button-addon1" show-clear>
				</div>


				<!-- Your Destination -->
				<div class="input-group mb-3">
					<button class="btn btn-outline-secondary" type="button" id="button-addon2">🔍</button>
					<input type="text" class="form-control" placeholder="Your Destination"
						>
				</div>


				<!-- Select date and time -->
				<div class="block">
					<el-date-picker v-model="date" type="datetime" placeholder="Pick a Date"
						format="YYYY/MM/DD hh:mm:ss" value-format="YYYY-MM-DD h:m:s a"
						style="height: 40px; " />
				</div>
				<div style="height: 300px; margin-top: 20px;">
					<el-steps direction="vertical" :active="1">
						<el-step title="Start" description="39A" />
						<el-step title="Futher Info" description="" />
						<el-step title="End" />
					</el-steps>
				</div>
			</div>
		</div>
	</div>

</template>

<script>
    
import axios from 'axios'


export default{
    data() {
        return {
            address: ""
        }
    },

    mounted() {
        // eslint-disable-next-line
        var autocomplete = new google.maps.places.Autocomplete(
      this.$refs["autocomplete"],
      {
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
            if(navigator.geolocation){
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
        getAddressFrom(lat, long){
            axios.get("https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat + "," + long + "&key=AIzaSyC9SSiHS7Va-YfYv3RojyCeVva48AHKSqQ").then(response => {
                if(response.data.error_message){
                    console.log(response.data.error_message);
                } else {
                    this.address = response.data.results[0].formatted_address
                    // console.log(response.data.results[0].formatted_address);

                }

            })
            .catch(error => {
                console.log(error.message);
            });

        }
    },
    showUserLocationOnTheMap(latitude, longitude){
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

    }

};
	/* eslint-disable */
// 	import {
// defineComponent,
// 		ref
// 	} from 'vue'
// 	import {
// 		Calendar,
// 		Search
// 	} from '@element-plus/icons-vue'

// 	const ur_position = ref('')
// 	const ur_destination = ref('')
// 	const date = ref('')




</script>

<style scoped>
	.enter {
		width: 80%;
		height: 40px;
		border-radius: 8px;
		margin-top: 20px;
	}
	::-ms-clear {
	  display: none;
	}
</style>