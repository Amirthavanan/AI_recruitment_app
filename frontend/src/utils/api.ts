import axios from "axios";


console.log(import.meta.env);
console.log(import.meta.env.VITE_API_BASE_URL);
console.table(import.meta.env);


const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
    headers: {
        "Content-Type": "application/json",
    },
});

api.interceptors.request.use((config) => {
    console.log("Calling:", config.baseURL + config.url);

    const token = localStorage.getItem("access_token");

    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
});

api.interceptors.request.use((config) => {
    console.log("Request URL:", config.baseURL + config.url);

    const token = localStorage.getItem("access_token");

    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
});

export default api;