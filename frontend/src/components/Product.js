import React from 'react'
import {Card} from 'react-bootstrap'
import { Link } from 'react-router-dom'

import Rating from './Rating'

function Product({product}) {
  return (
    <Card className='my-3 p-3 rounded'>
      <Link to={`/api/merch_detail/${product.id}/`}>
 
        <Card.Img src={product.images.map(image=> image.image)[0]} /> 
        
      </Link>

      <Card.Body>
        <Link to={`/api/merch_detail/${product.id}/`}>
          
          <Card.Title as='div'>
            <strong>{product.name}</strong>
          </Card.Title> 
        </Link>
        <Card.Text as='div'>
          <div className='my-3'>
          </div>
        
        </Card.Text>
        <Card.Text as='h3'>
        ¥{product.price}
        
          
          
        </Card.Text>
        {/* <Rating value={product.ratings}  color='gold' text={
          product.review >1
              ? `${product.review} Reviews`
              :  `${product.review} Review`} /> */}

        
      
      </Card.Body>      
    </Card>
    

  )
}

export default Product
