import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/manage_products/products/';

// Obtener todos los productos
export const getAllProducts = async () => {
  const response = await axios.get(API_BASE_URL);
  console.log(response.data);
  return response.data;
};

// Obtener productos ordenados por likes
export const getProductsByLikes = async () => {
  const response = await axios.get(`${API_BASE_URL}order-by-likes`);
  return response.data;
};

// Obtener productos por categoría (ID)
export const getProductsByCategoryId = async (categoryId) => {
  const response = await axios.get(`${API_BASE_URL}by-category/${categoryId}`);
  return response.data;
};

// Obtener productos por categoría (nombre)
export const getProductsByCategoryName = async (categoryName) => {
  const response = await axios.get(`${API_BASE_URL}by-category-name/${categoryName}`);
  return response.data;
};

// Dar like a un producto
export const likeProduct = async (productId) => {
  const response = await axios.put(`${API_BASE_URL}${productId}/like`);
  return response.data;
};

// Quitar like de un producto
export const dislikeProduct = async (productId) => {
  const response = await axios.put(`${API_BASE_URL}${productId}/dislike`);
  return response.data;
};