import { defineConfig } from "@playwright/test";

export default defineConfig({
  timeout: 90000,  
  use: {
    browserName: "chromium",
    headless: false,
    baseURL: "https://google.com",
  },
});
