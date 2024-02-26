// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    'nuxt-primevue',
    'nuxt-icon'
  ],
  primevue: {
    components: {
      include: ['Button', 'Fieldset', 'Avatar', 'Menu', 'Menubar']
    }
  },
})
