<template>
  <div class="min-h-screen flex flex-col items-center py-8 px-4">
    <h1 class="text-3xl font-bold mb-4">Your Profile</h1>
    <div class="card shadow-lg p-6 w-96">
      <div class="flex flex-col items-center">
        <img
          :src="user.profilePicture"
          alt="Profile Picture"
          class="w-24 h-24 rounded-full mb-4"
        />
        <h2 class="text-2xl font-semibold">{{ user.name }}</h2>
        <p class="text-gray-600">{{ user.email }}</p>
      </div>
      <div class="mt-6">
        <button class="btn btn-primary w-full" @click="editProfile">Edit Profile</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProfilePage",
  data() {
    return {
      user: {
        name: "John Doe",
        email: "johndoe@example.com",
        profilePicture: "https://via.placeholder.com/150", // Placeholder for profile picture
      },
    };
  },
  methods: {
    editProfile() {
      this.$router.push("/settings"); // Navigate to settings to edit profile
    },
  },
};
</script>

<style scoped>
/* Optional styling */
.card {
  background-color: white;
  border-radius: 0.5rem;
}
</style>
