<template>
  
  <l-map :zoom="zoom" :center="center" style="height: 500px; width: 100%">
  <l-tile-layer :url="url" :attribution="attribution"/>
    <div v-for="(zone, index) in zones_data" :key="index">
    <l-polygon :lat-lngs="zone.coordinates" name="h" :color="traduced(zone.colour)" :fill="true" :fillColor="traduced(zone.colour)" :fillOpacity="0.5">
      <l-popup>{{zone.name}}</l-popup>
    </l-polygon>
    </div>
  </l-map>
</template>

<script>
import { LMap, LTileLayer, LPolygon, LPopup} from "@vue-leaflet/vue-leaflet";

 
export default {
  name: "Zones",
  components: {
    LMap,
    LTileLayer,
    LPolygon,
    LPopup
  },
  props: ["zones_data"],
  data() {
    return {
      zoom: 12,
      center: [-34.92145, -57.95453],
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
    };
  },
  methods: {
        traduced(colour){
            let dic = { "Rojo" : "red",
                "Violeta" : "violet",
                "Amarillo": "yellow",
                "Azul": "blue",
                "Verde": "green"
                }
            return dic[colour]
        }
  },
};
</script>
