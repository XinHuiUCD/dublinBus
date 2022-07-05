<template>
   <div style="align-items: center;">
    <GMapMap
      :center="center"
      :zoom="15"
      map-type-id="terrain"
      style="width: 100%; height: 700px;"
      >

<div style="padding-top: 10px; margin: auto; text-align: center; align-items: center;" >
<button type="button" @click="hideAllMarkers()" class="btn btn-outline-info">Hide/Show Makers</button>
</div>



    <template v-for="marker in Hellodata " :key="marker.stop_id">

     

  <GMapMarker 
    :position="{ lat: marker.stop_lat, lng: marker.stop_lon}"
    :visible="marker.visibility"
    :title="marker.stop_name"
    :clickable="true"
    :icon="'https://img.icons8.com/fluency/48/000000/bus.png'"
    @click="openMarker(marker.stop_id)"

    >
    <GMapInfoWindow
            :closeclick="true"
          @closeclick="openMarker(null)"
          :opened="openedMarkerID === marker.stop_id"
            
          >

           <div style="text-align: center;">
              <h5>Real Time Information</h5>
              <div>Stop Name: {{ marker.stop_name }} </div>
              <table style=" margin: 0 auto;">
                    <tr>
                      <th>Bus Route</th>
                      <th>Arrival</th>
                    </tr>
                    <tr>
                      <td>145</td>
                      <td>6 mins</td>
                    </tr>
                    <tr>
                      <td>46a</td>
                      <td>12 mins</td>
                    </tr>
              </table>
            </div>
            
      </GMapInfoWindow>

    </GMapMarker>

        <!-- </MarkerCluster> -->
    </template>
    <!-- <directionsRenderer
        travelMode="DRIVING"
        :origin="startLocation"
        :destination="endLocation"
      /> -->
    
  </GMapMap>

  </div>
       
</template>



<script>


var clicked = true;

// import DirectionsRenderer from "@/components/DirectionsRenderer";

import markerLocations from "./json/BusStopsLongLatCSV.json"

           
export default{
  // components: {
  //       DirectionsRenderer,
  // },

  name: "DrawGoogleMap",
  data() {
    return {
      center: { 
          lat: 53.3498, 
          lng: -6.2603
      },
      currentLocation: null,
      Hellodata: markerLocations,
      openedMarkerID: null,
      currentPlace: null,
      markers: [],
      places: [],
      startLocation: null,
      endLocation: null,


      infoWindow: {
          position: {lat: 0, lng: 0},
          open: false,
          template: ''
        }

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
}, 
openMarker(id) {
       this.openedMarkerID = id
    }, 

setPlace2(place) {
      this.currentPlace = place;
    },
    addMarker(index) {
      const marker = {
        lat: this.currentPlace.geometry.location.lat(),
        lng: this.currentPlace.geometry.location.lng(),
      };
      if (index === 0) this.startLocation = marker;
      if (index === 1) this.endLocation = marker;
      this.center = marker;
    },
  



    
     

  }
  
};  

</script>

<style scoped>
</style>