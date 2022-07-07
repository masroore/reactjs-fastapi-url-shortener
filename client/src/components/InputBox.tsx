import * as React from 'react'
import Button from '@mui/material/Button'
import TextField from '@mui/material/TextField'
import Box from '@mui/material/Box'

interface Props {
    value: string
    onChange: (url: string) => void
    onSubmit: () => void
}

const InputBox = ({ value, onChange, onSubmit }: Props) => {
    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault()
        onSubmit()
    }

    return (
        <>
            <Box component='form' onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
                <TextField
                    margin='normal'
                    required
                    fullWidth
                    autoFocus
                    label='URL'
                    id='url'
                    value={value}
                    onChange={(e: any) => onChange(e.target.value)}
                />

                <Button type='submit' fullWidth variant='contained' sx={{ mt: 0, mb: 3 }} disableElevation>
                    Shorten
                </Button>
            </Box>
        </>
    )
}

export default InputBox
