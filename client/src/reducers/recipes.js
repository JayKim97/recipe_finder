import {GET_ALL, CREATE, GET_ITEM, EDIT, LIKE, DISLIKE, SAVE, DELETE} from '../constants/actionTypes'

const recipesReducers = (recipes=[], action) => {
  switch(action.type){
    case GET_ALL:
      return action.payload
    case CREATE:
      return [...recipes, action.payload]
    case GET_ITEM:
      return recipes
    case EDIT:
    case LIKE:
    case DISLIKE:
      return recipes.map((recipe)=> recipe.id===action.payload.id ? action.paylod: recipe);
    case SAVE:
      return recipes
    case DELETE:
      return recipes.map((recipe) => recipe.id !==action.payload.id )
    default: return recipes
  }
}

export default recipesReducers