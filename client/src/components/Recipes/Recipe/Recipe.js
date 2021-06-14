import React, {useEffect,useState} from 'react'
import {useSelector} from 'react-redux'
import {Card, CardHeader, IconButton, Avatar, CardMedia, CardActions, Typography, CardContent} from '@material-ui/core';
import {MoreVert} from '@material-ui/icons';
import moment from 'moment'
import ThumbUpAltIcon from '@material-ui/icons/ThumbUpAlt';
import ThumbDownAltIcon from '@material-ui/icons/ThumbDownAlt';
import BookmarkBorderIcon from '@material-ui/icons/BookmarkBorder';
import useStyles from './styles';

import { Link, useHistory, useLocation } from "react-router-dom"
import { useDispatch } from 'react-redux'
import { likeRecipe, dislikeRecipe, saveRecipe} from '../../../actions/recipes'
import {setCurrentId} from '../../../actions/currentId'

const Recipe = ({recipe}) => {
  const classes = useStyles(); 
  const [rating, setRating] = useState(0)
  const currentuser = useSelector(state => state.currentuser)
  const [userLiked, setUserLiked] = useState(currentuser.liked.find(like => like === recipe.id) ? true : false)
  const [userSaved, setUserSaved] = useState(currentuser.saved.find(save => save === recipe.id) ? true : false)
  const dispatch = useDispatch();
  const user = JSON.parse(localStorage.getItem("profile"));
  

  useEffect(() => {
    const calculateRating = () =>{
      if (recipe.num_likes === 0 && recipe.num_dislike === 0){
        return 0
      }
      if (recipe.num_likes === 0){
         return (recipe.num_dislike/(recipe.num_likes+recipe.num_dislike)) * -100
      } else {
        return (recipe.num_likes/(recipe.num_likes+recipe.num_dislike)) * 100
      }
    }
    setRating(calculateRating().toFixed())
  }, [recipe.num_likes,recipe.num_dislike])



  return (
    <Card className={classes.root}>
      <CardHeader
        avatar={<Avatar className={classes.avatar}>
          {recipe.creator_name[0].toUpperCase()}
        </Avatar>}
        action={
          <IconButton component={Link} to="/edit" aria-label="settings" onClick={()=>dispatch(setCurrentId(recipe.id))}>
            <MoreVert />
          </IconButton>
        }
        title={recipe.title}
        subheader={moment(recipe.created_at).fromNow()}
      />
      <CardMedia
        className={classes.media}
        image={recipe.link}
        title="Paella dish"
      />
      <CardActions disableSpacing>
        <Typography>
          {rating}%
        </Typography>
        <IconButton 
          color="primary" 
          onClick={()=>dispatch(likeRecipe(recipe.id))}
          disabled={!user?.result}>
          <ThumbUpAltIcon/>
        </IconButton>
        <IconButton
          color="primary" 
          onClick={()=>dispatch(dislikeRecipe(recipe.id))}
          disabled={!user?.result}>
          <ThumbDownAltIcon/>
        </IconButton>
        <IconButton  className={classes.save} onClick={()=>dispatch(saveRecipe(recipe.id))}>
          <BookmarkBorderIcon/>
        </IconButton>
      </CardActions>
    </Card>
  )
}

export default Recipe
