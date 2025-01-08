<template>
  <div class="min-h-screen flex flex-col items-center py-8 px-4">
    <h1 class="text-3xl font-bold mb-4">Settings</h1>
    <div class="card shadow-lg p-6 w-96">
      <form @submit.prevent="updateSettings">
        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Name</label>
          <input
            type="text"
            class="input input-bordered w-full"
            v-model="settings.name"
          />
        </div>
        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Email</label>
          <input
            type="email"
            class="input input-bordered w-full"
            v-model="settings.email"
          />
        </div>
        <div class="mb-4">
          <label class="block text-sm font-medium mb-1">Password</label>
          <input
            type="password"
            class="input input-bordered w-full"
            v-model="settings.password"
          />
        </div>
        <button type="submit" class="btn btn-primary w-full">Save Changes</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "SettingsPage",
  data() {
    return {
      settings: {
        name: "John Doe",
        email: "johndoe@example.com",
        password: "",
      },
    };
  },
  methods: {
    updateSettings() {
      // Mock saving data (replace with actual API request)
      console.log("Updated settings:", this.settings);
      alert("Settings saved successfully!");
      this.$router.push("/profile"); // Navigate back to the profile page
    },
  },
};
</script>

<style scoped>
.card {
  background-color: white;
  border-radius: 0.5rem;
}
</style>
