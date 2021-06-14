import {SET_CURRENT_ID} from '../constants/actionTypes'

export const setCurrentId = (id) => {
  return {
    type: SET_CURRENT_ID,
    payload: id
  }
}