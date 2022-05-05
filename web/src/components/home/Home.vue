<template>

    <div class="row p-5" style="background-color:#E8E8E8; height:300px">
        <h1 class="text-center mt-2" style="font-family:Times New Roman">Que se puede realizar en esta pagina web?</h1>

        <div class="col-md-2">
            <div class="">
                <img width="155" height="130" src="../../assets/images/logo.png" />
            </div>
        </div>
        <div class="col-md-10 mt-3" >
            <p style="font-size:25px">Los servicios que brindamos en este sistema son para los ciudadanos
                de La Plata y alrededores. Esta dedicado para la prevencion y seguridad en situaciones
                de inundacion.
            </p>
        </div>
    </div>
    <div class="container">
        <div class="row">
            <div class="col-md-4 col-sm-12 mt-3">
                    <Card
                    image_name="meeting-point"
                    text="Conozca los puntos de encuentros mas cercanos a usted"
                    link="/meeting-points"/>
            </div>
            <div class="col-md-4 col-sm-12 mt-3" style="font-size:15px">
                    <Card
                    image_name="recorrido-evacuacion"
                    text="Sepa que recorrido le es mas conveniente y cercano en caso de tener que evacuar"
                    link="/routes-of-evacuation"/>
            </div>
            <div class="col-md-4 col-sm-12 mt-3">
                <Card
                image_name="zonas_riesgo"
                text="Conoza las zonas con mas alta posibilidad de inundacion"
                link="/flood-zones"/>
            </div>

            <div class="col-md-4 col-sm-12 mt-3" style="font-size:15px">
                <Card
                image_name="report"
                text="Denuncie alcantarillas tapadas,basurales,u otras indoles que empeoren una inundacion"
                link="/reports"/>
            </div>
            <div class="col-md-6 col-sm-6 mt-3">
                <Card
                image_name="mapa"
                text="Realize las denuncias relacionadas a inundaciones "
                link="/meeting-points"/>
            </div>


        </div>
    </div>
</template>

<script>
  import Card from './Card';
    export default {
        name:"Home",
        components: {Card}
    }

</script>


<style>

</style>
