import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api', // Cambia esto por la URL de tu API Django
});

export default api;
