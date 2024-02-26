<script setup lang="ts">
</script>

<template>
  <div>
    <Menu class="w-full md:w-15rem">
      <template #start>
        <span class="inline-flex align-items-center gap-1 px-2 py-2">
          <svg width="35" height="40" viewBox="0 0 35 40" fill="none" xmlns="http://www.w3.org/2000/svg" class="h-2rem">
            <path d="..." fill="var(--primary-color)" />
            <path d="..." fill="var(--text-color)" />
          </svg>
          <span class="font-medium text-xl">PRIME<span class="text-primary">APP</span></span>
        </span>
      </template>
      <template>
        <span class="text-primary font-bold">OI</span>
      </template>
      <template>
        <a v-ripple class="flex align-items-center">
          <span class="ml-2">OI</span>
          <span class="ml-auto border-1 surface-border border-round surface-100 text-xs p-1">OI</span>
        </a>
      </template>
      <template #end>
        <button v-ripple
          class="relative overflow-hidden w-full p-link flex align-items-center p-2 pl-3 text-color hover:surface-200 border-noround">
          <Avatar image="/public/cachorro.png" class="mr-2" shape="circle" />
          <span class="inline-flex flex-column">
            <span class="font-bold">ASDAWDADWDDa</span>
            <span class="text-sm">Admin</span>
          </span>
        </button>
      </template>
    </Menu>
  </div>
</template>