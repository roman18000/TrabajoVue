<template>

    <h1>
        Recorridos de evacuacion y puntos de encuentro
    <div class="container mt-4" v-if="isCreated">
        <Map :points_data="points" :routes_data="routes" />
    </div>
    <div v-else>
        <h1>Cargando mapa..</h1>
        <div class="d-flex justify-content-center">
          <div class="spinner-border" role="status">
            <span class="sr-only"></span>
          </div>
        </div>
    </div>
    </h1>
</template>


<script>
import Map from './Map'
export default {
    name:'routes-component',
    components:{Map},
    data() {
        return {
            points: [],
            routes: [],
            mapIsCreated:false
        };
    },
    async created() {
        const responseOfPoints = await fetch("https://admin-grupo3.proyecto2021.linti.unlp.edu.ar/api/points/all");
        const responseOfRoutes = await fetch("https://admin-grupo3.proyecto2021.linti.unlp.edu.ar/api/route_of_evacuation/");
        const dataOfPoints = await responseOfPoints.json();
        const dataOfRoutes = await responseOfRoutes.json();
        this.points = dataOfPoints;
        this.routes = dataOfRoutes.recorridos;
        this.mapIsCreated = true;
    },
    computed: {
         isCreated () {
            return this.mapIsCreated;
        }
    }

}
</script>


<style>

</style>
