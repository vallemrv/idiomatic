import * as types from './mutations_type'
import  API from '@/api'

export default{
    is_username_free({commit}, params){
        commit(types.GET_REQUEST)
        API.is_username_free(params).then((r) =>{
            let res = r.data
            if(res.susscess){
                commit(types.SUSSCESS, res.alert)
            }else{
                commit(types.FAILURE, res.errors);
            }
         }
        ).catch((error)=>{
            commit(types.FAILURE, error);
        })
    },
    registrarse({commit}, params){
        commit(types.GET_REQUEST)
        API.registrarse(params).then((r)=>{
            let res = r.data
            if(res.susscess){
                commit(types.SUSSCESS, res.alert)
            }else{
                commit(types.FAILURE, res.errors);
            }

        }).catch((error)=>{
            commit(types.FAILURE, error);
        })
    },
    login({commit, state}, {username, password}){
        commit(types.GET_REQUEST)
        let p = new FormData()
        p.append("username", username)
        p.append("password", password)
        API.login(p).then((r)=>{
            let res = r.data
            if(res.susscess){
                commit(types.SUSSCESS, null);
                state.user = res.token;
                localStorage.setItem("user", res.token);
            }else{
                commit(types.FAILURE, res.errors);
            }

        }).catch(()=>{
            commit(types.FAILURE, "Credenciales no validas");
        })

    }
}