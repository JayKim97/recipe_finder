import {GET_ALL, CREATE, GET_ITEM, EDIT, LIKE, DISLIKE, SAVE, DELETE} from '../constants/actionTypes'
import * as api from '../api'

export const getRecipes = () => async(dispatch)=>{
  try {
    const {data} = await api.getRecipes()
    dispatch({type: GET_ALL, payload: data})
  } catch (error) {
    console.log(error)
  }
}

export const createRecipe = (formData) => async(dispatch)=>{
  try {
    const { data } = await api.createRecipe(formData)
    dispatch({type: CREATE, payload: data})
  } catch (error) {
    console.log(error)
  }
}

export const getItem = (id) => async(dispatch)=>{
  try {
    const {data} = await api.getRecipe(id)
    dispatch({type: GET_ITEM, payload: data})
  } catch (error) {
    console.log(error)
  }
}

export const editRecipe = (id, formData) => async(dispatch)=>{
  try {
    const {data} = await api.editRecipe(id, formData)
    dispatch({type: EDIT, payload: data})
  } catch (error) {
    console.log(error)
  }
}

export const likeRecipe = (id) => async(dispatch)=>{
  try {
    const {data} = await api.likeRecipe(id)
    dispatch({type: LIKE, payload: data})
  } catch (error) {
    console.log(error)
  }
}

export const dislikeRecipe = (id) => async(dispatch)=>{
  try {
    const {data} = await api.dislikeRecipe(id)
    dispatch({type: DISLIKE, payload: data})
  } catch (error) {
    console.log(error)
  }
}

export const saveRecipe = (id) => async(dispatch)=>{
  try {
    const {data} = await api.saveRecipe(id)
    dispatch({type: SAVE, payload: data})
  } catch (error) {
    console.log(error)
  }
}

export const deleteRecipe = (id) => async(dispatch)=>{
  try {
    const {data} = await api.deleteRecipe(id)
    dispatch({type:DELETE, payload: data})
  } catch (error) {
    console.log(error)
  }
}
