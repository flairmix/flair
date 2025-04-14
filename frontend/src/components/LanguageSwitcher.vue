<template>
    <div class="flex justify-end w-full pt-3 mb-4 text-sm text-gray-400 gap-3 px-6">
      <button class="border border-gray-600 px-2 py-1 rounded text-xs hover:bg-white hover:text-black" @click="$emit('languageChange', 'ru')">RU</button>
      <button class="border border-gray-600 px-2 py-1 rounded text-xs hover:bg-white hover:text-black" @click="$emit('languageChange', 'en')">EN</button>
      <button class="border border-gray-600 px-2 py-1 rounded text-xs hover:bg-white hover:text-black" @click="$emit('fontToggle')">Font</button>
    </div>
</template>
  
    