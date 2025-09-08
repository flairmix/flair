<template>
  <div class="bg-grid p-6 rounded-xl shadow-xl border border-gray-800 max-w-md mx-auto space-y-4">
    <!-- Name -->
    <h2 class="text-xl font-bold text-gray-100">{{ name }}</h2>

    <!-- Description -->
    <p class="text-gray-300">{{ description }}</p>

    <!-- Dynamic Inputs -->
    <div v-for="(input, index) in inputs" :key="index" class="desc-item p-2">
      <label class="text-sm font-semibold text-gray-300">{{ input.label }}</label>
      <input
        v-model.number="input.value"
        type="number"
        :placeholder="input.placeholder || ''"
        class="w-full p-2 rounded-lg border border-gray-700 bg-neutral-900 text-gray-100 hover-code-style transition-colors duration-200"
      />
      <p v-if="input.description" class="text-xs text-gray-500 mt-1">{{ input.description }}</p>
    </div>

    <!-- Calculate Button -->
    <button
      @click="calculate"
      class="w-full p-2 rounded-lg bg-[#3a86ff] text-white font-semibold hover:bg-[#2a6fd4] transition-colors"
      :disabled="loading"
    >
      {{ loading ? 'Загрузка...' : 'Расчет' }}
    </button>

    <!-- Output -->
    <div v-if="output !== null" class="w-full p-2 rounded-lg border border-gray-700 bg-neutral-800 text-[#3a86ff] font-bold mt-2">
      {{ output }}
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, watch } from "vue"

// Props
const props = defineProps({
  name: String,
  description: String,
  inputs: {
    type: Array,
    default: () => []
    /*
    Example:
    [
      { label: 'Alpha', param: 'alpha', description: 'Введите alpha', value: 12 },
      { label: 'Q0', param: 'q0_hr', description: 'Введите Q0', value: 200 }
    ]
    */
  },
  apiUrl: {
    type: String,
    required: true
  },
  apiResponseKey: {
    type: String,
    default: "result"
  }
})

const output = ref(null)
const loading = ref(false)

// Локальные reactive input’ы
const inputs = reactive(props.inputs.map(i => ({ ...i, value: i.value ?? 0 })))

// Синхронизация при изменении props.inputs
watch(
  () => props.inputs,
  (newInputs) => {
    inputs.splice(0, inputs.length, ...newInputs.map(i => ({ ...i, value: i.value ?? 0 })))
  },
  { deep: true }
)

// Функция расчета через GET-запрос
const calculate = async () => {
  loading.value = true
  try {
    // Формируем параметры URL
    const params = new URLSearchParams()
    inputs.forEach(inp => {
      const key = inp.param || inp.label
      params.append(key, inp.value)
    })

    const url = `${props.apiUrl}?${params.toString()}`
    const res = await fetch(url)

    if (!res.ok) throw new Error(`Ошибка запроса: ${res.status}`)
    const data = await res.json()
    output.value = data[props.apiResponseKey] ?? JSON.stringify(data)
  } catch (e) {
    output.value = "Ошибка: " + e.message
  } finally {
    loading.value = false
  }
}
</script>
