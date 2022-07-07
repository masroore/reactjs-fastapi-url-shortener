import { ReactTinyLink } from 'react-tiny-link'

const TinyLink = ({ target_url }) => {
    return (
        <>
            {target_url ? (
                <ReactTinyLink cardSize='small' showGraphic={true} maxLine={2} minLine={1} url={target_url} />
            ) : null}
        </>
    )
}

export default TinyLink
