<script setup>
    const itens = []
    let response = ref("")
    const dialog = reactive({
        text: '',
        type: '',
        name: '',
        image: '',
        historyId: null
    });

    const includeDialog = ((type) => {
        if (type === 'Q') {
            dialog.image = 'cachorro.png';
            dialog.name = 'Fuzari';
            dialog.type = 'right';
        } else {
            dialog.image = 'gibby.png';
            dialog.name = 'Bot';
            dialog.type = 'left';
        }
        // faz a cópia profunda da estrutura com os valores atuais (deep copy)
        conversationHistory.value.push(
            JSON.parse(JSON.stringify(dialog))
        );
    });
    const sendMessage = async () => {
        console.log(dialog.text);
        includeDialog('Q');

        //message.value;
        const { data: answer } = await useFetch('http://localhost:8000/chatbot/', {
            method: 'POST',
            body: {
                question: dialog.text,
                userId: 1,
                conversationId: dialog.historyId
            }
        })
        dialog.text = answer.value.message
        dialog.historyId = answer.value.history.id
        includeDialog('A');
        dialog.text = '';
    }
    const { data: requestHistory } = await useFetch('http://127.0.0.1:8000/history/1')
    for (let i = 0; i <= requestHistory._value.length - 1; i++) {
        let myObj = { label: requestHistory._value[i].id, icon: "iconoir:message-solid" }
        itens.push(myObj);
    }
    const conversationHistory = ref([])
</script>

<template>
    <div class="overflow-hidden bg-gray-900">
        <main class="absolute ml-96 mr-2 mt-2">
            <div class="bg-zinc-900 w-[calc(100vw-32rem)] h-[calc(100vh-6rem)] text-white rounded-lg">
                <div class="h-[calc(100vh-15rem)] overflow-y-scroll m-5 mt-5">
                    <div v-for="(conversation, id) in conversationHistory" :key="id">
                        <TextBox :name="conversation.name" :avatarImage="conversation.image"
                            :message="conversation.text" :type="conversation.type" />
                    </div>
                </div>
                <div class="bottom-0 absolute">
                    <input type="text" v-model="dialog.text"
                        class=" text-blue-950 font-bold bg-slate-50 rounded-3xl h-20 w-[calc(100vw-35rem)] m-5" />
                    <Button @click="sendMessage"
                        class="w-14 h-14 bg-slate-800 rounded-3xl items-center text-center justify-center fixed bottom-[calc(1vh+7rem)] left-[calc(100vw-14rem)]">
                        <Icon name="material-symbols:send" size="2rem"></Icon>
                    </Button>
                </div>
            </div>
        </main>
        <Sidebar :itens="itens" />
    </div>
</template>

<style scoped>
    /* button{
        background-color: black;
        color: white;
    } */
</style>