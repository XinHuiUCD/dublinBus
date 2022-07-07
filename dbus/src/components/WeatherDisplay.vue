<!-- <template>
    <div id="Weather" >
        <div class="weather-collapse">
            <el-collapse v-model="activeName" accordion>
                <el-collapse-item title="&nbsp; Current Weather" name="1">
                    <div style="font-weight: bold; font-family: 'Actor';font-size: 16px; text-align:center;box-shadow: 3px 3px 3px; border-radius: 5px;border:1px solid #999999; color:#6f6f6f; ">

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
</template>

<script lang="ts">
/* eslint-disable */


import axios from 'axios'

import { result } from 'lodash';
import { defineComponent } from 'vue'


import {
    ref
} from 'vue'

const activeName = ref('1');

var weather = {};

export default ({
  name: "WeatherData",
  
	setup(){
    const result = ref(null)
    


    fetch('https://api.openweathermap.org/data/2.5/weather?q=Ireland&units=metric&appid=17f166d4fd4137881f3c09b22dd04a7a')
      .then(response => response.json())
      .then(data => result.value = data)
      .then((result) => {
            result.main
            weather = result.main.temp;

			console.log("helllooooo", result.weather[0].description)
            console.log("icon init",result.weather[0].icon);
        })


    return { result }

      
  }, 
   methods: {
    currentDateTime() {
      const current = new Date();
      const date = current.getFullYear()+'-'+(current.getMonth()+1)+'-'+current.getDate();
      const time = current.getHours() + ":" + current.getMinutes() + ":" + current.getSeconds();
      const dateTime = date +' '+ time;

      return dateTime;
    }
  }


});






</script>


<style>

</style>






 -->
 
 <template>
     <div id="Weather">
         <div class="demo-collapse">
             <el-collapse v-model="activeName" accordion>
                 <el-collapse-item title="&nbsp; Current Weather" name="1">
                     <div
                         style="font-weight: bold;  font-family: 'Actor';font-size: 16px; text-align:center;box-shadow: 3px 3px 3px;   border-radius: 5px;border:1px solid #999999; color:#6f6f6f; ">
 
                         <p style=" font-size:16px; position: relative; display: inline-block; height: auto;">Date &
                             Time: {{ currentDateTime() }}</p>
                         <div v-if="result">
                             <img src="http://openweathermap.org/img/w/10d.png" style="width: 100px;">
                             <div>
                                 <p>Temp: {{ (result.list[0].main.temp - 273.15).toFixed(2) }}°<span>C</span></p>
                                 
                             </div>
                             <div>
                                 <p>Feels Like: {{ (result.list[0].main.feels_like - 273.15).toFixed(2) }}°<span>C</span></p>
                             </div>
                             <div>{{ result.list[0].weather[0].description }}</div>
                         </div>
 
 
 
 
                     </div>
                 </el-collapse-item>
                 <el-collapse-item title="&nbsp; Tomorrow's Weather " name="2">
                     <div
                         style="font-weight: bold;  font-family: 'Actor';font-size: 16px; text-align:center;box-shadow: 3px 3px 3px;   border-radius: 5px;border:1px solid #999999; color:#6f6f6f; ">
 
                         
                         <div v-if="result">
                             <img src="http://openweathermap.org/img/w/04d.png" style="width: 100px;">
                             <div>
                                 <p>Current date {{result.list[10].dt_txt}}</p>
                             </div>
                             <div>
                                 <p>Temp: {{ (result.list[10].main.temp - 273.15).toFixed(2) }}°<span>C</span></p>
                                 
                             </div>
                             <div>
                                 <p>Feels Like: {{ (result.list[10].main.feels_like - 273.15).toFixed(2) }}°<span>C</span></p>
                             </div>
                             <div>{{ result.list[10].weather[0].description }}</div>
                         </div>
 
 
 
 
                     </div>
                 </el-collapse-item>
                 <el-collapse-item title="&nbsp; Future Weather" name="3">
                     <div
                         style="font-weight: bold;  font-family: 'Actor';font-size: 16px; text-align:center;box-shadow: 3px 3px 3px;   border-radius: 5px;border:1px solid #999999; color:#6f6f6f; ">
                     <div v-if="result">
                             <img src="http://openweathermap.org/img/w/04n.png" style="width: 100px;">
                             <div>
                                 <p>Current date {{result.list[20].dt_txt}}</p>
                             </div>
                             <div>
                                 <p>Temp: {{ (result.list[20].main.temp - 273.15).toFixed(2) }}°<span>C</span></p>
                                 
                             </div>
                             <div>
                                 <p>Feels Like: {{ (result.list[20].main.feels_like - 273.15).toFixed(2) }}°<span>C</span></p>
                             </div>
                             <div>{{ result.list[20].weather[0].description }}</div>
                         </div>
                     </div>  
                 </el-collapse-item>
             </el-collapse>
         </div>
     </div>
 </template>
 
 <script lang="ts">
 /* eslint-disable */
 
 
 import axios from 'axios'
 
 import { result } from 'lodash';
 import { defineComponent } from 'vue'
 
 
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
             
         }
     },
 
     setup() {
         const result = ref(null)
 
 
 
         fetch('https://api.openweathermap.org/data/2.5/weather?q=Ireland&units=metric&appid=17f166d4fd4137881f3c09b22dd04a7a').then(response => response.json()),
         fetch('https://api.openweathermap.org/data/2.5/forecast?lat=53.3498&lon=-6.2603&appid=17f166d4fd4137881f3c09b22dd04a7a')
             .then(response => response.json())
             .then(data => result.value = data)
             .then((result) => {
                 console.log("lfg", result)
                 // result.main
                 // weather = result.main.temp;
 
                 // console.log("helllooooo", result.weather[0].description)
                 // console.log("icon init", result.weather[0].icon);
             })
 
 
         // return { result }
 
         // Promise.all([
         //         fetch('https://api.openweathermap.org/data/2.5/weather?q=Ireland&units=metric&appid=17f166d4fd4137881f3c09b22dd04a7a').then(res => res.ok && res.json() || Promise.reject(res)),
         //         fetch('https://api.openweathermap.org/data/2.5/forecast?lat=53.3498&lon=6.2603&appid=17f166d4fd4137881f3c09b22dd04a7a').then(res => res.ok && res.json() || Promise.reject(res))
         // ]).then(result => {
         //     console.log("temparature", result[0].main.temp)
 
         // })
 
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
 
 // https://api.openweathermap.org/data/2.5/forecast?lat=53.3498&lon=6.2603&appid=17f166d4fd4137881f3c09b22dd04a7a
 
 
 
 
 </script>
 
 
 <style>
 </style>
 
 
 
 
 
