<template>
    <form @submit.prevent="searchPokemon">
        <input v-model="pokemonName" placeholder="Type Pokemon's Name" />
        <button type="submit">Search</button>
    </form>
</template>

<script>
export default {
    data() {
        return {
            pokemonName: ""
        }
    },
    methods: {
        searchPokemon() {
            this.$router.push(`/pokemon/${this.pokemonName}`)
        }
    }
}
</script>

<style>
form {
    display: flex;
    flex-direction: column;
    height: 94vh;
    justify-content: center;
    align-items: center;
    gap: 2rem;

    input {
        padding: 1rem 4rem;
        text-align: center;
        border-radius: 15px;
        border: 0px;
        font-size: 24pt;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);

        &:focus {
            outline: none;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }
    }

    button {
        border: none;
        padding: 1rem 2rem;
        font-size: 18pt;
        border-radius: 15px;
        cursor: pointer;
        transition: 0.3s;

        &:hover {
            background-color: rgb(143, 226, 143);
        }
    }
}
</style>
