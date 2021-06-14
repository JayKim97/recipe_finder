import React from 'react'
import {useSelector} from "react-redux";
import { CircularProgress, Grid } from '@material-ui/core';
import Recipe from './Recipe/Recipe';

const Recipes = () => {
  const recipes = useSelector(state => state.recipes)
  return !recipes.length ? (
    <CircularProgress/>
  ) : (
    <Grid container alignItems="stretch" spacing={3}>
      {recipes.map((recipe)=> (
        <Grid key={recipe.id} item xs={12} sm={4}>
          <Recipe recipe={recipe}/>
        </Grid>
      ))}
    </Grid>
  )
}

export default Recipes
