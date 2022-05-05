<template>
  <div id="app">
     <Navbar/>    
     <View/>
     <Footer/>
  </div>
</template>

<script>
import Navbar from "./components/Navbar";
import View from "./components/View";
import Footer from "./components/Footer"

export default {
  name: "app",
  components: {
    Navbar,
    View,
    Footer
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50
}
</style>
