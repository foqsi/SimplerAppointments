<template>
  <header class="shadow fixed top-0 left-0 right-0 z-10 bg-base-100">
    <div class="navbar mx-auto w-full max-w-screen-xl">
      <!-- Left Section -->
      <div class="navbar-start">
        <SideMenu />
        <a href="/" class="btn btn-ghost lg:hidden text-lg -ml-8"
          >SimplerAppointments</a
        >
      </div>

      <!-- Center Links -->
      <div class="navbar-center lg:flex">
        <ul class="menu menu-horizontal px-1 text-lg">
          <!-- Brand -->
          <a href="/" class="btn btn-ghost hidden lg:flex text-xl -ml-4"
            >SimplerAppointments</a
          >
        </ul>
      </div>

      <!-- Right Section -->
      <div class="navbar-end flex items-center gap-2">
        <!-- SwapTheme -->
        <SwapTheme />

        <!-- Profile Dropdown -->
        <div v-if="isLoggedIn" class="dropdown dropdown-end">
          <div tabindex="0" class="btn btn-ghost btn-circle avatar">
            <div class="w-10 rounded-full">
              <img
                alt="Profile Avatar"
                src="data:image/png;base64,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"
              />
            </div>
          </div>
          <ul
            tabindex="0"
            class="menu menu-sm dropdown-content bg-base-100 mt-3 w-24 p-2 shadow"
          >
            <!-- <li>
              <a href="/profile" class="justify-between">
                Profile
                <span class="badge">New</span>
              </a>
            </li> -->
            <!-- <li><a href="/settings">Settings</a></li> -->
            <li><a @click="logout">Logout</a></li>
          </ul>
        </div>
        <!-- Login Button -->
        <a v-if="!isLoggedIn" href="/login" class="btn">Login</a>
      </div>
    </div>
  </header>
</template>

<script>
import { ref, onMounted } from "vue";
import { supabase } from "../utils/supabase";
import { useRouter } from "vue-router"; // Import useRouter
import SwapTheme from "./SwapTheme.vue";
import SideMenu from "./SideMenu.vue";

export default {
  name: "NavBar",
  components: {
    SwapTheme,
    SideMenu,
  },
  setup() {
    const isLoggedIn = ref(false);
    const router = useRouter();

    // Check user session on component mount
    onMounted(async () => {
      const {
        data: { session },
      } = await supabase.auth.getSession();
      isLoggedIn.value = !!session;

      // Listen for auth state changes
      supabase.auth.onAuthStateChange((event, session) => {
        isLoggedIn.value = !!session;
      });
    });

    // Logout function
    const logout = async () => {
      try {
        await supabase.auth.signOut();
        isLoggedIn.value = false;
        router.push("/logout"); // Redirect to LogoutPage
      } catch (error) {
        console.error("Error logging out: ", error);
      }
    };

    return {
      isLoggedIn,
      logout,
    };
  },
};
</script>
