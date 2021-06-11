import { Grid, TextField } from '@material-ui/core'
import React from 'react'

const Input = ({name, handleChange, label, half, type, value, row, multiline, optional}) => {
  return (
    <Grid item xs={12} sm={half? 6:12}>
      <TextField
        name={name}
        onChange={handleChange}
        label={label}
        fullWidth
        required={optional ? undefined : 'enabled'}
        value={value? value : undefined}
        type={type}
        multiline={multiline? 'enabled': undefined}
        rows={row}
      />
    </Grid>
  )
}

export default Input
