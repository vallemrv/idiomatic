import * as types from './mutations_type'

export default{
    [types.GET_REQUEST](state){
        state.ocupado = true
        state.error = null
    },
    [types.FAILURE](state, error){
        state.ocupado = false
        state.error = error
    },
    [types.SUSSCESS](state){
        state.ocupado = false
        state.error = null
    }

}