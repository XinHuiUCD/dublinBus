<!-- <template>
	<div id="Weather" style="width: 20%;height: 750px; float: right; background: whitesmoke; position: relative;">
		<div class="demo-collapse">
			<el-collapse v-model="activeName" accordion>
				<el-collapse-item title="Current Weather" name="1">
					<div>
						<img src="@/assets/imgs/晚上.png" style="width: 200px;">
					</div>
				</el-collapse-item>
				<el-collapse-item title="Today's Weather" name="2">
					<div>
						<img src="@/assets/imgs/太阳.png" style="width: 200px;">
						<img src="@/assets/imgs/有风.png" style="width: 200px;">
						<img src="@/assets/imgs/晚上.png" style="width: 200px;">
					</div>
				</el-collapse-item>
				<el-collapse-item title="Future Weather" name="3">
					<div>
						<img src="@/assets/imgs/太阳.png" style="width: 200px;">
					</div>
				</el-collapse-item>
			</el-collapse>
		</div>
	</div>
</template>

<script lang="ts" setup>
	import {
		ref
	} from 'vue'

	const activeName = ref('1');

</script>


<style>
</style> -->


<!-- <template>
	<div id="Weather" style="width: 20%;height: 750px; float: right; background: whitesmoke;">
		<vue-weather api-key="<17f166d4fd4137881f3c09b22dd04a7a>" units="ie" latitude="53.349722" longitude="-6.260278" />
	</div>


</template>

<script>
	import VueWeather from "vue-weather-widget";

	export default {
		components: {
			VueWeather,
		},
	};
</script> -->


<template>

	<div id="app" :class="typeof weather.main != 'undefined' && weather.main.temp > 18 ? 'warm' : ''"
		style="width: 20%;height: 750px; float: right;">

		<main>
			<div class="search-box">
				<input type="text" class="search-bar" placeholder="Search..." v-model="query"
					@keypress="fetchWeather" />
			</div>

			<div class="weather-wrap" v-if="typeof weather.main != 'undefined' ">

				<div class="location-box">
					<div class="location"> {{ weather.name }} , {{ weather.sys.country }}</div>
					<div class="date"> {{ dateBuilder() }}</div>
				</div>
				<div class="weather-box">
					<div class="temp"> {{ Math.round(weather.main.temp)}} °C</div>
					<div class="weather"> {{ weather.weather[0].main}}</div>
				</div>
			</div>
		</main>

	</div>
</template>

<script>
	export default {
		name: 'app',
		data() {
			return {
				api_key: '17f166d4fd4137881f3c09b22dd04a7a',
				url_base: 'https://api.openweathermap.org/data/2.5/',
				query: '',
				weather: {}
			}
		},
		methods: {
			fetchWeather(e) {
				if (e.key == "Enter") {
					fetch(`${this.url_base}weather?q=${this.query}&units=metric&APPID=${this.api_key}`)
						.then(res => {
							return res.json();
						}).then(this.setResults);
				}
			},
			setResults(results) {
				this.weather = results;
			},
			dateBuilder() {
				let d = new Date();
				let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
					"October", "November", "December"
				]
				let days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
				let day = days[d.getDay()];
				let date = d.getDate();
				let month = months[d.getMonth()];
				let year = d.getFullYear();
				return `${day} ${date} ${month} ${year}`;
			}
		}

	}
</script>


<style>
	#app {
		background-image: url('../../../dist/img/太阳.f8f35a34.png');
		background-size: cover;
		background-position: bottom;
		transition: 0.4s;
	}

	#app.warm {
		background-image: url('../../../dist/img/太阳.f8f35a34.png');
	}

	main {
		min-height: 100vh;
		padding: 25px;
		background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.25), rgba(0, 0, 0, 0.75));
	}

	.search-box {
		width: 100%;
		margin-bottom: 30px;
	}

	.search-box .search-bar {
		display: block;
		width: 100%;
		padding: 15px;
		color: #313131;
		font-size: 20px;
		appearance: none;
		border: none;
		outline: none;
		background: none;
		box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.25);
		background-color: rgba(255, 255, 255, 0.5);
		border-radius: 0px 16px 0px 16px;
		transition: 0.4s;
	}

	.search-box .search-bar:focus {
		box-shadow: 0px 0px 16px rgba(0, 0, 0, 0.25);
		background-color: rgba(255, 255, 255, 0.75);
		border-radius: 16px 0px 16px 0px;
	}

	.location-box .location {
		color: #fff;
		font-size: 32px;
		font-weight: 500;
		text-align: center;
		text-shadow: 1px 3px rgba(0, 0, 0, 0.25);
	}

	.location-box .date {
		color: #FFF;
		font-size: 20px;
		font-weight: 400;
		font-style: italic;
		text-align: center;
	}

	.weather-box {
		text-align: center;
	}

	.weather-box .temp {
		display: inline-block;
		padding: 10px 25px;
		color: #FFF;
		font-size: 102px;
		font-weight: 800;
		text-shadow: 3px 6px rgba(0, 0, 0, 0.25);
		background-color: rgba(255, 255, 255, 0.25);
		border-radius: 16px;
		margin: 30px 0px;
		box-shadow: 3px 6px rgba(0, 0, 0, 0.25);
	}

	.weather-box .weather {
		color: #fff;
		font-size: 48px;
		font-weight: 600;
		font-style: italic;
		text-shadow: 3px 6px rgba(0, 0, 0, 0.25);
	}
</style>
