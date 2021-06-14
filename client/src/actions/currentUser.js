import { CURRENT_USER_SAVED, CURRENT_USER_LIKED } from "../constants/actionTypes";
import * as api from '../api'


export const getUserLiked = () => async(dispatch) =>{
  try {
    const {data} = await api.getUserLiked()
    dispatch({type: CURRENT_USER_LIKED, payload: data})
  } catch (error) {
    console.log(error)
  }
}

export const getUserSaved = () => async(dispatch) =>{
  try {
    const {data} = await api.getUserSaved()
    dispatch({type: CURRENT_USER_SAVED, payload: data})
  } catch (error) {
    console.log(error)
  }
}