import { createRouter, createWebHistory } from "vue-router";
import LandingPage from "../views/LandingPage.vue";
import LoginPage from "../views/LoginPage.vue";
import ProfilePage from "../views/ProfilePage.vue";
import SettingsPage from "../views/SettingsPage.vue";
import PricingPage from "../views/PricingPage.vue";
import ProductPage from "../views/ProductPage.vue";
import LogoutPage from "../views/LogoutPage.vue";

import DashboardPage from "../views/DashboardPage.vue";
import AppointmentsComponent from "../components/dashboard/AppointmentsComponent.vue";
import CalendarComponent from "../components/dashboard/CalendarComponent.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: LandingPage,
    meta: { title: "Simpler Appointments" },
  },
  {
    path: "/login",
    name: "Login",
    component: LoginPage,
    meta: { title: "Login - Simpler Appointments" },
  },
  {
    path: "/profile",
    name: "Profile",
    component: ProfilePage,
    meta: { title: "Profile - Simpler Appointments" },
  },
  {
    path: "/settings",
    name: "Settings",
    component: SettingsPage,
    meta: { title: "Settings - Simpler Appointments" },
  },
  {
    path: "/pricing",
    name: "Pricing",
    component: PricingPage,
    meta: { title: "Pricing - Simpler Appointments" },
  },
  {
    path: "/product",
    name: "Product",
    component: ProductPage,
    meta: { title: "Product - Simpler Appointments" },
  },
  {
    path: "/logout",
    name: "Logout",
    component: LogoutPage,
    meta: { title: "Logout - Simpler Appointments" },
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: DashboardPage,
    meta: { title: "Dashboard - Simpler Appointments" },
    children: [
      {
        path: "calendar",
        component: CalendarComponent,
      },
      {
        path: "appointments",
        component: AppointmentsComponent,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// This navigation guard will run before each route change
router.beforeEach((to, from, next) => {
  // If the route has a title in the meta field, use it; otherwise, fallback to a default title
  document.title = to.meta.title || "El Reno Nail Salon";
  next();
});

export default router;
