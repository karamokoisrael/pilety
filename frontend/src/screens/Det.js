import React from 'react';
import { Card, Col, Row } from 'react-bootstrap';
import Featured from '../components/HorizontalProductBox';

const ProductDetails = () => {
  return (
    <div>
        <Card className="product-details-container">
            <Row>

            
            <Col md={8}>
            <div className="product-details-image">
                <div className="product-details-image-container">
                <img src="https://picsum.photos/200/300" alt="Product" />
                </div>
            </div>
            </Col>
            <Col md={4}>
                <div className="product-details-info">
                    <h1 className="product-details-name">Product Name</h1>
                    <p className="product-details-quantity">Quantity: 10</p>
                    <p className="product-details-price">$100</p>
                    <p className="product-details-status">In StockStock</p>
                    <p className="product-details-status">Lorem Lorem Lorem Lorem 
                    Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem Lorem </p>
                    <button className="product-details-button">Add to Cart</button>
                </div>
            </Col>
            </Row>
        </Card>
        <Featured/>
    </div>
  );
};

export default ProductDetails;
