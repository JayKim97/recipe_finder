import { AppBar, Typography,Button, Toolbar } from '@material-ui/core'
import { Link, useHistory, useLocation } from "react-router-dom"
import React, { useState, useEffect } from 'react'
import useStyles from './styles'
import {logout} from '../../actions/auth'
import {useDispatch} from 'react-redux'
import decode from 'jwt-decode'

const Navbar = () => {
  const classes = useStyles();
  const [user, setUser] = useState(JSON.parse(localStorage.getItem("profile")));
  const dispatch = useDispatch()
  const history = useHistory();

  const location = useLocation();

  const logoutHandler = (e) =>{
    e.preventDefault();
    dispatch(logout())
    history.push("/")
    setUser(null);
  }



  useEffect(() => {
    const token = user?.token;
    if (token){
      const decodedToken = decode(token);
      console.log(decodedToken.exp*1000)
      console.log(new Date().getTime())
      if (decodedToken.exp * 1000 < new Date().getTime()) dispatch(logout());
    }

    setUser(JSON.parse(localStorage.getItem("profile")))

  }, [location])

  return (
    <AppBar position="static" className={classes.appBar}>
      <div className={classes.title}>
        <Typography variant="h6" component={Link} to="/" color="inherit" style={{textDecoration:'none'}}>
          Recipe Finder
        </Typography>
      </div>
      <Toolbar className={classes.toolbar}>
        {user&&<Button component={Link} to="/addrecipe" color="inherit">Add Recipe</Button>}
        {user ?
          <Button color="secondary" onClick={logoutHandler}>Logout</Button>
          : <Button component={Link} to="/auth" color="inherit">Login</Button>
        }
      </Toolbar>
    </AppBar>
  )
}

export default Navbar
