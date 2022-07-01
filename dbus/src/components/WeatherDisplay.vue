<template>
  <!--
    <div id="Weather" style="height: 700px;">
        <div class="demo-collapse">
            <el-collapse v-model="activeName" accordion>
                <el-collapse-item title="&nbsp; Current Weather" name="1">
                    <div style="font-weight: bold;  font-family: 'Actor';font-size: 16px; text-align:center; ">

                        <p>Current Date & Time: {{currentDateTime()}}</p>
                        <div v-if="result">
                            <img src="http://openweathermap.org/img/w/10d.png" style="width: 100px;"> 

                             <div><p>Temp: {{result.main.temp}}°<span>C</span></p></div> 
                                <div><p>Feels Like: {{result.main.feels_like}}°<span>C</span></p></div> 
                                <div>{{result.weather[0].description}}</div>     
                        </div>



                        
                    </div> 
                </el-collapse-item>
                <el-collapse-item title="&nbsp; Today's Weather" name="2">
                    <div>
                        <img src="https://z4a.net/images/2022/06/23/rain.png" style="width: 200px;">
                    </div>
                </el-collapse-item>
                <el-collapse-item title="&nbsp; Future Weather" name="3">
                    <div>
                        <img src="https://z4a.net/images/2022/06/23/sunny.png" style="width: 200px;">
                    </div>
                </el-collapse-item>
            </el-collapse>
        </div>
    </div>
-->
  <div id="Weather" style="height: 700px;">
    <div class="demo-collapse">
      <el-collapse v-model="activeName" accordion>
        <el-collapse-item title="&nbsp; Current Weather" name="1">
          <div style="font-weight: bold;  font-family: 'Actor';font-size: 16px; text-align:center; ">

            <p>Current Date & Time: {{ currentDateTime() }}</p>
            <div v-if="result">
              <img src="http://openweathermap.org/img/w/10d.png" style="width: 100px;">

              <div>
                <p>Temp: {{ result.main.temp }}°<span>C</span></p>
              </div>


              <div>
                <p>Feels Like: {{ result.main.feels_like }}°<span>C</span></p>
              </div>
              <div>{{ result.weather[0].description }}</div>

            </div>

          </div>
        </el-collapse-item>
        <el-collapse-item title="&nbsp; Today's Weather" name="2">
          <div>
            <img src="https://z4a.net/images/2022/06/23/rain.png" style="width: 200px;">
          </div>
        </el-collapse-item>
        <el-collapse-item title="&nbsp; Future Weather" name="3">
          <div>
            <img src="https://z4a.net/images/2022/06/23/sunny.png" style="width: 200px;">
          </div>
        </el-collapse-item>
      </el-collapse>
    </div>
  </div>
</template>

<script lang="ts">
/*
import { ref } from 'vue';
import { useStore } from 'vuex';

export default {
  name: "WeatherDisplay",
  setup() {
    let temps = ref([]);
    let tempsLen = ref('');
    const store = useStore();

    const getWeather = () => {
      store.dispatch("getWeather");
      temps.value = store.state.weather.temps;
      tempsLen.value = store.state.weather.tempsLen;
    };

    return {
      temps,
      tempsLen,
      getWeather,
    };
  }
};*/

/* eslint-disable */


import { ref } from 'vue'

const activeName = ref('1');

var weather = {};

export default ({
  name: "WeatherData",

  setup() {
    const result = ref(null)

    fetch('https://api.openweathermap.org/data/2.5/weather?q=Ireland&units=metric&appid=17f166d4fd4137881f3c09b22dd04a7a')
      .then(response => response.json())
      .then(data => result.value = data)
      .then((result) => {
        result.main
        weather = result.main.temp;

        console.log("helllooooo", result.weather[0].description)
        console.log("icon init", result.weather[0].icon);
      })


    return { result }


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
</script>


<style scoped>
</style>


