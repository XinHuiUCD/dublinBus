<template>
   
    <GMapMap
      :center="center"
      :zoom="15"
      map-type-id="terrain"
      style="width: 100%; height: 700px"
      >

<div style="padding-top: 10px;">
<button type="button" @click="hideAllMarkers()" class="btn btn-outline-info">Hide/Show Makers</button>
</div>



    <template v-for="marker in Hellodata " :key="marker.stop_id">

     

  <GMapMarker 
    :position="{ lat: marker.stop_lat, lng: marker.stop_lon}"
    :visible="marker.visibility"
    :title="marker.stop_name"
    :clickable="true"
    />

        <!-- </MarkerCluster> -->
    </template>
    
  </GMapMap>

  
       
</template>



<script>


var clicked = true;


import markerLocations from "./json/BusStopsLongLatCSV.json"

           
export default{

  name: "DrawGoogleMap",
  data() {
    return {
      center: { 
          lat: 39.7837304, 
          lng: -100.4458825 
      },
      currentLocation: null,
      Hellodata: markerLocations,

    };
  },
 
  mounted() {
    this.setLocationLatLng();
  },
 
  methods: {
    setPlace(loc) {
      this.currentLocation = loc;
    },
    setLocationLatLng: function() {
        navigator.geolocation.getCurrentPosition(geolocation => {
          this.center = {
            lat: geolocation.coords.latitude,
            lng: geolocation.coords.longitude
          };
        });
        
        
    }, 
    hideAllMarkers() {
        if (clicked) {
            for(let i=0;i<this.Hellodata.length;i++){
    

            this.Hellodata[i]["visibility"] = false;
    
            }
             clicked = false;

        }else {
            for(let i=0;i<this.Hellodata.length;i++){
    

            this.Hellodata[i]["visibility"] = true;
    
        }
            clicked = true;


}
}


    
     

  }
  
};  

</script>

<style scoped>
</style>