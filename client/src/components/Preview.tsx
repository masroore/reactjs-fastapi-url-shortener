import { CopyToClipboard } from 'react-copy-to-clipboard'
import { useState } from 'react'
import TinyLink from './TinyLink'

interface Props {
    target_url: string
    short_url: string
}
const Preview = ({ target_url, short_url }: Props) => {
    const [copied, setCopied] = useState<boolean>(false)

    return (
        <>
            <CopyToClipboard text={short_url} onCopy={() => setCopied(true)}>
                <span>Click to Copy: {short_url}</span>
            </CopyToClipboard>
            {copied ? <span style={{ color: 'red' }}>Copied.</span> : null}
            <TinyLink target_url={target_url} />
        </>
    )
}

export default Preview
