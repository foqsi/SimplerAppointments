import './tailwind.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import posthogPlugin from "./plugins/posthog"

const app = createApp(App);
app.use(posthogPlugin);
app.use(router);

app.mount('#app');
