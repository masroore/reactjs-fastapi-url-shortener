import Layout from './containers/Layout'
import { useState, useEffect } from 'react'
import Preview from './components/Preview'
import InputBox from './components/InputBox'
import { isWebUri } from 'valid-url'
import ShortUrlService from './services/ShortUrl'
import { useMutation } from 'react-query'

function App() {
    const [targetUrl, setTargetUrl] = useState('')
    const [shortUrl, setShortUrl] = useState('')

    const { isLoading, mutate: postUrl } = useMutation(
        async () => {
            setShortUrl('')
            return await ShortUrlService.shorten(targetUrl)
        },
        {
            onSuccess: (response) => {
                setShortUrl(response.url)
            },
            onError: (err) => {
                setShortUrl('')
                console.log(err.response?.data || err)
            },
        }
    )

    useEffect(() => {
        if (isLoading) setShortUrl('')
    }, [isLoading])

    const handleText = (url) => {
        setShortUrl('')
        setTargetUrl(url)
    }

    const handleSubmit = () => {
        if (isWebUri(targetUrl)) {
            postUrl()
        }
    }

    return (
        <Layout>
            <InputBox value={targetUrl} onChange={handleText} onSubmit={handleSubmit} />
            {shortUrl && <Preview target_url={targetUrl} short_url={shortUrl} />}
        </Layout>
    )
}

export default App
