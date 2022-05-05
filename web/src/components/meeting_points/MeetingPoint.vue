<template>
<h1>
    Meeting Point View
</h1>

<div class="container mt-4" v-if="isCreated">
    <Map :points_data="points" />
</div>
<div v-else>
    <h1>Cargando mapa..</h1>
    <div class="d-flex justify-content-center">
      <div class="spinner-border" role="status">
        <span class="sr-only"></span>
      </div>
    </div>
</div>
<div class="container mt-5">
      <div class="card text-white bg-info mb-3" v-for="(point, index) in points" :key="index">
        <div class="card-header">"informacion de muestra"</div>
        <div class="card-body">
          <h5 class="card-title">{{point.address}}</h5>
          <p class="card-text">
            Nro. de telefono: <strong>{{point.phone}}</strong>
          </p>
          <p>Email: <strong>{{point.email}}</strong> </p>
        </div>
      </div>
</div>


</template>


<script>
import Map from '../map/Map'
export default {
    name:'meeting-index',
    components:{Map},
    data() {
        return {
            points: [ ],
            errors:[ ],
            mapIsCreated: false
        }
    },

    async created() {
        const response = await fetch("https://admin-grupo3.proyecto2021.linti.unlp.edu.ar/api/points/all");
        const data = await response.json();
        this.points = data;
        this.mapIsCreated = true;

    },
    computed: {
         isCreated () {
            return this.mapIsCreated;
        },

    },


}
</script>


<style>

</style>
