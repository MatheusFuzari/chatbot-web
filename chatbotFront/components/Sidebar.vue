<script setup>
const props = defineProps({
  itens: { type: Array }
})
console.log(props.itens)
</script>

<template>
  <aside class="w-60 h-screen border-r-2 bg-gray-950 text-white border-r-gray-700">
    <section class="p-4">
      <img class="w-20 inline" src="https://cdn-icons-png.freepik.com/512/2822/2822451.png" />
      <p class="text-red-400 font-semibold text-xl ml-3 inline">Pinnocchio</p>
    </section>
    <nav>
      <NuxtLink to="/">
        <div class="w-13 h-8 bg-red-800 rounded-lg text-center justify-center m-5">
          <Icon name="octicon:feed-plus-16" class="w-5 h-5 inline" />
          <span class="ml-5">Nova Conversa</span>
        </div>
      </NuxtLink>
      <p class="text-center">Suas conversas:</p>
      <ul class="m-3 h-[calc(100vh-20rem)] overflow-y-scroll">
        <li v-for="(item, index) in props.itens" :key="index"
          class="h-12 cursor-pointer border-gray-500 border-b-2 text-gray-200">
          <NuxtLink :to="`/conversation/${item.label}`">
            <Icon :name="item.icon" />{{ item.label }}
          </NuxtLink>
        </li>
      </ul>
    </nav>
    <section class="bottom-0 fixed ml-12">
      <img src="https://upload.wikimedia.org/wikipedia/pt/b/bf/SpongeBob_SquarePants_personagem.png"
        class="w-20 h-20 rounded-3xl inline">
      <span>User</span>
    </section>
  </aside>
</template>