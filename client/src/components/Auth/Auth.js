import { Button, Container, Grid, Grow, Paper, Typography } from '@material-ui/core'
import React, {useState} from 'react'
import Input from '../Input/Input'
import {useDispatch} from 'react-redux'
import {useHistory} from 'react-router-dom'
import {signup,signin} from '../../actions/auth'


const Auth = () => {
  const initialState = {
    firstName:"",
    lastName:"",
    email:"",
    password:"",
    confirmPassword:"",
  }
  const [formData, setFormData] = useState(initialState)
  const [isSignUp, setIsSignUp] = useState(false)
  
  const dispatch = useDispatch();
  const history = useHistory();

  const handleSubmit = (e) =>{
    e.preventDefault();
    if(isSignUp){
      dispatch(signup(formData, history))
    } else {
      dispatch(signin(formData, history))
    }
  }

  const handleChange = (e) =>{
    setFormData({...formData, [e.target.name]: e.target.value})
  }

  const switchMode = () =>{
    setIsSignUp((prevState) => !prevState)
  }

  return (
    <Grow in>
      <Container>
        <Paper elevation={3}>
          <Typography variant="h5">
            {isSignUp? "Sign Up" : "Login"}
          </Typography>
          <form onSubmit={handleSubmit}>
            <Grid container spacing={2}>
            {isSignUp ? 
              <>
                <Input
                  name="firstName"
                  label="First Name"
                  handleChange={handleChange}
                  half
                />
                <Input
                  name="lastName"
                  label="Last Name"
                  handleChange={handleChange}
                  half
                />
              </> : null
              }
              <Input
                name="email"
                label="Email"
                handleChange={handleChange}
                type="email"
              />
              <Input
                name="password"
                label="Password"
                handleChange={handleChange}
                type="password"
              />
              {isSignUp? 
              <Input
                name="confirmPassword"
                label="Confirm Password"
                handleChange={handleChange}
                type="password"
              />:null
              }
            </Grid>
            <Button type="submit" fullWidth variant="contained" color="primary">{isSignUp ? "Sign Up" : "Sign In"}</Button>
            <Grid container justify="flex-end">
              <Grid item>
                <Button onClick={switchMode}>
                  {isSignUp
                    ? "Already have an account? Sign In"
                    : "Don't have an account? Sign Up"}
                </Button>
              </Grid>
            </Grid>
          </form>
        </Paper>
      </Container>
    </Grow>
  )
}

export default Auth
