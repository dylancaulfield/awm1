import axios from "axios";
import state from "@/store"


export async function get(url) {

    const response = await axios.get(url, {
        withCredentials: true
    });
    return response.data;

}

export async function post(url, data) {

    const response = await axios.post(
        url,
        data,
        {
            headers: {
                "X-CSRFToken": state.state.csrf
            },
            withCredentials: true
        }
    )
    return response.data;

}