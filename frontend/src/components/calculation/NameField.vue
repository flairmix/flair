<template>
  <div class="p-2">
    <label class="block text-sm font-medium">Name</label>
    <input 
      v-model="localValue"
      type="text" 
      class="w-full p-2 border rounded"
      placeholder="Enter name"
    />
  </div>
</template>

<script setup>
import { computed } from "vue"

const props = defineProps({ modelValue: String })
const emit = defineEmits(["update:modelValue"])

const localValue = computed({
  get: () => props.modelValue,
  set: (val) => emit("update:modelValue", val)
})
</script>
