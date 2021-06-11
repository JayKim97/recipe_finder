import { Button, Container, Grow, Paper, Typography } from '@material-ui/core'
import React, { useState } from 'react'
import { useDispatch } from 'react-redux'
import { useHistory } from 'react-router-dom'
import {createRecipe} from '../../actions/recipes'
import Input from '../Input/Input'



const Form = () => {
  const initialState={
    title:"",
    link:"",
    instruction:""
  }
  const dispatch = useDispatch()

  const [recipeData, setRecipeData] = useState(initialState)

  const history = useHistory()


  const handleSubmit = (e) =>{
    e.preventDefault()
    dispatch(createRecipe(recipeData))
    history.push('/')
  }

  const handleChange = (e) =>{
    setRecipeData({...recipeData, [e.target.name]: e.target.value})
  }


  return (
    <Grow in>
      <Container>
        <Paper elevation={3}>
          <Typography variant="h5">
            Add Recipe
          </Typography>
          <form onSubmit={handleSubmit}>
            <Input name="title" value={recipeData.title} label="Title" fullWidth handleChange={handleChange}/>
            <Input name="link" value={recipeData.link} label="Link (optional)" fullWidth type="url" handleChange={handleChange} optional/>
            <Input name="instruction" value={recipeData.instruction} label="Instruction" multiline row={4} fullWidth handleChange={handleChange}/>
            <Button type="submit" fullWidth variant="contained" color="primary">Submit</Button>
          </form>
        </Paper>
      </Container>
    </Grow>
  )
}

export default Form
