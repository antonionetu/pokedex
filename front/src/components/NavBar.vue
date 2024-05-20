<template>
    <nav>
        <RouterLink to="/">Home</RouterLink>
    </nav>
</template>

<script>
export default {
    name: "NavBar"
}
</script>

<style scoped>
nav {
    background-color: #333;
    padding: 10px 40px;
    height: 6vh;

    a {
        color: #fff;
        text-decoration: none;
        font-size: 18pt;

        &:hover {
            text-decoration: underline;
        }
    }
}

.nav-link:hover {
    background-color: #555;
}
</style>
