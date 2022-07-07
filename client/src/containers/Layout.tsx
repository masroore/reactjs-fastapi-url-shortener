import CssBaseline from '@mui/material/CssBaseline'
import Box from '@mui/material/Box'
import Typography from '@mui/material/Typography'
import Container from '@mui/material/Container'
import Footer from '../components/Footer'
import { createTheme, ThemeProvider } from '@mui/material/styles'

type Props = {
    children: JSX.Element[] | JSX.Element
    footer: any
}
const theme = createTheme()

export default function Layout({ children, footer }: Props) {
    return (
        <ThemeProvider theme={theme}>
            <Container component='main' maxWidth='md'>
                <CssBaseline />
                <Box
                    sx={{
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                        minHeight: '88vh',
                    }}
                >
                    <Container component='main' sx={{ mt: 6 }}>
                        <Typography variant='h2' component='h1' gutterBottom>
                            Shorty
                        </Typography>
                        <Typography variant='h5' component='h2' gutterBottom>
                            {'URL shortener made with Reactjs & FastAPI'}
                        </Typography>

                        {children}
                    </Container>
                </Box>
            </Container>
            <Footer {...footer} />
        </ThemeProvider>
    )
}
