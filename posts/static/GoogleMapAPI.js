        //Google Map API with Location lat and long
        var map;
        function initMap() {
       var cafe = {lat: 10.448311, lng: -61.444424};
          map = new google.maps.Map(document.getElementById('map'), {
            zoom: 21,
            center: cafe,
            styles: [
              {
                "elementType": "geometry",
                "stylers": [
                  {
                    "color": "#242f3e"
                  }
                ]
              },
              {
                "elementType": "labels.text.fill",
                "stylers": [
                  {
                    "color": "#746855"
                  }
                ]
              },
              {
                "elementType": "labels.text.stroke",
                "stylers": [
                  {
                    "color": "#242f3e"
                  }
                ]
              },
              {
                "featureType": "administrative.locality",
                "elementType": "labels.text.fill",
                "stylers": [
                  {
                    "color": "#d59563"
                  }
                ]
              },
              {
                "featureType": "poi",
                "elementType": "labels.text.fill",
                "stylers": [
                  {
                    "color": "#d59563"
                  }
                ]
              },
              {
                "featureType": "poi.park",
                "elementType": "geometry",
                "stylers": [
                  {
                    "color": "#263c3f"
                  }
                ]
              },
              {
                "featureType": "poi.park",
                "elementType": "labels.text.fill",
                "stylers": [
                  {
                    "color": "#6b9a76"
                  }
                ]
              },
              {
                "featureType": "road",
                "elementType": "geometry",
                "stylers": [
                  {
                    "color": "#38414e"
                  }
                ]
              },
              {
                "featureType": "road",
                "elementType": "geometry.stroke",
                "stylers": [
                  {
                    "color": "#212a37"
                  }
                ]
              },
              {
                "featureType": "road",
                "elementType": "labels.text.fill",
                "stylers": [
                  {
                    "color": "#9ca5b3"
                  }
                ]
              },
              {
                "featureType": "road.highway",
                "elementType": "geometry",
                "stylers": [
                  {
                    "color": "#746855"
                  }
                ]
              },
              {
                "featureType": "road.highway",
                "elementType": "geometry.stroke",
                "stylers": [
                  {
                    "color": "#1f2835"
                  }
                ]
              },
              {
                "featureType": "road.highway",
                "elementType": "labels.text.fill",
                "stylers": [
                  {
                    "color": "#f3d19c"
                  }
                ]
              },
              {
                "featureType": "transit",
                "elementType": "geometry",
                "stylers": [
                  {
                    "color": "#2f3948"
                  }
                ]
              },
              {
                "featureType": "transit.station",
                "elementType": "labels.text.fill",
                "stylers": [
                  {
                    "color": "#d59563"
                  }
                ]
              },
              {
                "featureType": "water",
                "elementType": "geometry",
                "stylers": [
                  {
                    "color": "#17263c"
                  }
                ]
              },
              {
                "featureType": "water",
                "elementType": "labels.text.fill",
                "stylers": [
                  {
                    "color": "#515c6d"
                  }
                ]
              },
              {
                "featureType": "water",
                "elementType": "labels.text.stroke",
                "stylers": [
                  {
                    "color": "#17263c"
                  }
                ]
              }
            ]
          });
        //   var icon = {
        //     url: "image path", // url
        //     scaledSize: new google.maps.Size(50, 50), // size
        // };
        // //Maker for the Google Map 
        // var marker = new google.maps.Marker({
        //     position: cafe,
        //     icon: icon,
        //     map: map,
        //     title:'Amanti Del Caffe'
        // });
    var icon = {
          url: "image path", // url
          scaledSize: new google.maps.Size(50, 50), // size
      };
  
   marker = new google.maps.Marker({
    position: cafe,
    map: map,
    icon: icon
   });
    }