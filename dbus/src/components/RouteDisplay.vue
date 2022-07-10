 <template>
    <div id="route">
        <el-autocomplete class="inline-input" v-model="select_route" :fetch-suggestions="querySearch" placeholder="Select Route"
            :trigger-on-focus="false" @select="handleSelect" clearable style="width:100%;"></el-autocomplete>
        <MapDisplay />
    </div>
</template>
 
 <script lang="ts" setup>
import MapDisplay from '@/components/MapDisplay.vue'
import { ref, onMounted } from 'vue'

// need to connect database or import json to get bus id, 
// stop id, stop lat and stop lon to show the position and direction

interface RoutetItem {
    value: string
}
const select_route = ref('')

const restaurants = ref<RoutetItem[]>([])
// eslint-disable-next-line
const querySearch = (queryString: string, cb: any) => {
    const results = queryString
        ? restaurants.value.filter(createFilter(queryString))
        : restaurants.value
    // call callback function to return suggestions
    cb(results)
}
const createFilter = (queryString: string) => {
    return (restaurant: RoutetItem) => {
        return (
            restaurant.value.toLowerCase().indexOf(queryString.toLowerCase()) === 0
        )
    }
}
const loadAll = () => {
    return [
        // autocomplete test
        { value: '1' },
        { value: '4' },
        { value: '6' },
        { value: '7' },
        { value: '7A' },
        { value: '7B' },
        { value: '7D' },
        { value: '7N' },
        { value: '9' },
        { value: '11' },
        { value: '13' },
        { value: '14' },
        { value: '15' },
        { value: '15A' },
        { value: '15B' },
        { value: '15D' },
        { value: '16' },
        { value: '25N' },
        { value: '26' },
        { value: '27' },
        { value: '27A' },
        { value: '27B' },
        { value: '27X' },
        { value: '29N' },
        { value: '31N' },
        { value: '32X' },
        { value: '33' },
        { value: '33D' },
        { value: '33N' },
        { value: '33X' },
        { value: '37' },
        { value: '38' },
        { value: '38A' },
        { value: '38B' },
        { value: '39' },
        { value: '39A' },
        { value: '39X' },
        { value: '40' },
        { value: '40B' },
        { value: '40D' },
        { value: '40E' },
        { value: '41' },
        { value: '41B' },
        { value: '41C' },
        { value: '42' },
        { value: '41D' },
        { value: '42D' },
        { value: '42N' },
        { value: '41X' },
        { value: '43' },
        { value: '44' },
        { value: '44B' },
        { value: '46A' },
        { value: '46E' },
        { value: '46N' },
        { value: '47' },
        { value: '49' },
        { value: '49N' },
        { value: '51N' },
        { value: '51X' },
        { value: '52' },
        { value: '53A' },
        { value: '69A' },
        { value: '70' },
        { value: '145' },
        { value: '155' },
        
    ]
}

const handleSelect = (item: RoutetItem) => {
    console.log(item)
}

onMounted(() => {
    restaurants.value = loadAll()
})

</script>
 
 
 <style>
 </style>
