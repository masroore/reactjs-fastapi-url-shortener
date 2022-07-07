import Button from '@mui/material/Button'
import TextField from '@mui/material/TextField'
import Box from '@mui/material/Box'

interface Props {
    value: string
    onChange: (event: any) => void
    onSubmit: (event: any) => void
}

const InputBox = ({ value, onChange, onSubmit }: Props) => {
    const handleSubmit = (event: any) => {
        event.preventDefault()
        onSubmit(event)
    }

    return (
        <div>
            <Box sx={{ display: 'flex', flexWrap: 'wrap' }}>
                <form onSubmit={handleSubmit}>
                    <TextField
                        label='URL'
                        id='filled-size-small'
                        value={value}
                        sx={{ m: 1, width: '35ch' }}
                        onChange={(e) => onChange(e.target.value)}
                        variant='filled'
                    />

                    <Button variant='contained' disableElevation size='large' type='submit'>
                        Shorten
                    </Button>
                </form>
            </Box>
        </div>
    )
}

export default InputBox
