import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Container from '@mui/material/Container'
import Link from '@mui/material/Link'

function Copyright(props: any) {
    return (
        <Typography variant='body2' color='text.secondary' {...props}>
            {'Copyright © '}
            <Link color='inherit' target='_blank' href='https://github.com/masroore/reactjs-fastapi-url-shortener/'>
                Shorty
            </Link>
            {` ${new Date().getFullYear()}.`}
        </Typography>
    )
}
export default function Footer(props: any) {
    return (
        <Box
            component='footer'
            sx={{
                py: 3,
                px: 2,
                mt: 'auto',
                backgroundColor: (theme) =>
                    theme.palette.mode === 'light' ? theme.palette.grey[200] : theme.palette.grey[800],
            }}
        >
            <Container maxWidth='xl'>
                <Typography variant='body2'>Simple URL Shortener</Typography>
                <Copyright {...props} />
            </Container>
        </Box>
    )
}
