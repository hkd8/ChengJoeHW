// Setting the link for the dataset we are grabbing from
var link = "https://gbfs.citibikenyc.com/gbfs/en/station_information.json?";
var link2 = "https://gbfs.citibikenyc.com/gbfs/en/station_status.json";

// Setting the base Map variable
var myMap = L.map("map-id", {
  center: [40.73, -74.0059],
  zoom: 12
});

//Creating the function where we nest our code
function createMap(link)  {

  // Create the tile layer that will be the background of our map
  var base = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
  }).addTo(myMap);

  // Create a baseMaps object to hold the lightmap layer
  var light = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
   maxZoom: 18,
   id: "mapbox.light",
   accessToken: API_KEY
 });

  var baseMaps = {
   "Light": light,
   "Base": base
 };

 //Adding the control layer to myMap
 L.control.layers(baseMaps).addTo(myMap);}

// Create the createMarkers function
function createMarkers(link)  {

  // Pulling the data from the link
  d3.json(link, function(data) {
   
  //Here we are setting variable for markers
  //We set the markers variable here because we needed to slice the amount of data we are gathering using the SLICE function
    var markers = data.data.stations
    limit = 100
    markers = markers.slice(0, limit)
    
  //Here is our for loop. NOTE that we are using our new variable MARKERS, due to prior slicing
  //NOTE we are binding our popup data within our FOR loop. 
    markers.forEach(d => {
      L.marker([d.lat, d.lon])
      .bindPopup("<h3>" + d.name +
      "</h3><hr><p>" + 'Capacity: ' + d.capacity + "</p>")
      .addTo(myMap);
      
      })
  

    })};

//Now we are using the newly made functions here to push the data onto our HTML
  createMarkers(link);
  createMap(link);

// Create the createMarkers function


// Pulling the data from the link
d3.json(link2, function(data2) {
   
  //Here we are setting variable for markers
  //We set the markers variable here because we needed to slice the amount of data we are gathering using the SLICE function
    var markers2 = data2.data.stations
    limit2 = 100
    markers2 = markers2.slice(0, limit2)
    
  //Here is our for loop. NOTE that we are using our new variable MARKERS, due to prior slicing
  //NOTE we are binding our popup data within our FOR loop.   
    var filter = {"0": true}
    var result = markers2.filter(item => filter[item.is_installed])});
    console.log (markers2)

