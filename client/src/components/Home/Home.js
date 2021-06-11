import { Grow } from '@material-ui/core'
import React, {useEffect} from 'react'
import { useDispatch, useSelector } from "react-redux";
import {getRecipes} from '../../actions/recipes'


const Home = () => {
  const recipes = useSelector(state => state.recipes)
  const dispatch = useDispatch()
  useEffect(() => {
    dispatch(getRecipes())
    console.log(recipes)
  }, [])

  return (
    <Grow in>
      <div>home</div>
    </Grow>
  )
}

export default Home
