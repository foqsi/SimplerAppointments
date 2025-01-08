<template>
  <div>
    <!-- Scope Selector -->
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-2xl font-bold">Calendar</h2>
      <select
        v-model="selectedScope"
        @change="loadAppointments"
        class="select select-bordered"
      >
        <option value="user">My Appointments</option>
        <option value="company">Company Appointments</option>
      </select>
    </div>

    <!-- FullCalendar -->
    <FullCalendar
      :plugins="[dayGridPlugin]"
      :initialView="'dayGridMonth'"
      :headerToolbar="headerToolbar"
      :events="events"
      :height="'auto'"
      :locale="'en'"
      :dayMaxEvents="true"
    />
  </div>
</template>

<script>
import FullCalendar from "@fullcalendar/vue3";
import dayGridPlugin from "@fullcalendar/daygrid";
import { supabase } from "../../utils/supabase";

export default {
  name: "CalendarComponent",
  components: {
    FullCalendar,
  },
  data() {
    return {
      selectedScope: "user", // Default scope is 'user'
      events: [], // Calendar events
      headerToolbar: {
        start: "title",
        center: "",
        end: "prev,next today",
      },
    };
  },
  methods: {
    async loadAppointments() {
      const user = await supabase.auth.getUser();
      const userId = user?.data?.user?.id;
      const companyId = user?.data?.user?.user_metadata?.company_id;

      try {
        let data = [];
        if (this.selectedScope === "user") {
          // Fetch user-specific appointments
          const response = await supabase
            .from("appointments")
            .select("*")
            .eq("user_id", userId);

          if (response.error) throw response.error;
          data = response.data;
        } else if (this.selectedScope === "company") {
          // Fetch company-specific appointments
          const response = await supabase
            .from("appointments")
            .select("*")
            .eq("company_id", companyId);

          if (response.error) throw response.error;
          data = response.data;
        }

        // Map data to FullCalendar event format
        this.events = data.map((appointment) => ({
          title: appointment.title,
          start: appointment.start_date,
          end: appointment.end_date,
        }));
      } catch (error) {
        console.error("Error fetching appointments:", error);
        this.events = []; // Ensure the calendar clears if there's an error
      }
    },
  },
  async mounted() {
    await this.loadAppointments(); // Load appointments on initial render
    console.log(dayGridPlugin); // Use dayGridPlugin to prevent "unused vars" error
  },
};
</script>

<style scoped>
/* Optional styling for calendar */
.fc .fc-toolbar-title {
  font-size: 1.25rem;
  font-weight: bold;
}
</style>
