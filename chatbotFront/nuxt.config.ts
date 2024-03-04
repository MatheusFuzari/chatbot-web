// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    }
  },
  modules: [
    'nuxt-primevue',
    'nuxt-icon'
  ],
  css: ['assets/css/main.css'],
  primevue: {
    components: {
      include: ['Button', 'Fieldset', 'Avatar', 'Menu', 'ScrollPanel',]
    }
  },
})
