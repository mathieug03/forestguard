//Leaflet initialising and satellite then legend layers
var map = L.map('map', { center: [48.8566, 2.3522], zoom: 2 });

L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    attribution: '&copy; ForestGuard - Imagery: Esri, Maxar, Earthstar Geographics',
    maxZoom: 19,
    minZoom: 2,
}).addTo(map);

L.tileLayer('https://services.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}', {
    maxZoom: 19,
    minZoom: 2,
}).addTo(map);

// Fire icon to be displayed when needed
var fireIcon = L.icon({
    iconUrl: 'https://upload.wikimedia.org/wikipedia/commons/0/0e/Basic_red_dot.png',
    shadowUrl: '',

    iconSize: [40, 40], // size of the icon
    iconAnchor: [20, 20], // point of the icon which will correspond to marker's location
    popupAnchor: [0, -25] // point from which the popup should open relative to the iconAnchor 
});

//L.marker([48.8566, 2.3522], { icon: fireIcon }).addTo(map)
//    .bindPopup('Wildfire in Paris');


// Fonction exposée à Python pour ajouter un point sur la carte
eel.expose(ajouter_point_sur_carte);

function ajouter_point_sur_carte(lat, lon, message) {
    L.marker([lat, lon], { icon: fireIcon }).addTo(map)
        .bindPopup(message);
};

// Ajouter un point test pour vérifier si tout fonctionne
// ajouter_point_sur_carte(48.8566, 2.3522, 'paris');