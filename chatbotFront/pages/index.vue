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
        respon.value = bardRes
    }
</script>
<template>
    <div>
        <label class="text-red-500">Ask anything...: </label>
        <input type='text' v-model='question' />
        <br>
        <button @click='SendForm' class="w-5 h-3 rounded-sm bg-white border-black text-blue-700">Send</button>
    </div>
    <div>
        <h2>Bard: </h2>
        <p>
            {{ respon }}
        </p>
    </div>
</template>