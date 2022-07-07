import axios from 'axios'

const apiClient = axios.create({
    baseURL: 'http://localhost:8000/',
    headers: {
        'Content-type': 'application/json;charset=utf-8',
        'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,PATCH,OPTIONS',
        'Access-Control-Allow-Origin': '*',
    },
})

const shorten = async (target_url: string) => {
    const response = await apiClient.post('/url', { target_url })
    return response.data
}

const ShortUrlService = {
    shorten,
}

export default ShortUrlService
