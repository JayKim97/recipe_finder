import {combineReducers} from 'redux'
import authReducer from './auth'
import recipesReducers from './recipes'

export default combineReducers({
  auth: authReducer,
  recipes: recipesReducers
})