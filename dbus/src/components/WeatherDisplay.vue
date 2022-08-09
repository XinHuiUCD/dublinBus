<template>
	<div id="Weather">
		<h2 style="text-align:center">
            <span style="color: black">Up to date</span>&nbsp;
            <span style="color: gray">Weather Information</span>
        </h2>
		<div class="demo-collapse">
			<el-collapse v-model="activeName" accordion>
				<el-collapse-item title="&nbsp; Current Weather" name="1">
					<div
						style=" font-size: 16px; text-align:center;box-shadow: 3px 3px 3px;   border-radius: 5px;border:1px solid #999999; color:#6f6f6f; ">
						<p style=" font-size:16px; position: relative; display: inline-block; height: auto;">
							<span style="color: gray;">Date & Time:</span>  {{ currentDateTime() }}</p>
						<div v-if="result">
							<img v-bind:src="'http://openweathermap.org/img/w/' + result.list[0].weather[0].icon + '.png'" style="width: 80px; height: 80px;">
							<div>
								<p><span style="color: gray;">Temp:</span>  {{ (result.list[0].main.temp - 273.15).toFixed(2) }}°<span>C</span></p>

							</div>
							<div>
								<p><span style="color: gray;">Feels Like:</span> 
									{{ (result.list[0].main.feels_like - 273.15).toFixed(2) }}°<span>C</span>
								</p>
							</div>
							<div><p><span style="color: gray;">Description:</span> {{ result.list[0].weather[0].description }}</p></div>
						</div>
					</div>
				</el-collapse-item>
				<el-collapse-item title="&nbsp; Tomorrow's Weather " name="2">
					<div
						style="font-size: 16px; text-align:center;box-shadow: 3px 3px 3px;   border-radius: 5px;border:1px solid #999999; color:#6f6f6f; ">


						<div v-if="result">
							<img v-bind:src="'http://openweathermap.org/img/w/' + result.list[8].weather[0].icon + '.png'" style="width: 80px; height: 80px;">
							<div>
								<p><span style="color: gray;">Temp:</span>  {{ (result.list[8].main.temp - 273.15).toFixed(2) }}°<span>C</span></p>

							</div>
							<div>
								<p><span style="color: gray;">Feels Like:</span> 
									{{ (result.list[8].main.feels_like - 273.15).toFixed(2) }}°<span>C</span>
								</p>
							</div>
							<div><p><span style="color: gray;">Description:</span> {{ result.list[8].weather[0].description }}</p></div>
						</div>


					</div>
				</el-collapse-item>
				<el-collapse-item title="&nbsp; Future Weather" name="3">
					<div style="font-size: 16px; text-align:center;box-shadow: 3px 3px 3px;   border-radius: 5px;border:1px solid #999999; color:#6f6f6f; ">
						<div v-if="result" style="display: inline-block; padding-right: 5px; border: 1px solid black; border-radius: 5px;">
							<img v-bind:src="'http://openweathermap.org/img/w/' + result.list[16].weather[0].icon + '.png'" style="width: 80px; height: 80px;">
							<div>
								<p><span style="color: gray;">Date: </span>{{ (result.list[16].dt_txt).slice(0,10) }}</p>
							</div>
							<div>
								<p><span style="color: gray;">Temp:</span>  {{ (result.list[16].main.temp - 273.15).toFixed(2) }}°<span>C</span></p>

							</div>
							<div>
								<p><span style="color: gray;">Feels Like:</span> 
									{{ (result.list[16].main.feels_like - 273.15).toFixed(2) }}°<span>C</span>
								</p>
							</div>
							<div><p><span style="color: gray;">Description: </span> {{ result.list[16].weather[0].description }}</p></div>
						</div>
						<div v-if="result" style="display: inline-block; padding-left: 5px; border: 1px solid black; border-radius: 5px;">
							<img v-bind:src="'http://openweathermap.org/img/w/' + result.list[22].weather[0].icon + '.png'" style="width: 80px; height: 80px;">
							<div>
								<p><span style="color: gray;">Date: </span>{{ (result.list[22].dt_txt).slice(0,10) }}</p>
							</div>
							<div>
								<p><span style="color: gray;">Temp:</span>  {{ (result.list[22].main.temp - 273.15).toFixed(2) }}°<span>C</span></p>

							</div>
							<div>
								<p><span style="color: gray;">Feels Like:</span> 
									{{ (result.list[22].main.feels_like - 273.15).toFixed(2) }}°<span>C</span>
								</p>
							</div>
							<div><p><span style="color: gray;">Description: </span> {{ result.list[22].weather[0].description }}</p></div>
						</div>
						<div v-if="result" style="display: inline-block; padding-left: 5px; border: 1px solid black; border-radius: 5px;">
							<img v-bind:src="'http://openweathermap.org/img/w/' + result.list[32].weather[0].icon + '.png'" style="width: 80px; height: 80px;">
							<div>
								<p><span style="color: gray;">Date: </span>{{ (result.list[32].dt_txt).slice(0,10) }}</p>
							</div>
							<div>
								<p><span style="color: gray;">Temp:</span>  {{ (result.list[32].main.temp - 273.15).toFixed(2) }}°<span>C</span></p>

							</div>
							<div>
								<p><span style="color: gray;">Feels Like:</span> 
									{{ (result.list[32].main.feels_like - 273.15).toFixed(2) }}°<span>C</span>
								</p>
							</div>
							<div><p><span style="color: gray;">Description: </span> {{ result.list[32].weather[0].description }}</p></div>
						</div>
					</div>
				</el-collapse-item>
			</el-collapse>
		</div>
	</div>
</template>

<script lang="ts">
/* eslint-disable */


import {
	ref
} from 'vue'

const activeName = ref('1');

var weather = {};

export default ({
	name: "WeatherData",
	data() {
		return {
			currentWeather: null,
			activeName

		}
	},

	setup() {
		const result = ref(null)



		fetch(
			'https://api.openweathermap.org/data/2.5/weather?q=Ireland&units=metric&appid=17f166d4fd4137881f3c09b22dd04a7a'
		)
			.then(response => response.json()),
			fetch(
				'https://api.openweathermap.org/data/2.5/forecast?lat=53.3498&lon=-6.2603&appid=17f166d4fd4137881f3c09b22dd04a7a'
			)
				.then(response => response.json())
				.then(data => result.value = data)
				.then((result) => {
					
				})


		return {
			result
		}




	},
	methods: {
		currentDateTime() {
			const current = new Date();
			const date = current.getFullYear() + '-' + (current.getMonth() + 1) + '-' + current.getDate();
			const time = current.getHours() + ":" + current.getMinutes() + ":" + current.getSeconds();
			const dateTime = date + ' ' + time;

			return dateTime;
		}
	}


});

	// https://api.openweathermap.org/data/2.5/forecast?lat=53.3498&lon=6.2603&appid=17f166d4fd4137881f3c09b22dd04a7a
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
p {
	font-family: 'Roboto', sans-serif;
}
  

h2{
  font-family: 'Roboto', sans-serif;

}

</style>
