<template>
    <div class="bg-grid min-h-screen flex flex-col bg-[#0D0D0D] text-white font-code items-center justify-start">
		<Header/>	
	  	<LanguageSwitcher @fontToggle="cycleFont" @languageChange="setLanguage" />
		<Hero />
		<Navigation />
		<Footer/>
    </div>
</template>
  
  <script setup lang="ts">
	import { ref } from 'vue'
  import Header from '../components/Header.vue'
	import LanguageSwitcher from '../components/LanguageSwitcher.vue'
	import Hero from '../components/Hero.vue'
  import Navigation from '../components/Navigation.vue'
  import Footer from '../components/Footer.vue'
  
  const currentLang = ref<'ru' | 'en'>('en')
  
  function setLanguage(lang: 'ru' | 'en') {
    currentLang.value = lang
    document.querySelectorAll('[data-ru], [data-en]').forEach(el => {
      const val = el.getAttribute(`data-${lang}`)
      if (val) el.textContent = val
    })
  }
  
  function cycleFont() {
    const fonts = ["'JetBrains Mono'", "'Fira Code'", "'IBM Plex Mono'"]
    const html = document.documentElement
    const current = getComputedStyle(html).getPropertyValue('--font-family')?.trim()
    let index = fonts.findIndex(f => current.includes(f.replace(/'/g, '')))
    const nextFont = fonts[(index + 1) % fonts.length]
    html.style.setProperty('--font-family', nextFont)
  }
  </script>
  