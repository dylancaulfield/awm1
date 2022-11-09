<template>
    <div>

        <v-container>

            <p v-show="!this.user.email">
                <router-link to="/login">Login to save locations to your account</router-link>
            </p>

            <p>Click on the map to save a location</p>

            <LMap @click="savePosition" ref="map" style="width: 100%; height: 300px" :zoom="zoom" :center="center">
                <LTileLayer :url="url" :attribution="attribution"></LTileLayer>
            </LMap>

            <v-card class="mt-6"  :key="i" v-for="(location, i) in locations">
                <v-list>
                    <v-list-item>
                        <v-list-item-content>
                            <v-list-item-title>Location</v-list-item-title>
                            <v-list-item-subtitle>{{location.latitude}}</v-list-item-subtitle>
                            <v-list-item-subtitle>{{location.longitude}}</v-list-item-subtitle>
                            <v-list-item-subtitle>Created: {{location.created}}</v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-list>
            </v-card>


        </v-container>

    </div>
</template>

<script>
//import L from "leaflet"
import {LMap, LTileLayer} from "vue2-leaflet"
import {mapState, mapActions} from "vuex";


export default {
    name: 'Home',
    components: {
        LMap,
        LTileLayer,
        //LMarker
    },
    data(){
        return {
            url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
            attribution:
                '&copy; <a target="_blank" href="http://osm.org/copyright">OpenStreetMap</a> contributors',
            zoom: 10,
            center: [53.3498, 6.2603]
        }
    },
    methods: {

        savePosition(event){

            const location = {
                latitude: event.latlng.lat,
                longitude: event.latlng.lng,
                created: new Date().toLocaleDateString()
            };

            this.addLocation(location)

        },

        ...mapActions({
            addLocation: "addLocation"
        })
    },
    computed: mapState({
        locations: state => state.locations,
        user: state => state.user
    })
}
</script>
