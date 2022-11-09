<template>
<div>

    <v-container class="max-width">

        <v-card>

            <v-card-text>

                <v-form ref="loginForm" class="pt-4">

                    <h1 class="mb-6">Login</h1>

                    <v-divider class="mb-6"></v-divider>

                    <v-text-field required filled label="Email" v-model="user.username" :rules="[v => !!v || 'Email is required']"></v-text-field>
                    <v-text-field required filled type="password" label="Password" v-model="user.password" :rules="[v => !!v || 'Password is required']"></v-text-field>

                    <v-btn @click="login" color="primary" >Login</v-btn>

                </v-form>

            </v-card-text>



        </v-card>



    </v-container>

</div>
</template>

<script>
import store from "@/store";


export default {
    name: "Login",
    data(){
        return {
            user: {}
        }
    },
    methods:{

        login(){

            if(!this.$refs.loginForm.validate()){
                return;
            }

            store.dispatch("login", this.user)

        }

    }
}
</script>

<style scoped>

</style>