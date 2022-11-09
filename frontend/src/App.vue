<template>
    <v-app>
        <v-app-bar
            app
            color="primary"
            dark
            hide-on-scroll
        >

            <router-link class="white--text" style="text-decoration: none" to="/">
                <v-app-bar-title>AWM1</v-app-bar-title>
            </router-link>


            <v-spacer></v-spacer>


        </v-app-bar>

        <v-main>
            <router-view/>
        </v-main>
    </v-app>
</template>

<script>
import store from "@/store";


export default {
    name: 'App',

    data: () => ({
        //
    }),

    beforeMount() {

        store.dispatch("getCsrf")
        store.dispatch("fetchLocations")

    }

};
</script>

<style>

.max-width {
    max-width: 800px;
}

</style>
