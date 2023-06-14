<template>
  <div class="max-w-3xl py-12 mx-auto">
    <div class="flex flex-row items-center justify-between">
      <h1 class="text-5xl">List</h1>
      <Button icon-left="plus">New List</Button>
    </div>

    <div class="py-5">
      <Card title="General">
        <div>
          <ul>
            <li class="flex flex-row space-y-5 justify-between" v-for="action in actions.data" :keys="actions.title">
              <router-link :to="`actions/${action.name}`">
                {{ action.title }}
              </router-link>

              <Button @click="() => completeAction(action.name)" icon="check"></Button>
            </li>
          </ul>

          <div id="add-action" class="flex justify-center ">
            <Button @click="AddActionDialogShown = true" icon-left="plus">New Action</Button>
          </div>
        </div>
      </Card>
    </div>
    <Dialog :options="{
      title: 'Add New Action',
      description: 'Fill the form to Add new Action',
      actions: [
        {
          label: 'Add Action',
          appearance: 'primary',
          handler: ({ close }) => {
            addAction();
            close();
          },
        },
        { label: 'Cancel' },
      ]
    }" v-model="AddActionDialogShown">
    <template #body-content class="">
            <Input label="Action Name" type="text" required placeholder="Action Name" v-model="action.title"/> 
            <Input label="List" type="select" :options="categoryOptions" v-model="action.category"/>
            <Input label="Descriptoin" type="text" required placeholder="Describe Task" v-model="action.description" />
            <Input label="Status" type="checkbox" required />
    </template>
    </Dialog>

  </div>
</template>

<script setup>
import { Dialog, createListResource, Card , Input} from 'frappe-ui'
import { reactive, ref, computed } from 'vue'

const action = reactive({
  title: '',
  category: 'General',
  description: ''
})

const categories = createListResource({
  doctype: 'Category',
  fields: ['name'],
  transform(categories) {
    return categories.map((c) => c.name)
  },
  cache: 'actions',
})
categories.reload()

const categoryOptions = computed(() => {
  if (categories.list.loading || !categories.data) {
    return []
  }
  return categories.data
})

const completeAction = (actionName) => {
  actions.setValue.submit({
    name: actionName,
    status: 'Completed',
    onSuccess() {
      actions.reload()
    },
  })
}

const AddActionDialogShown = ref(false)
const actions = createListResource({
  doctype: "Actions",
  fields: ['name', 'title', "date", 'description', 'status']
})

actions.reload()

const addAction = () => {
  
  actions.insert.submit(action)
}
</script>
