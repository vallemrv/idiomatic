import axios from "axios"

const url_server = "http://localhost:8000/"

export const is_username_free = (params)=>{
        return axios.post(url_server+"is_username_free", params)
    }

export const registrarse = (params) =>{
      return axios.post(url_server+"registrarse", params)
}