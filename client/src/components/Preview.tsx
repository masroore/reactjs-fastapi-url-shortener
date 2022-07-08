import { CopyToClipboard } from 'react-copy-to-clipboard'
import { useState } from 'react'
import TinyLink from './TinyLink'
import Button from '@mui/material/Button'

interface Props {
    target_url: string
    short_url: string
}
const Preview = ({ target_url, short_url }: Props) => {
    const [copied, setCopied] = useState<boolean>(false)

    return (
        <>
            <p>{short_url}</p>
            <CopyToClipboard text={short_url} onCopy={() => setCopied(true)}>
                <Button variant='contained' disableElevation>
                    Copy URL to Clipboard
                </Button>
            </CopyToClipboard>{' '}
            {copied && <span style={{ color: 'red' }}>Copied.</span>}
            <TinyLink target_url={target_url} />
        </>
    )
}

export default Preview
