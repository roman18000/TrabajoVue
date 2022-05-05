<template>
<h1>Zona</h1>

<div v-if="isCreated">
  <div>
    <l-map :zoom="zoom" :center="zone.coordinates[1]" style="height: 500px; width: 100%">
      <l-tile-layer :url="url" :attribution="attribution"/>
      <l-polygon :lat-lngs="zone.coordinates" :color="traduced(zone.colour)" :fill="true" :fillColor="traduced(zone.colour)" :fillOpacity="0.5">
      </l-polygon>
    </l-map>
  </div>
  <br>
  <div style="text-align:left">
    <h3><b>{{zone.name}}</b></h3>
    <h4><b>Id: </b>{{zone.id}}</h4>
    <h4><b>Color:</b> {{zone.colour}}</h4>
    <h4><b>Cantidad de coordenadas:</b> {{zone.coordinates.length}}</h4>
    <h4><router-link :to="{ name: 'flood_zone'}" class="btn btn-primary" > Volver</router-link></h4>
  </div>
</div>
<div v-else>
  <h2>Cargando mapa..</h2>
</div>
</template>


<script>
import { LMap, LTileLayer, LPolygon} from "@vue-leaflet/vue-leaflet";

export default { 
    name:'DetailMap-Component',
    components: {
    LMap,
    LTileLayer,
    LPolygon
    },
    data(){
      return{
        zone: [],
        mapIsCreated: false,
        zoom: 12,
        url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
        attribution:'&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
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
    async created() { 
      const response = await fetch(`https://admin-grupo3.proyecto2021.linti.unlp.edu.ar/api/flood_zones/show/${this.$route.params.id}`);
      const data = await response.json();
      this.zone = data.attributes; 
      this.mapIsCreated = true;         
    },
    computed: {  
         isCreated () {  
            return this.mapIsCreated;
          },
    }
}



</script>


<style>

</style>