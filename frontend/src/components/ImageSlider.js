import React, { useState } from 'react';
import { Image, Card} from 'react-bootstrap'


const ImageSlider = ({ images }) => {
  const [currentImageIndex, setCurrentImageIndex] = useState(0);

  const handleNext = () => {
    setCurrentImageIndex(currentImageIndex === images.length - 1 ? 0 : currentImageIndex + 1);
  };

  const handlePrevious = () => {
    setCurrentImageIndex(currentImageIndex === 0 ? images.length - 1 : currentImageIndex - 1);
  };

  return (
    <Card className="image-slider">
      
      <Card.Img src={images[currentImageIndex].image} alt={`Image ${currentImageIndex + 1}`} />
      <div className="controls">
        <button onClick={handlePrevious}>Prev</button>
        <button onClick={handleNext}>Next</button>
      </div>
    </Card>
  );
};

export default ImageSlider;
