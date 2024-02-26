<script setup>
  import 'primeicons/primeicons.css'
  console.log("caralho")
  const itens = [
    {
      label: "cu",
      icon: "pi pi-user"
    },
    {
      label: "caralho"
    }
  ]
</script>
<template>
  <div>
    <Menu :model="itens">
    </Menu>
    <Menubar :model="itens">
    </Menubar>
  </div>
</template>