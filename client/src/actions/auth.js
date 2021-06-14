import { AUTH, LOGOUT } from '../constants/actionTypes'
import * as api from '../api'

export const signup = (formData, history) => async (dispatch) => {
  try {
    const {data} = await api.signup(formData)
    dispatch({type: AUTH, payload: data})
    history.push("/")
  } catch (error) {
    return error.response.data.message
  }
}

export const signin = (formData, history) => async (dispatch) =>{
  try{
    const { data } = await api.signin(formData)
    dispatch({type: AUTH, payload:data})
    history.push("/")
  } catch (error) {
    console.log(error.response.data.message)
  }
}

export const logout = () => {
  return {type:LOGOUT}
}