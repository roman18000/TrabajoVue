<template>
  <l-map style="height: 400px" :zoom="zoom" :center="center">
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>
    <div v-for="(point, index) in points_data" :key="index">
      <l-marker :lat-lng="formatCoordinates(point)" v-on:click="eventOnClick">
        <l-tooltip>
          <ul>
            <li>
              <strong>{{ point.name }}</strong>
            </li>
            <li>
              <strong>{{ point.address }}</strong>
            </li>
            <li>
              <strong>{{ point.phone }}</strong>
            </li>
            <li>
              <strong>{{ point.email }}</strong>
            </li>
          </ul>
        </l-tooltip>
      </l-marker>
      <l-polyline
        v-for="(route, index) in routes_data"
        :lat-lngs="formatRouteCoordinates(route)"
        color="red"
        :key="index"
      ></l-polyline>
    </div>
  </l-map>
  <div class="row mt-5">
    <div class="col-6">
      <div class="card text-white bg-info mb-3" v-for="(point, index) in points_data" :key="index">
        <div class="card-header">{{point.name}}</div>
        <div class="card-body">
          <h5 class="card-title">{{point.address}}</h5>
          <p class="card-text">
            Nro. de telefono: <strong>{{point.phone}}</strong>
          </p>
          <p>Email: <strong>{{point.email}}</strong> </p>
        </div>
      </div>
    </div>

    <div class="col-6">
      <div class="card" v-for="(route, index) in routes_data" :key="index">
        <div class="card text-white bg-primary mb-3">
          <div class="card-header">{{ route.name }}</div>
          <div class="card-body">
            <p class="card-text">{{ route.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import {
  LMap,
  LTileLayer,
  LMarker,
  LTooltip,
  LPolyline,
} from "@vue-leaflet/vue-leaflet";

export default {
  components: {
    LMap,
    LTileLayer,
    LPolyline,
    LMarker,
    LTooltip,
  },
  props: ["points_data", "routes_data", "email", "name", "phone"],
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 13,
      center: [-34.9214, -57.9544],
      markerLatLng: [51.504, -0.159],
      address: "",
      show: false,
    };
  },
  methods: {
    formatCoordinates(point) {
      return [point.coordinates_latitude, point.coordinates_longitude];
    },
    formatRouteCoordinates(route) {
      const coords = [];
      for (const coor in route.coordinates) {
        coords.push(Object.values(route.coordinates[coor])); // Object.values() convierte el objeto en array [-34,..., -54,...]
      }
      return coords;
    },
  },
};
</script>

<style scoped>
.card-header {
  font-size: 50px;
}

.card-title {
  font-size: 40px;
}

.card-text {
  font-size:25px
}

strong {
  font-size:25px
}


</style>
