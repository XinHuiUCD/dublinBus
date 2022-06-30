console.log("hellloooxcxcoooccooo")

var markerCluster;




// Testing -----------------------------------------------




var markers = [];
// intialise the map function
function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: new google.maps.LatLng(53.350140, -6.266155),
        zoom: 14,
    });
    
   
// pop up window variable
    infoWindow = new google.maps.InfoWindow();

// code to get current location
  const locationButton = document.createElement("button");



  locationButton.textContent = "Current Location";
  locationButton.classList.add("custom-map-control-button");
  map.controls[google.maps.ControlPosition.LEFT_CENTER].push(locationButton);
  locationButton.addEventListener("click", () => {
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {

            lat: position.coords.latitude,
            lng: position.coords.longitude,
        
          };
          console.log("this is your position", pos)
          infoWindow.setPosition(pos);
          infoWindow.setContent("You are here!");
          infoWindow.open(map);
          map.setCenter(pos);
        },
        () => {
          handleLocationError(true, infoWindow, map.getCenter());
        }
      );
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
      
    }
  });


  const markerCluster = new markerClusterer.MarkerClusterer({ map, markers });

    $.getJSON("./static/BusStopsLongLatCSV.json", function (stops){
      console.log(stops[0].stop_lat);
       
        for (let i = 0; i < stops.length; i++){
          
          
          var color = 'red';
          var infoBox = stops[i].stop_name;    

          // console.log(stops[i].stop_name)
            // console.log('station', station);
            circle = new google.maps.Circle({
                strokeColor: color,
                strokeOpacity: '0.8',
                strokeWeight: 0,
                fillColor: color,
                fillOpacity: 0.55,
                map,
                radius: 20,
                clickable: true,
                center: {
                    lat: stops[i].stop_lat,
                    lng: stops[i].stop_lon
                },

                
            })

            makeClickable(map, circle, infoBox);

        
          }

          
        })        

       

}

// new MarkerClusterer({ map, circle });






function makeClickable(map, circle, info) {
  console.log('In the make clickable')
    var infowindow = new google.maps.InfoWindow({
        content: info
    });

    google.maps.event.addListener(circle, 'click', function (ev) {
        infowindow.setPosition(circle.getCenter());
        infowindow.open(map);
    });
}




$('#datetime').datetimepicker({
  format: 'hh:mm:ss a'
});


function openNav() {
  document.getElementById("mySidepanel").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidepanel").style.width = "0";
}