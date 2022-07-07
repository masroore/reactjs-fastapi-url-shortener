import CssBaseline from '@mui/material/CssBaseline'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Container from '@mui/material/Container'
import Footer from '../components/Footer'

type Props = {
    children: JSX.Element[] | JSX.Element
    footer: any
}

export default function Layout({ children, footer }: Props) {
    return (
        <Box
            sx={{
                display: 'flex',
                flexDirection: 'column',
                minHeight: '100vh',
            }}
        >
            <CssBaseline />

            <Container component='main' sx={{ mt: 8, mb: 2 }} maxWidth='sm'>
                <Typography variant='h2' component='h1' gutterBottom>
                    Shorty
                </Typography>
                <Typography variant='h5' component='h2' gutterBottom>
                    {'URL shortener made with Reactjs & FastAPI'}
                </Typography>
                <Typography variant='body1'>Sticky footer placeholder.</Typography>

                {children}
            </Container>

            <Footer {...footer} />
        </Box>
    )
}
