 <template>
     <div id="route">
        <el-input v-model="input" placeholder="Select Route" clearable />
        <MapDisplay />
     </div>
 </template>
 
 <script lang="ts">
import MapDisplay from '../components/MapDisplay.vue'
import { ref } from 'vue'
const input = ref('')
 export default{
    components:{
        MapDisplay,
    },
    data() {
		return {
            input,
			}
		},
 }
 </script>
 
 
 <style>
 </style>