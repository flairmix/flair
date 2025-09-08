<template>
  <div class="p-2">
    <label class="block text-sm font-medium">Output</label>
    <div class="w-full p-2 border rounded bg-gray-600" >
      {{ value }}
    </div>
  </div>
</template>

<script setup>
defineProps({ value: [Number, String] })
</script>
