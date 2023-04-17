import {
    CARGO_LIST_REQUEST, 
    CARGO_LIST_SUCCESS, 
    CARGO_LIST_FAIL,

    CARGO_DETAILS_REQUEST, 
    CARGO_DETAILS_SUCCESS, 
    CARGO_DETAILS_FAIL
} from '../constants/cargoConstants'

export const cargoListReducer = (state = {cargos:[]}, action) => {
switch (action.type) {
    case CARGO_LIST_REQUEST:
        return {loading:true, cargos:[]}
    
    case CARGO_LIST_SUCCESS:
        return {loading:false, cargos:action.payload}
        
    case CARGO_LIST_FAIL:
        return {loading:false, error:action.payload}
            
                

    default:
        return state
}
}


export const cargoDetailsReducer = (state = {cargo:[] }, action) => {
switch (action.type) {
    case CARGO_DETAILS_REQUEST:
        return {loading:true, ...state}
    
    case CARGO_DETAILS_SUCCESS:
        return {loading:false, cargo:action.payload}
        
    case CARGO_DETAILS_FAIL:
        return {loading:false, error:action.payload}
            
                

    default:
        return state
}
}

