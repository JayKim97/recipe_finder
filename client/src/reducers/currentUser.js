import {CURRENT_USER_SAVED, CURRENT_USER_LIKED} from '../constants/actionTypes'

const currentUserReducer = (state={},action)=>{
  switch(action.type){
    case CURRENT_USER_SAVED:
      return {...state, saved: action.payload}
    case CURRENT_USER_LIKED:
      return {...state, liked: action.payload}
    default: return state
  }
}

export default currentUserReducer