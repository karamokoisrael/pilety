import React from 'react'
import {Card} from 'react-bootstrap'
import { Link } from 'react-router-dom'

import Rating from './Rating'

// function Product({product}) {
//   return (
//     <Card className='my-3 p-3 rounded'>
//       <Link to={`/api/merch_detail/${product.id}/`}>
 
//         <Card.Img src={product.images.map(image=> image.image)[0]} /> 
        
//       </Link>

//       <Card.Body>
//         <Link to={`/api/merch_detail/${product.id}/`}>
          
//           <Card.Title as='div'>
//             <strong>{product.name}</strong>
//           </Card.Title> 
//         </Link>
//         <Card.Text as='div'>
//           <div className='my-3'>
//           </div>
        
//         </Card.Text>
//         <Card.Text as='h3'>
//         ¥{product.price}
        
          
          
//         </Card.Text>
//         {/* <Rating value={product.ratings}  color='gold' text={
//           product.review >1
//               ? `${product.review} Reviews`
//               :  `${product.review} Review`} /> */}

        
      
//       </Card.Body>      
//     </Card>
    

//   )
// }

// export default Product

// import React from 'react';

// Example product data
const products = [
  {
    id: 1,
    name: 'Product 1',
    price: 10.99,
    image: 'https://via.placeholder.com/150',
  },
  {
    id: 2,
    name: 'Product 2',
    price: 19.99,
    image: 'https://via.placeholder.com/150',
  },
  {
    id: 3,
    name: 'Product 3',
    price: 5.99,
    image: 'https://via.placeholder.com/150',
  },
  {
    id: 4,
    name: 'Product 4',
    price: 15.99,
    image: 'https://via.placeholder.com/150',
  },
  {
    id: 5,
    name: 'Product 5',
    price: 8.99,
    image: 'https://via.placeholder.com/150',
  },
  {
    id: 6,
    name: 'Product 6',
    price: 12.99,
    image: 'https://via.placeholder.com/150',
  },
];

const ProductGrid = () => {
  return (
    <div className="product-grid">
      {products.map((product) => (
        <div key={product.id} className="product-grid-item">
          <img src={product.image} alt={product.name} />
          <div className="product-name">{product.name}</div>
          <div className="product-price">${product.price.toFixed(2)}</div>
          <button>Add to Cart</button>
        </div>
      ))}
    </div>
  );
};

export default ProductGrid;

