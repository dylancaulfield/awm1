import Vue from 'vue'
import Vuex from 'vuex'
import {get, post} from "@/utilities/request";
import router from "@/router";

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        csrf: String,
        user: {},
        locations: []
    },
    mutations: {

        setCsrf(state, token){
            state.csrf = token
        },

        setUser(state, user){
            state.user = user
        },

        addLocation(state, location){
            state.locations.push(location)
        }

    },
    actions: {

        async fetchLocations(context){

            const locations = await get("/api/places");

            for(let location of locations){
                context.commit("addLocation", location)
            }

        },

        async getCsrf(context){

            const data = await get("/api/auth/csrf");
            context.commit("setCsrf", data)

        },

        async login(context, user){

            const response = await post("/api/auth/login", {
                username: user.username,
                password: user.password
            })
            context.commit("setUser", response);
            await router.push("/")
            await context.dispatch("fetchLocations");

        },

        async logout(context){

            await post("/api/auth/logout", {});
            context.commit("setUser", {});
            await router.push("/")

        },

        async addLocation(context, location){

            context.commit("addLocation", location);

            if (!context.state.user.username){
                return;
            }

            await post("/api/places/create", {
                latitude: location.latitude,
                longitude: location.longitude,
                name: location.name
            });

        },

    },
    modules: {}
})
