<template>
  <h1 class="title">Denunciar</h1>
  <form
    v-on:submit.prevent="submitDenuncia">
    <div  style="width: 50%; float: left ">
      <div class="form-group mt-2 text-center">

        <input
          class="form-control text-center"
          type="text"
          placeholder="Ingrese el titulo de la denuncia"
          v-model="form.title"
          required oninvalid="this.setCustomValidity('ingrese titulo')" oninput="this.setCustomValidity('')"
        />
      </div>
      <div class = "form-group mt-2">


        <select required class="form-control text-center" v-model="form.category">
          <option disabled value="">seleccione categoria</option>
          <option>Alcantarillas</option>
          <option>Basura</option>
          <option>Otros</option>
        </select>
      </div>

      <div class = "form-group mt-2">

        <input
          class="form-control text-center"
          type="text"
          placeholder="Ingrese su nombre"
          v-model="form.first_name"
          required oninvalid="this.setCustomValidity('ingrese nombre')" oninput="this.setCustomValidity('')"
        />
      </div>
      <div class = "form-group mt-2">

        <input
          class="form-control text-center"
          type="text"
          placeholder="Ingrese su apellido"
          v-model="form.last_name"
          required oninvalid="this.setCustomValidity('ingrese apellido')" oninput="this.setCustomValidity('')"
        />
      </div>
      <div class = "form-group mt-2">

        <input
          class="form-control text-center"
          type="text"
          placeholder="Ingrese su telefono"
          v-model="form.phone"
          required oninvalid="this.setCustomValidity('ingrese telefono')" oninput="this.setCustomValidity('')"
        />
      </div>
      <div class = "form-group  mt-2" >

        <input
          type="email"
          class="form-control text-center"
          placeholder="Ingrese su email"
          v-model="form.email"
          required oninvalid="this.setCustomValidity('ingrese email')" oninput="this.setCustomValidity('')"
        />
      </div>
      <div class = "form-group mt-2">
        <textarea
          class = "form-control text-center"
          v-model="form.description"
          placeholder="ingrese una descripción de la denuncia"
          required oninvalid="this.setCustomValidity('ingrese descripcion')" oninput="this.setCustomValidity('')"
        ></textarea>
      </div>
    </div>
    
    <div style="height: 400px; width: 50%; float:right">
      <l-map
        v-if="showMap"
        :zoom="zoom"
        :center="center"
        :options="mapOptions"
        style="height: 80%"
        @update:center="centerUpdate"
        @update:zoom="zoomUpdate"
        @click="addMarker"
      >
        <l-tile-layer :url="url" :attribution="attribution" />
        <l-marker :lat-lng="withPopup" v-model="coordinates">
          <l-popup>
            <div @click="innerClick">I am a popup</div>
          </l-popup>
        </l-marker>
      </l-map>
    </div>

    <div>
      <button type="submit" class="btn-lg btn-success mt-2">Generar denuncia</button>
    </div>
   </form>
</template>

<script>
import { latLng } from "leaflet";
import { LMap, LTileLayer, LMarker, LPopup } from "@vue-leaflet/vue-leaflet";
import axios from 'axios';

export default {
  name: "Example",
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LPopup,
    
  },
  data() {
    return {
      
      coordinates:[],
      form: {
        title: '',
        category: '',
        description: '', 
        coordinates_latitude: '', 
        coordinates_longitude: '',  
        first_name: '', 
        last_name: '',
        phone: '',
        email: ''

      },
      zoom: 13,
      center: [-34.9214, -57.9544],
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      withPopup: {},
      
      currentZoom: 11.5,
      currentCenter: latLng(),
      
      mapOptions: {
        zoomSnap: 0.5
      },
      showMap: true
    };
  },
  methods: {
    zoomUpdate(zoom) {
      this.currentZoom = zoom;
    },
    centerUpdate(center) {
      this.currentCenter = center;
    },
  
    innerClick() {
      alert("Click!");
    },

    addMarker(e){
      this.form.coordinates_latitude = e.latlng['lat'];
      this.form.coordinates_longitude = e.latlng['lng'];
      console.log(this.form.coordinates_longitude);
      //var mark = {};
      //mark = {id:1, coordinates: [e.latlng['lat'],e.latlng['lng']]};
      //console.log(mark);
      console.log(e.latlng);
      console.log(this.withPopup);
      
      this.withPopup = latLng(e.latlng['lat'],e.latlng['lng']);
    },

    submitDenuncia(){
      if(this.form.coordinates_latitude == ''){
        alert("no ingreso coordenadas")
      }
      else{
      axios.post('http://127.0.0.1:5000/api/report/', this.form)
        .catch((error) => {
          error.response.status
        })
      }
    }
   

  }
};
</script>
