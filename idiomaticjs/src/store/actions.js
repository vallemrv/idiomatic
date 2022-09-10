import * as types from './mutations_type'
import * as API from '@/api'
import state from './state'

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
            console.log(r)
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
    }
}