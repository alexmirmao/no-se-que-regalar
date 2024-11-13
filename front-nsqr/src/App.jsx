import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ProductsPage from './pages/ProductsPage';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/products" element={<ProductsPage type="all" />} />
        <Route path="/products/likes" element={<ProductsPage type="likes" />} />
        <Route path="/products/category/id/:value" element={<ProductsPage type="categoryId" />} />
        <Route path="/products/category/name/:value" element={<ProductsPage type="categoryName" />} />
      </Routes>
    </Router>
  );
};

export default App;
