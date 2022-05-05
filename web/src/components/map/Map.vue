<template>
  <l-map style="height: 400px" :zoom="zoom" :center="center">
    <l-tile-layer :url="url" :attribution="attribution"></l-tile-layer>

            <div v-for="(point, index) in points_data" :key="index">
            <l-marker :lat-lng="formatCoordinates(point)" name="Hi!!" v-on:click="eventOnClick(point)">
                <l-tooltip>
                    <ul>
                        <li><strong>{{ point.name }}</strong></li>
                        <li><strong>{{ point.address }}</strong></li>
                        <li><strong>{{ point.phone }}</strong></li>
                        <li><strong>{{ point.email }}</strong></li>
                    </ul>
                </l-tooltip>
            </l-marker>
            </div>
  </l-map>
</template>

<script>
import { LMap, LTileLayer, LMarker, LTooltip } from "@vue-leaflet/vue-leaflet";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
    LTooltip,
  },
  props: ["points_data"],
  data() {
    return {
      url: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
      zoom: 13,
      center:  [-34.9214, -57.9544],
      address: "",
      show:false
    };
  },
  created() {
    //do we support geolocation
    if(!("geolocation" in navigator)) {
      // this.errorStr = 'Geolocation is not available.';
      this.center = [-34.9214, -57.9544]
      return;
    }

    navigator.geolocation.getCurrentPosition(pos => {
      // this.center =;
      console.log(pos);
    }, err => {
      // this.gettingLocation = false;
      // this.errorStr = err.message;
      console.log(err);
    })
  },
  methods: {
    formatCoordinates(point) {
      return [point.coordinates_latitude, point.coordinates_longitude];
    },
    eventOnClick(point) {
      var txt = "Nombre " + point.name+
          "  Direccion " +  point.address +
          "  Telefono " + point.phone +
          "  Email " + point.email;
        alert(txt)
  },
  },


};

</script>
