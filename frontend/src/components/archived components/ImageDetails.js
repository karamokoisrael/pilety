import React from 'react'
import Carousel from 'react-bootstrap/Carousel'
import {Row, Col, Image, ListGroup, Button, Card} from 'react-bootstrap'

function ImageDetails({source}) {
  return (
    <Carousel>
      <Carousel.Item>
        <Image 
          className="d-block w-100" 
          src={`${source[0]}?text=First slide&bg=373940`} 
          fluid />
      
      </Carousel.Item>

       <Carousel.Item>
        <Image 
          className="d-block w-100" 
          src={`${source[1]}?text=Second slide&bg=373940`} 
          fluid />
      </Carousel.Item>

      <Carousel.Item>
        <Image 
          className="d-block w-100" 
          src={`${source[2]}?text=Third slide&bg=373940`} 
          fluid />
      </Carousel.Item>

      <Carousel.Item>
        <Image 
        className="d-block w-100" 
        src={`${source[3]}?text=Forth slide&bg=373940`} 
        fluid />
      </Carousel.Item>

      <Carousel.Item>
        <Image 
        className="d-block w-100" 
        src={`${source[4]}?text=Fifth slide&bg=373940`} 
        fluid />
      </Carousel.Item>
      <Carousel.Item>
        <Image 
        className="d-block w-100" 
        src={`${source[5]}?text=Sixth slide&bg=373940`} 
        fluid /> 
      </Carousel.Item>
      
    </Carousel>
  //   {product.images?.map(image=> (
      
  //     <Col md={6} key={source.id}>
  //       <Carousel>
        
  //         <Carousel.Item key={source.id}>
  //         {source.id==1
  //           ? <Image 
  //           className="d-block w-100" 
  //           src={`${source.image}?text=First slide&bg=373940`} 
  //           fluid />
  //         : image.id==2
  //         ? <Image 
  //         className="d-block w-100" 
  //         src={`${source.image}?text=Second slide&bg=373940`} 
  //         fluid />
  //       : image.id==3
  //       ? <Image 
  //       className="d-block w-100" 
  //       src={`${source.image}?text=Third slide&bg=373940`} 
  //       fluid />
  //     : image.id==4
  //     ? <Image 
  //     className="d-block w-100" 
  //     src={`${source.image}?text=Forth slide&bg=373940`} 
  //     fluid />
  //   : image.id==5
  //   ? <Image 
  //   className="d-block w-100" 
  //   src={`${source.image}?text=Fifth slide&bg=373940`} 
  //   fluid />
  // : <Image 
  // className="d-block w-100" 
  // src={`${source.image}?text=Sixth slide&bg=373940`} 
  // fluid />

            
  //           }

            
  //         </Carousel.Item>
          
  //       </Carousel>
  //     </Col>)
      
  //     )}


  )
}

export default ImageDetails
