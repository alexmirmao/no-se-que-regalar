import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import {
  getAllProducts,
  getProductsByLikes,
  getProductsByCategoryId,
  getProductsByCategoryName,
  likeProduct,
  dislikeProduct,
} from "../api/products";
import ProductGrid from "../components/ProductGrid";

const ProductsPage = () => {
  const { type, value } = useParams(); // "type" puede ser "all", "likes", "categoryId", "categoryName"
  const [products, setProducts] = useState([]); // Inicializa como un array vacío
  const [loading, setLoading] = useState(true); // Indicador de carga
  const [error, setError] = useState(null); // Manejo de errores

  useEffect(() => {
    console.log("type:", type, "value:", value); // Verifica los parámetros
    const fetchProducts = async () => {
        setLoading(true);
        setError(null);
        try {
          let data = [];
          if (type === "all") { // Predeterminado a "all" si no hay "type"
            data = await getAllProducts();
          } else if (type === "likes") {
            data = await getProductsByLikes();
          } else if (type === "categoryId") {
            data = await getProductsByCategoryId(value);
          } else if (type === "categoryName") {
            data = await getProductsByCategoryName(value);
          }
          setProducts(Array.isArray(data) ? data : []);
        } catch (err) {
          console.error("Error fetching products:", err);
          setError("No se pudieron cargar los productos.");
        } finally {
          setLoading(false);
        }
      };

    fetchProducts();
  }, [type, value]);

  const handleLike = async (productId) => {
    try {
      await likeProduct(productId);
      setProducts((prev) =>
        prev.map((product) =>
          product.id === productId ? { ...product, likes: product.likes + 1 } : product
        )
      );
    } catch (err) {
      console.error("Error liking product:", err);
    }
  };

  const handleDislike = async (productId) => {
    try {
      await dislikeProduct(productId);
      setProducts((prev) =>
        prev.map((product) =>
          product.id === productId ? { ...product, likes: product.likes - 1 } : product
        )
      );
    } catch (err) {
      console.error("Error disliking product:", err);
    }
  };

  if (loading) {
    return <div>Cargando productos...</div>; // Mensaje de carga
  }

  if (error) {
    return <div>{error}</div>; // Muestra el mensaje de error
  }

  return (
    <div>
      <h1>Productos ({type})</h1>
      <ProductGrid products={products} onLike={handleLike} onDislike={handleDislike} />
    </div>
  );
};

export default ProductsPage;
