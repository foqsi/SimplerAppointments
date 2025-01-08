<template>
  <div id="app" class="flex flex-col min-h-screen">
    <!-- Navbar -->
    <NavBar />

    <!-- Main Content -->
    <main class="flex-1 pt-24 pb-24">
      <router-view />
    </main>

    <!-- Footer -->
    <FooterBar />
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import FooterBar from "./components/FooterBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
    FooterBar,
  },
};
</script>
