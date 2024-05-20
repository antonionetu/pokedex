<template>
    <section v-if="pokemon" class="pokemon-details">
        <img :src="gifPath" :alt="pokemon.name" />
        <div>
            <h1>{{ pokemon.name }}</h1>
            <div class="pokemon-attributes">
                <p><strong>Height:</strong> {{ pokemon.height }}</p>
                <p><strong>Weight:</strong> {{ pokemon.weight }}</p>
                <p>
                    <strong>Type:</strong>
                    {{ pokemon.types.map((type) => type.type.name).join(", ") }}
                </p>
                <p>
                    <strong>Abilities:</strong>
                    {{ pokemon.abilities.map((ability) => ability.ability.name).join(", ") }}
                </p>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref, watch } from "vue"
import { useRoute } from "vue-router"

const route = useRoute()
const pokemon = ref(null)
const gifPath = ref(null)
const apiUrl = import.meta.env.VITE_API_URL

watch(() => route.params.name, fetchData, { immediate: true })

function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1)
}

async function fetchData(name) {
    const response = await fetch(`${apiUrl}/pokemon/${name}`)
    const data = await response.json()

    pokemon.value = data
    pokemon.value.name = capitalizeFirstLetter(pokemon.value.name)

    gifPath.value = new URL(data.sprites.other.showdown.front_default, import.meta.url).href
}
</script>

<style scoped>
.pokemon-details {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8rem;
    width: 100%;
    height: 100vh;

    img {
        width: 10%;
    }

    h1 {
        font-size: 34pt;
        font-style: italic;
    }
}

.pokemon-attributes {
    margin-bottom: 20px;

    p {
        margin: 5px 0;
        font-size: 24pt;
    }
}
</style>
