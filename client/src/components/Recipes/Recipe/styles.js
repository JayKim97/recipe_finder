import { makeStyles } from '@material-ui/core/styles';
import { red } from '@material-ui/core/colors';

export default makeStyles({
  root: {
    maxWidth: 345,
  },
  media: {
    height: 0,
    paddingTop: '56.25%', // 16:9
  },
  save: {
    marginLeft: 'auto'
  },
  avatar: {
    backgroundColor: red[500],
  },
  rating:{
    transform: 'translateY(10%)'
  }
});