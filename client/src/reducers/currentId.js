import {SET_CURRENT_ID} from '../constants/actionTypes'


const currentIdReducer = (state={}, action)=>{
  switch(action.type){
    case SET_CURRENT_ID:
      state = action.payload
      return state
    default: return state
  }
}

export default currentIdReducer