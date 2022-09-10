import axios from "axios"

const url_server = "http://localhost:8000/"

export default {
    is_username_free: (params)=>{
        return axios.post(url_server+"is_username_free", params)
    },
    registrarse: (params) =>{
        return axios.post(url_server+"registrarse", params)
    },
    login: (params) =>{
        return axios.post(url_server+"token/new.json", params)
    }
} 

