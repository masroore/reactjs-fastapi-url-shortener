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

    const handleText = (text) => {
        setTargetUrl(text)
    }

    const handleSubmit = (ev) => {
        if (isWebUri(targetUrl)) {
            /* TODO: send API, */
            postUrl()
        }
    }

    return (
        <Layout>
            <InputBox value={targetUrl} onChange={handleText} onSubmit={handleSubmit} />
            {shortUrl && <Preview target_url={targetUrl} short_url={shortUrl} />}
            <p>{targetUrl}</p>
        </Layout>
    )
}

export default App
