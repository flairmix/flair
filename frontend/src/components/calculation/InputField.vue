<template>
  <div class="p-2">
    <label class="block text-sm font-medium">{{ label }}</label>
    <input
      v-model.number="localValue"
      type="number"
      class="w-full p-2 border rounded"
      :placeholder="placeholder"
    />
    <p class="text-xs text-gray-500 mt-1">{{ description }}</p>
  </div>
</template>

<script setup>
import { computed } from "vue"

const props = defineProps({
  modelValue: Number,
  label: String,
  description: String,
  placeholder: String
})
const emit = defineEmits(["update:modelValue"])

const localValue = computed({
  get: () => props.modelValue,
  set: (val) => emit("update:modelValue", val)
})
</script>
