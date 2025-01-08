<template>
  <div class="min-h-screen flex flex-col items-center py-8 px-4">
    <h1 class="text-4xl font-bold mb-8">Pricing Plans</h1>
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 w-full max-w-5xl">
      <!-- Free Plan -->
      <div class="card border shadow-md p-6">
        <h2 class="text-2xl font-semibold mb-4 text-center">Free</h2>
        <p class="text-gray-600 mb-6 text-center">
          Perfect for individuals just getting started.
        </p>
        <ul class="mb-6 text-gray-600 space-y-2">
          <li>✔ Basic Features</li>
          <li>✔ Limited Support</li>
          <li>✖ Customization Options</li>
        </ul>
        <div class="text-center">
          <button class="btn btn-outline w-full">Get Started</button>
        </div>
      </div>

      <!-- $20 Plan -->
      <div class="card border shadow-md p-6">
        <h2 class="text-2xl font-semibold mb-4 text-center">$20/month</h2>
        <p class="text-gray-600 mb-6 text-center">
          Great for small teams or projects.
        </p>
        <ul class="mb-6 text-gray-600 space-y-2">
          <li>✔ All Free Plan Features</li>
          <li>✔ Priority Support</li>
          <li>✔ Limited Customization</li>
        </ul>
        <div class="text-center">
          <button class="btn btn-primary w-full">Choose Plan</button>
        </div>
      </div>

      <!-- $50 Plan -->
      <div class="card border shadow-md p-6">
        <h2 class="text-2xl font-semibold mb-4 text-center">$50/month</h2>
        <p class="text-gray-600 mb-6 text-center">
          Best for businesses and advanced users.
        </p>
        <ul class="mb-6 text-gray-600 space-y-2">
          <li>✔ All $20 Plan Features</li>
          <li>✔ Full Customization</li>
          <li>✔ Dedicated Support</li>
        </ul>
        <div class="text-center">
          <button class="btn btn-primary w-full">Choose Plan</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PricingPage",
};
</script>

<style scoped>
.card {
  background-color: white;
  border-radius: 0.5rem;
  transition: transform 0.2s, box-shadow 0.2s;
}
.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
}
</style>
