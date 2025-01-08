<template>
  <div class="min-h-screen flex flex-col items-center justify-center gap-4">
    <div class="w-24 h-24 mb-6">
      <!-- TODO: add logo -->
      <img src="" alt="Logo" class="object-contain w-full h-full" />
    </div>

    <label class="input input-bordered flex items-center gap-2 w-72">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 16 16"
        fill="currentColor"
        class="h-5 w-5 opacity-70 leading-none"
      >
        <path
          d="M2.5 3A1.5 1.5 0 0 0 1 4.5v.793c.026.009.051.02.076.032L7.674 8.51c.206.1.446.1.652 0l6.598-3.185A.755.755 0 0 1 15 5.293V4.5A1.5 1.5 0 0 0 13.5 3h-11Z"
        />
        <path
          d="M15 6.954 8.978 9.86a2.25 2.25 0 0 1-1.956 0L1 6.954V11.5A1.5 1.5 0 0 0 2.5 13h11a1.5 1.5 0 0 0 1.5-1.5V6.954Z"
        />
      </svg>
      <input
        v-model="email"
        type="email"
        class="input w-full"
        placeholder="Email"
      />
    </label>

    <label class="input input-bordered flex items-center gap-2 w-72">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 16 16"
        fill="currentColor"
        class="h-5 w-5 opacity-70 leading-none"
      >
        <path
          fill-rule="evenodd"
          d="M14 6a4 4 0 0 1-4.899 3.899l-1.955 1.955a.5.5 0 0 1-.353.146H5v1.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-2.293a.5.5 0 0 1 .146-.353l3.955-3.955A4 4 0 1 1 14 6Zm-4-2a.75.75 0 0 0 0 1.5.5.5 0 0 1 .5.5.75.75 0 0 0 1.5 0 2 2 0 0 0-2-2Z"
          clip-rule="evenodd"
        />
      </svg>
      <input
        v-model="password"
        type="password"
        class="input w-full"
        placeholder="Password"
      />
    </label>

    <button class="btn w-72" @click="handleLogin">Sign in</button>
    <div class="flex justify-center items-center w-72 mx-auto">
      <div class="divider w-full text-center">OR</div>
    </div>
    <button class="btn w-72" @click="handleSignup">Sign up</button>

    <p v-if="error" class="text-red-500 text-center mt-4">{{ error }}</p>
  </div>
</template>

<script>
import { supabase } from "../utils/supabase";

export default {
  data() {
    return {
      email: "",
      password: "",
      error: "",
    };
  },
  methods: {
    async handleLogin() {
      try {
        const { error } = await supabase.auth.signInWithPassword({
          email: this.email,
          password: this.password,
        });

        if (error) {
          this.error = error.message;
        } else {
          localStorage.setItem("isLoggedIn", "true");
          this.$router.push("/dashboard");
        }
      } catch (err) {
        this.error =
          "Error logging in. Please contact the administrator for assistance.";
      }
    },
    async handleSignup() {
      try {
        const { error } = await supabase.auth.signUp({
          email: this.email,
          password: this.password,
        });

        if (error) {
          this.error = error.message;
        } else {
          alert("Signup successful! Please check your email to verify.");
        }
      } catch (err) {
        this.error = "Error signing up. Please try again later.";
      }
    },
  },
  mounted() {
    if (localStorage.getItem("isLoggedIn") === "true") {
      this.$router.push("/login");
    }
  },
};
</script>

<style scoped>
html,
body {
  margin: 0;
  padding: 0;
}
</style>
