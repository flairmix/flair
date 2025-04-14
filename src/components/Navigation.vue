<template>

	<div class="mt-8 flex flex-wrap justify-center gap-10">

		<div class="flex flex-col items-center w-[320px]">
			<router-link 
				to="/blog/bim"
				class="peer px-4 py-2 border border-white text-white rounded hover:bg-white hover:text-black transition cursor-pointer">
				Flair : BIM
			</router-link>
			<div class="mt-6 px-4 py-2 text-sm text-gray-400 border border-transparent rounded 
						peer-hover:border-blue-500 peer-hover:text-blue-400 transition text-center w-full pointer-events-none"
						data-ru="Моделирование, автоматизация проектирования"
       					data-en="Modeling, design automation">
						Моделирование, автоматизация проектирования
			</div>
		</div>

		<div class="flex flex-col items-center w-[320px]">
			<router-link 
			to="/blog/hvac"
			 class="peer px-4 py-2 border border-white text-white rounded hover:bg-white hover:text-black transition cursor-pointer">
			Flair : HVAC
			</router-link>
			<div class="mt-6 px-4 py-2 text-sm text-gray-400 border border-transparent rounded 
						peer-hover:border-blue-500 peer-hover:text-blue-400 transition text-center w-full pointer-events-none"
						data-ru="Инженерные системы, расчёты"
						data-en="HVAC systems, calculations">
						Инженерные системы, расчёты
			</div>
		</div>

		<div class="flex flex-col items-center w-[320px]">
			<router-link 
			to="/blog/code" 
			class="peer px-4 py-2 border border-white text-white rounded hover:bg-white hover:text-black transition cursor-pointer">
			Flair : Code
			</router-link>
			<div class="mt-6 px-4 py-2 text-sm text-gray-400 border border-transparent rounded 
						peer-hover:border-blue-500 peer-hover:text-blue-400 transition text-center w-full pointer-events-none"
						data-ru="Скрипты, аддоны, Revit API, AI и NER-инструменты"
						data-en="Scripts, add-ons, Revit API, AI & NER tools">
						Скрипты, аддоны, Revit API, AI и NER-инструменты
			</div>
		</div>
	</div>






</template>

