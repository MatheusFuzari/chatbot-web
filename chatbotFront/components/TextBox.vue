
import type { mergeProps } from 'vue';
<script setup leng="ts">
    const props = defineProps({
        avatarImage: {type: String},
        name: {type: String},
        message: {type: String},
        side: {type: String}
    })

    const cardStyle = computed(()=>(props.side == 'left' ? 
        {
            color: 'red',
            size: '15px'
        } :
        {
            color: 'blue',
            size: '25px'
        }
    ))
</script>
<template>
    <div>
        <Fieldset :class="props.side == 'left' ? 'question' : 'answer' ">
            <template #legend>
                <div class="flex align-items-center pl-2">
                    <Avatar :image="props.avatarImage" shape="circle" />
                    <span class="font-bold">{{ props.name }}</span>
                </div>
            </template>
            <p class="m-0">
                {{ props.message }}
            </p>
        </Fieldset>
    </div>
</template>

<style scoped lang='scss'>
    .question{
        .p-fieldset-legend div{
            display: flex;
            justify-content: flex-end;
        }

        .p-toggleable-content .p-fieldset-content p{
            display: flex;
            justify-content: flex-end;
        }
    }
    .answer{
        .p-fieldset-legend div{
            display: flex;
            justify-content: flex-end;
        }

        .p-toggleable-content p{
            display: flex;
            justify-content: flex-end;
        }
    }
    
</style>