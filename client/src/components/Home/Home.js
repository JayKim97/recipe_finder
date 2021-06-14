import { Grow, Container } from '@material-ui/core'
import React, {useEffect} from 'react'
import { useDispatch } from "react-redux";
import {getRecipes} from '../../actions/recipes'
import Recipes from '../Recipes/Recipes'


const Home = () => {
  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(getRecipes());
  }, [dispatch]);

  return (
    <Grow in>
      <Container>
        <Recipes/>
      </Container>
    </Grow>
  )
}

export default Home
