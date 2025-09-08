<template>
  <div class="max-w-md mx-auto p-4 rounded-xl shadow">
    <NameField v-model="name" />
    <DescriptionField v-model="description" />

    <InputField
      v-model="inputValue"
      label="Input Value"
      description="Enter a number to calculate"
      placeholder="e.g. 10"
    />

    <OutputField :value="calculatedOutput" />
  </div>
</template>

<script setup>
import { ref, computed } from "vue"
import NameField from "./NameField.vue"
import DescriptionField from "./DescriptionField.vue"
import InputField from "./InputField.vue"
import OutputField from "./OutputField.vue"

const name = ref("")
const description = ref("")
const inputValue = ref(0)

const calculatedOutput = computed(() => inputValue.value * 2) // example calc
</script>
