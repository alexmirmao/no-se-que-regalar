import React from 'react';

const ProductGrid = ({ products = [], onLike, onDislike }) => {
  return (
    <div style={{ display: 'flex', flexWrap: 'wrap', gap: '1rem' }}>
      {products.map((product) => (
        <div key={product.product_id} style={{ flex: '1 1 calc(33.333% - 1rem)', border: '1px solid #ccc', padding: '1rem' }}>
          <h3>{product.product_name}</h3>
          <p>{product.description}</p>
          <p>Likes: {product.likes}</p>
          <button onClick={() => onLike(product.id)}>Like</button>
          <button onClick={() => onDislike(product.id)}>Dislike</button>
        </div>
      ))}
    </div>
  );
};

export default ProductGrid;
