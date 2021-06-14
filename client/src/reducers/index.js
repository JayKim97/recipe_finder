import {combineReducers} from 'redux'
import authReducer from './auth'
import recipesReducers from './recipes'
import currentIdReducer from './currentId'
import currentUserReducer from './currentUser'

export default combineReducers({
  auth: authReducer,
  recipes: recipesReducers,
  currentid: currentIdReducer,
  currentuser: currentUserReducer
})