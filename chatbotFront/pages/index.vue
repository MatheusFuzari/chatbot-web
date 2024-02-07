<script setup>
    let question = ref('')
    let respon = ref('')
    const SendForm = async() => {
        console.log(question)
        const {data: bardRes} = await useFetch("http://127.0.0.1:8000/chatbot/",
        {
            method: 'POST',
            body: {
                'question': question
            },
        })
        console.log(bardRes)
        respon.value = bardRes.value
    }

    const dialog = {
        type: '',
        message: '',
    }


    let dialogs = ref([])

    const addDialog = computed((diag)=>(dialogs.push(diag)))
</script>
<template>
    <div class="">
        <div :v-for="(d, index) in dialogs" :key=index>
            <TextBox avatarImage="gibby.png" name="Gibby pança de égua" :message="d.message" :side="d.type" TextBox>></TextBox>
        </div>
        <label class="text-red-500">Ask anything...: </label>
        <br>
        <textarea v-model='question' class="border-2 border-blue-300"></textarea>
        <br>
        <Button label="Ask" @click="SendForm"></Button>
    </div>
    <br>
    <hr class="bg-black text-black h-1">
    <br>
    <div>
        <h2>Bard: </h2>
        <p>
            {{ respon.content }}
        </p>
    </div>
    <br>
    <TextBox avatarImage="gibby.png" name="Gibby pança de égua" message="It's that glock? It's that glock?" side="left" TextBox>></TextBox>
    <TextBox avatarImage="cachorro.png" name="Cachorro barriga d'verme" message="Oh my godness, mate!" side="right"></TextBox>
</template>