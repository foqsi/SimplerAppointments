<template>
  <div class="flex">
    <!-- Sidebar -->
    <aside class="menu menu-vertical p-4 border-r">
      <ul>
        <li>
          <router-link to="/dashboard/calendar">Calendar</router-link>
        </li>
        <li>
          <router-link to="/dashboard/appointments">Appointments</router-link>
        </li>
      </ul>
    </aside>

    <!-- Content Area -->
    <div class="flex-1 p-4">
      <router-view />
    </div>
  </div>
</template>

<script>
export default {
  name: "DashboardPage",
};
</script>
