import { createRouter, createWebHashHistory } from "vue-router"
import HomeView from "../views/HomeView.vue"

const routes = [
    {
        path: "",
        redirect: "/home"
    },
    {
        path: "/home",
        name: "home",
        component: HomeView
    },
    {
        path: "/pokemon/:name",
        name: "pokemon",
        component: () => import("../views/PokemonView.vue")
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
