<template>
    <div class="bg-grid min-h-screen flex flex-col bg-[#0D0D0D] text-white font-code items-center justify-start">
    <h1 class="text-3xl font-mono mb-6">Flair : {{ title }} — Публикации</h1>

    <div class="grid md:grid-cols-2 gap-6">
      <div
        v-for="post in posts"
        :key="post.id"
        class="bg-gray-800 p-4 rounded-xl border border-gray-700 hover:border-blue-500 transition"
      >
        <div class="text-xs text-gray-400 mb-1">{{ post.date }} • #{{ post.id }}</div>
        <h3 class="text-lg font-semibold mb-2">{{ post.title }}</h3>
        <p class="text-gray-300">{{ post.description }}</p>
      </div>
    </div>
    <CalculatorWidget
      name="Максимальный расход воды"
      description="Введите параметры для расчета"
      api-url="https://api.flairbim.com/water/calculate_flow_max_hr"
      api-response-key="result"
      :inputs="[
        { label: 'Alpha', param: 'alpha', description: 'Введите alpha', value: 12 },
        { label: 'Q0', param: 'q0_hr', description: 'Введите расход Q0', value: 200 }
      ]"
    />
  </div>
</template>

<script lang="ts" setup>
import { useRoute } from 'vue-router'
import { ref, computed, watch } from 'vue'
import CalculatorWidget from '../components/calculation/CalculatorWidget.vue'


const route = useRoute()
const posts = ref<any[]>([])

const titleMap: Record<string, string> = {
  bim: 'BIM',
  hvac: 'HVAC',
  code: 'Code',
}
const title = computed(() => titleMap[route.params.category as string] ?? 'Блог')

watch(
  () => route.params.category,
  (newCategory) => {
    console.log('Смена категории:', newCategory)
    loadPosts(newCategory as string)
  },
  { immediate: true }
)

function loadPosts(cat: string) {
  posts.value = [
    {
      id: 1,
      title: `Пост из категории "${cat}"`,
      date: '2025-04-14',
      description: `Описание публикации из раздела "${cat}".`,
    },
    {
      id: 2,
      title: `Ещё один пост по "${cat}"`,
      date: '2025-04-13',
      description: `Дополнительное описание для "${cat}".`,
    },
  ]
}
</script>
