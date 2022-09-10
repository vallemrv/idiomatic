<template>
    <v-container>
        <v-card>
            <v-card-title > 
              <v-sheet class="pa-5" color="blue"> Registro </v-sheet> 
            </v-card-title>
            <v-card-text>
                <v-form>
                    <v-alert color="warning" v-if="alert!=''">{{alert}}</v-alert>
                    <v-text-field placeholder="Username"  variant="underlined" v-model="username" @focusout="exit_username()"></v-text-field>
                    <v-text-field placeholder="Nombre"  variant="underlined" v-model="nombre"></v-text-field>
                    <v-text-field placeholder="Apellido"  variant="underlined" v-model="apellido"></v-text-field>
                    <v-text-field placeholder="email" variant="underlined" v-model="email" type="email"></v-text-field>
                    <v-text-field placeholder="password"   variant="underlined" v-model="password" type="password"></v-text-field>
                    <v-text-field placeholder="Repetir password"  variant="underlined" v-model="re_pass" type="password"></v-text-field>
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn @click="$router.back()">Cancelar</v-btn>
                <v-btn @click="enviar()">Aceptar</v-btn>
            </v-card-actions>
        </v-card>
    </v-container>
</template>


<script>
import { mapActions, mapState } from 'vuex'
export default{
data(){
    return {
        nombre:"",
        apellido:"",
        email:"",
        password:"",
        username:"",
        re_pass:"",
        alert:"",
    }
},
computed:{
    ...mapState(["error", "ocupado", "user"])
},
methods:{
    ...mapActions(["is_username_free", "registrarse"]),
    exit_username(){
        if (this.username == "") this.alert="Tiene que ser un usuario valido"
        else{
            this.alert = ""
            let p = new FormData()
            p.append("username", this.username)
            this.is_username_free(p)
        }
    },
    enviar(){
        if(this.password == "" || this.password != this.re_pass){
            this.alert = "Contraseñas no validas o no son iguales."
        }else{
            let p = new FormData();
            p.append("username", this.username);
            p.append("nombre", this.nombre);
            p.append("apellido", this.apellido);
            p.append("email", this.email);
            p.append("password", this.password);
            this.registrarse(p);
        }
     }
   },
watch:{
    error(v){
        if (v){
            this.alert=v
        }else{
            this.alert = ""
        }
    },
    user(v){
        if(v){
            this.$router.back();
        }
    }
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