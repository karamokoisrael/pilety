import React, { useState } from "react";
// import { ListGroup } from "react-bootstrap";
import ListGroup from 'react-bootstrap/ListGroup';

const ServiceBox = ({ title, description, active, onClick }) => {
  return (
    <div className={`service-box ${active ? "active" : ""}`} onClick={onClick}>
      <h3>{title}</h3>
      {active && <p>{description}</p>}
    </div>
  );
};

const ServiceDescription = ({ activeBox }) => {
  const descriptions = {
    warehouse:
      "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec eget dolor eget odio rhoncus dictum. Morbi faucibus mauris vitae sapien blandit, sed volutpat quam finibus. Integer in mauris ex. Sed malesuada felis lectus, et blandit sapien bibendum vel.",
    shipping:
      "Sed sit amet lacinia arcu. Curabitur dictum erat sed iaculis iaculis. Maecenas non erat ut elit malesuada cursus. Sed ut viverra ex. Morbi id faucibus dolor, nec malesuada arcu. Sed et consectetur ipsum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae.",
    productSourcing:
      "Nulla eu tortor justo. Suspendisse lobortis augue et sagittis lobortis. Vivamus vel felis at lacus porttitor feugiat vel vitae risus. Fusce euismod nulla vitae nisi luctus bibendum. Aliquam laoreet, mauris sed malesuada bibendum, lectus mauris consectetur lorem, ut commodo mauris tellus ac nulla. Nam quis tellus metus. Nullam vitae ante id metus maximus elementum in id nulla."
  };

  return (
    <div className="service-description">
      <p>{descriptions[activeBox]}</p>
    </div>
  );
};


const ServicBoxes = () => {
  const [activeService, setActiveService] = useState("shipping");

  const handleClick = (service) => {
    setActiveService(service);
  };

  return (
    <div className="services-container">
      <ListGroup horizontal className="services-heading">
        <ListGroup.Item
          className={`services-title ${activeService === "warehouse" ? "active" : ""}`}
          onClick={() => handleClick("warehouse")}
        >
          Warehouse
        </ListGroup.Item>
        <ListGroup.Item
          className={`services-title ${activeService === "shipping" ? "active" : ""}`}
          onClick={() => handleClick("shipping")}
        >
          Shipping
        </ListGroup.Item>
        <ListGroup.Item
          className={`services-title ${activeService === "sourcing" ? "active" : ""}`}
          onClick={() => handleClick("sourcing")}
        >
          Sourcing
        </ListGroup.Item>
      </ListGroup>
      <div className="services-description">
        {activeService === "warehouse" && (
          <p>
            Our warehouse is equipped with the latest technology to ensure the
            safety and security of your products.
          </p>
        )}
        {activeService === "shipping" && (
          <p>
            We offer fast and reliable shipping services to ensure your products
            arrive at their destination on time and in good condition.
          </p>
        )}
        {activeService === "sourcing" && (
          <p>
            We have a vast network of suppliers to help you find the best products
            at the most competitive prices.
          </p>
        )}
      </div>
    </div>
  );
};

export default ServicBoxes;
