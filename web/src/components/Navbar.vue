<template>
  <nav class="navbar navbar-expand-lg navbar-dark static-top " style="background-color: black">
    <div class="container">
      <a class="navbar-brand" href="#">
        <img
          src="../assets/images/logo.png"
          alt="Logo"
          height="45"
          width="55"
        />
      </a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <router-link to="/" class="nav-link"> Inicio </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/reports" class="nav-link">
              Denuncias
            </router-link>
          </li>
          <li>
            <router-link to="/meeting-points" class="nav-link">
              Puntos de encuentro
            </router-link>
          </li>
          <li>
            <router-link to="/routes-of-evacuation" class="nav-link">
              Rutas de evacuacion
            </router-link>
          </li>
          <li>
            <router-link to="/flood-zones" class="nav-link">
              Zonas inundables
            </router-link>
          </li>


        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped></style>
