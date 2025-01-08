<template>
  <div class="flex">
    <!-- Overlay -->
    <div
      v-if="isOpen"
      class="fixed top-0 left-0 w-full h-full bg-black bg-opacity-50 z-40"
      @click="toggleMenu"
    ></div>

    <!-- Side Menu -->
    <div
      :class="[
        'fixed top-0 left-0 h-full bg-base-100 shadow-lg z-50 transform transition-transform duration-300',
        isOpen ? 'translate-x-0' : '-translate-x-full',
      ]"
      style="width: 250px"
    >
      <div class="flex flex-col h-full">
        <!-- Header with Close Button -->
        <div class="flex items-center justify-between px-4 py-3 border-b">
          <h2 class="text-xl font-bold">Navigation</h2>
          <button class="btn btn-ghost btn-sm" @click="toggleMenu">✕</button>
        </div>

        <!-- Menu Items -->
        <nav class="flex-1 p-4">
          <ul class="menu menu-vertical text-xl">
            <li><a href="/dashboard">Dashboard</a></li>
            <div class="divider"></div>
            <li><a href="/product">Product</a></li>
            <li><a href="/pricing">Pricing</a></li>
          </ul>
        </nav>

        <!-- Footer Section -->
        <div class="p-4">
          <ul class="menu menu-vertical text-xl">
            <li><a href="/settings">Settings</a></li>
          </ul>
        </div>
        <div class="p-4 border-t">
          <button class="btn btn-primary w-full mt-4">Logout</button>
        </div>
      </div>
    </div>

    <!-- Content Area -->
    <div class="flex-1">
      <!-- Button to Open Menu -->
      <button class="btn m-4" @click="toggleMenu" v-if="!isOpen">☰</button>
      <slot />
    </div>
  </div>
</template>

<script>
export default {
  name: "SideMenu",
  data() {
    return {
      isOpen: false, // Menu is open by default
    };
  },
  methods: {
    toggleMenu() {
      this.isOpen = !this.isOpen;
    },
  },
};
</script>
