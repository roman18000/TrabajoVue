<template>
<div class="card" style="width: 255px; height:320px">
  <img width="100" height="165" class="card-img-top" :src="getImage" alt="Card image cap">
  <div class="card-body">
    <p class="card-text" style="font-weight:bold">{{text}}</p>
  </div>
  <router-link :to="link" class="btn btn-primary"> Ir </router-link>
</div>
</template>


<script>
export default { 
    name:'Card-Component',
    props: ['image_name', 'text', 'link'],
    computed: { 
       getImage() { 
          return require(`../../assets/images/${this.image_name}.png`);
       }
    }

    
}



</script>


<style>

</style>