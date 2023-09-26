
import React, {useState, useEffect} from 'react'
import { Row, Col } from 'react-bootstrap'
import {useDispatch, useSelector} from 'react-redux'

import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';

import Product from '../components/Product'
import {listProducts} from '../actions/productActions'
import Loader from '../components/Loader';
import Message from '../components/Message';
import Cargo from '../components/Cargo';
import HorizontalProductBox from '../components/HorizontalProductBox'
import TrackingBox from '../components/TrakingBox'
import ServicesBox from '../components/ServicesBox'
import Featured from '../components/HorizontalProductBox';
import MapBox from '../components/MapBox';

function HomePage() {
  // const dispatch = useDispatch()
  // const productList = useSelector(state => state.productList)
  // const {error, loading, products} = productList
 
  // useEffect(() => {
  //   dispatch(listProducts())
      
  
  // }, [dispatch])
// const merch = products
  return (
    <div>
      <ServicesBox/>
      <TrackingBox/>
      <Featured/>
      <MapBox/>
      {/* <HorizontalProductBox/> */}
      
      <Tabs
      defaultActiveKey="profile"
      id="uncontrolled-tab-example"
      className="mb-3"
    >
      
      
      {/* <Tab eventKey="stemmix" title="Stem Mix">
      <h1 className='text-center p-3'> Stems</h1>
      </Tab> */}
      {/* <Tab eventKey="mix" title="Merch">
      <h1 className='text-center p-3'> Latest Merch</h1>
        {loading ? <Loader/>
                 : error ? <Message variant='danger'>{error}</Message>
                         :<Row>
                            { merch.map(product => (
                              <Col key={product.id} sm={12} md={12} lg={4} xl={3}> 
                                <Product product={product}> </Product>
                              </Col>
                            ))}
                          </Row>}


      </Tab> */}
      {/* <Tab eventKey="contact" title="Contact">
        <div>THis is Contact</div>
      </Tab>
      <Tab eventKey="lims" title="Lims">
        <div>THis is Lims</div>
      </Tab> */}
    </Tabs>
    
      
    </div>
  )
}

export default HomePage
