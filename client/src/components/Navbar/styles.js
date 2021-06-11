import { makeStyles } from '@material-ui/core/styles'

export default makeStyles((theme) => ({
  appBar:{
    display: "flex",
    flexDirection: "row",
    justifyContent: "space-between",
    padding: "0px 50px" ,
    alignItems: "center",
  },
  title:{
    display:"flex",
    alignItems:"center",
  },
  toolbar:{
    display: "flex",
    justifyContent: "flex-end",
    
  }
}))