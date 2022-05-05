<template>

<h1>
    Zonas Inundables
</h1>

<div class="container mt-4" v-if="isCreated">
    <Map :zones_data="zones" />
</div>
<div v-else>
    <h1>Cargando mapa..</h1>
    <div class="d-flex justify-content-center">
      <div class="spinner-border" role="status">
        <span class="sr-only"></span>
      </div>
    </div>
</div>
<br>
<h2>Zonas</h2>
<table class="table" style="width: 800px; height: 200px;  margin-left: auto; margin-right: auto;">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">Nombre</th>
                <th scope="col">Color</th>
                <th scope="col">Opciones</th>
            </tr>
        </thead>
        <tbody v-for="(zone, index) in zones" :key="index" >
            <tr>
                <th scope="row">{{index}}</th>
                <th>{{zone.name}}</th>
                <th :style="{backgroundColor: traduced(zone.colour)}"></th>
                <th><router-link :to="{ name: 'flood_zone_detail', params: { id: zone.id} }" class="btn btn-primary" > Ver zona  {{zone.id}}</router-link></th>
            </tr>
        </tbody>
</table>
</template>


<script>
import Map from './Map'
export default {
    name:'zones-index',
    components:{Map},
    data() {
        return {
            zones: [ ],
            errors:[ ],
            mapIsCreated: false
        }
    },
    async created() {
        const response = await fetch("https://admin-grupo3.proyecto2021.linti.unlp.edu.ar/api/flood_zones/all");
        const data = await response.json();
        this.zones = data.zonas;  //hago esto porque la api me lo devuelve como zonas[adentro 0{id...}]
        this.mapIsCreated = true;



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
    computed: {
         isCreated () {
            return this.mapIsCreated;
        }
    },

}
</script>


<style>

</style>
