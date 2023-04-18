import React, {useState, useEffect} from 'react'
import {Row, Col,ListGroup, Button, Card, Form} from 'react-bootstrap'
import { Link } from 'react-router-dom'
import { useParams, useNavigate } from 'react-router-dom'

import Loader from '../components/Loader'
import Message from '../components/Message'
import { useDispatch, useSelector } from 'react-redux'
import { listProductDetails } from '../actions/productActions'
import ImageSlider from '../components/ImageSlider'

function ProductDetails(history) { 
  const [qty, setQty] = useState(1)

  const dispatch = useDispatch();
  const productDetails = useSelector(state => state.productDetails);
  const { loading, error, product } = productDetails
  const { id } = useParams()

  useEffect(() => {
    dispatch(listProductDetails(id));
  }, [dispatch, id]);



  const navigate = useNavigate();

  const addToCartHandler = () => {
    navigate(`/cart/${id}?qty=${qty}`)
  }
  return (
    <div>
      {loading ? <Loader/>
                : error ? <Message variant='danger'>{error}</Message> 
                        : <Row>
                            <Col md={6}> 
                            
                              {product && product.images ? (
                                <ImageSlider images={product.images} />
                              ) : (
                                <p>No images available</p>
                              )}
                              </Col>

                            <Col md={3}>
                            <Card>
                            <ListGroup variant='flush'>

                            <ListGroup.Item>
                              <h3>{product.name} </h3>
                            </ListGroup.Item>

                            {/* <ListGroup.Item>
                              <Rating value={product.ratings} color='gold' text={
                                product.review == 1
                                    ? `${product.ratings} Review`
                                    : `${product.ratings} Reviews` }/> 
                            </ListGroup.Item> */}
                            {/* price */}
                            <ListGroup.Item>
                              Price : $ {product.price}
                            </ListGroup.Item>

                            {product.stock > 0 && (
                              <ListGroup.Item>
                                <Row>
                                  <Col>Qty</Col>
                                  <Col xs='auto' className='my-1'>
                                    <Form.Control
                                    as='select'
                                    value={qty}
                                    onChange={(e) => setQty(e.target.value)}
                                    >
                                      {
                                        [...Array(product.stock).keys()].map((x) => (
                                          <option key={x + 1} value={x + 1}>
                                            {x + 1}
                                          </option>
                                        ))
                                      }
                                    </Form.Control>
                                  </Col>
                                </Row>
                              </ListGroup.Item>
                            )
                            
                            }

                            {/* Description */}
                            <ListGroup.Item>
                            Description : {product.description}
                            </ListGroup.Item>

                          </ListGroup>
                            </Card>
                              
                            </Col>

                            <Col md={3}>
                              <Card>
                                <ListGroup variant='flush'>
                                  <ListGroup.Item>
                                    <Row>
                                      <Col>Price:</Col>
                                      <Col> <strong>${product.price}</strong></Col>
                                      

                                    </Row>
                                  </ListGroup.Item>
                                  {/* <ListGroup.Item>
                                    <Row>
                                      <Col>Status:</Col>
                                      <Col> 
                                        <strong>{product.gross_gain > 0  ? 'Aproved': 'Not Aproved'}
                                        </strong>
                                      </Col>
                                      

                                    </Row>
                                  </ListGroup.Item> */}
                                  <ListGroup.Item>
                                    <Button 
                                    onClick={addToCartHandler}
                                    className='btn btn-primary' 
                                    disabled={product.price==0}  
                                    type='button'> Add to Cart</Button>
                                  </ListGroup.Item>
                                  
                                </ListGroup>
                              </Card>
                            </Col>
                          </Row> 
      }

      <Link to='/' className='btn btn-light my-3'>Back</Link>
      
    </div>
  )
}

export default ProductDetails
