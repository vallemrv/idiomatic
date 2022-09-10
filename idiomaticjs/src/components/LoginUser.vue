<template>
    <v-container>
        <v-card>
            <v-card-title > 
              <v-sheet class="pa-5" color="blue"> Registro </v-sheet> 
            </v-card-title>
            <v-card-text>
                <v-form>
                    <v-alert color="warning" v-if="alert!=''">{{alert}}</v-alert>
                    <v-text-field placeholder="Username"  variant="underlined" v-model="username" ></v-text-field>
                    <v-text-field placeholder="password"   variant="underlined" v-model="password" type="password"></v-text-field>
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="$router.push('registro')">Registrase</v-btn>
                <v-btn @click="login({username:username, password:password})">Aceptar</v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>


<script>
import { mapActions, mapState } from 'vuex'
export default{
data(){
    return {
        password:"",
        username:"",
        alert:"",
    }
},
computed:{
    ...mapState(["error", "ocupado"])
},
methods:{
    ...mapActions(["login"]),
   },
watch:{
    error(v){
        if (v){
            this.alert=v
        }else{
            this.alert = ""
        }
    },
}

}
</script>

<style scoped>
.v-card{
    width: 60%;
    margin-top: 5%;
    margin-left: auto;
    margin-right: auto;
}
@media (max-width: 1200px) {
.v-card{
    width: 90%;
}    
}
</style>