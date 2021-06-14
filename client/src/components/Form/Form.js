import { Button, Container, Grow, Paper, Typography,TextField } from '@material-ui/core'
import React, { useState } from 'react'
import { useEffect } from 'react'
import { useDispatch,useSelector } from 'react-redux'
import { useHistory,useLocation } from 'react-router-dom'
import {createRecipe, editRecipe} from '../../actions/recipes'
import { setCurrentId } from '../../actions/currentId'
import Input from '../Input/Input'



const Form = () => {
  // const initialState={
  //   title:"",
  //   link:"",
  //   instruction:"",
  //   category:"",
  //   tags:"",
  //   ingredients:""
  // }
  const dispatch = useDispatch()
  const location = useLocation();


  const currentId = useSelector(state => state.currentid)
  const recipe = useSelector(state=> currentId? state.recipes.find((r)=> r.id===currentId): null)
  const [recipeData, setRecipeData] = useState(recipe ? {title: recipe.title, link: recipe.link, instruction: recipe.instruction} : {
    title:"",
    link:"",
    instruction:"",
    category:"",
    tags:"",
    ingredients:""
  })
  
  const history = useHistory()


  const handleSubmit = (e) =>{
    e.preventDefault()
    if (currentId){
      dispatch(editRecipe(currentId, recipeData))
    } else {
      dispatch(createRecipe(recipeData))
    }
    // dispatch(setCurrentId(null))
    history.push('/')
  }

  const handleChange = (e) =>{
    setRecipeData({...recipeData, [e.target.name]: e.target.value})
  }

  useEffect(() => {
    
    return () => {
      dispatch(setCurrentId(null))
    }
  }, [])


  return (
    <Grow in>
      <Container>
        <Paper elevation={3}>
          <Typography variant="h5">
            Add Recipe
          </Typography>
          <form onSubmit={handleSubmit}>
            <Input name="title" value={recipeData.title} label="Title" fullWidth handleChange={handleChange}/>
            <Input name="link" value={recipeData.link} label="Image Link" fullWidth type="url" handleChange={handleChange}/>
            {location.pathname === '/edit' ? null : 
                  <>
                    <Input name="category" value={recipeData.category} label="Category" fullWidth handleChange={handleChange}/>
                    <Input name="tags" value={recipeData.tags} label="Tags(seperate with comma)" fullWidth handleChange={handleChange}/>
                    <Input name="ingredients" value={recipeData.ingredients} label="Ingredients (seperate with comma)" fullWidth handleChange={handleChange}/>
                  </>
                  }
            <TextField
                name="instruction"
                label="Instruction"
                fullWidth
                required
                value={recipeData.instruction}
                multiline
                rows={4}
                onChange={handleChange}
              />
            <Button type="submit" fullWidth variant="contained" color="primary">Submit</Button>
          </form>
        </Paper>
      </Container>
    </Grow>
  )
}

export default Form
