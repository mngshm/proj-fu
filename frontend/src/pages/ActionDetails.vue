<template>
  <div class="justify-center items-center top-0 bottom-0  ">
  <div class="px-64 py-5 flex flex-row justify-between items-center ">
    
    <h1 class="font-black text-5xl text-gray-900">{{ action.doc.title }}</h1>
    <div>
      <Button @click="action.setValue.submit({'status': 'Archive'})" v-if="action.doc.status !='Archived'" class="m-2 text-red-500 border-red-500" icon-left="trash">Delete</Button>
      <Button @click="action.setValue.submit({'status': 'Completed'})" v-if="action.doc.status === 'ToDo'" class="m-2 text-green-500 border-green-500" icon-left="done">Mark as Done</Button>
    </div>
  </div>
  <div class="mx-20 my-5 flex flex-row items-center">
    <p>{{ action.doc.description }}</p>
  </div>
  <div class="mx-20 my-5 flex flex-row justify-center">
    <Button class="m-2" icon-left="arrow-left" @click="router.back()">Go back</Button>
  </div>
  </div>
</template>

<script setup>

import {ref } from 'vue'
import {useRouter} from 'vue-router'
import { TextEditor, createDocumentResource } from 'frappe-ui' 

const content = ref('')
const router = useRouter()
const props = defineProps(['name']);

const action = createDocumentResource({
  doctype: 'Actions',
  name: props.name
})
</script>
