//./plugins/posthog.js
import posthog from "posthog-js";

export default {
  install(app) {
    app.config.globalProperties.$posthog = posthog.init(
      "phc_SCT9TkM0b7uIk6OKgR39Cxg84bfjN444naPXrR48Vuf",
      {
        api_host: "https://us.i.posthog.com",
      }
    );
  },
};
