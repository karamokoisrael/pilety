import React from "react";
// import "./MapBox.css";

const MapBox = () => {
  return (
    <div className="map-wrapper">
      <div className="map-heading">Our Offices in China</div>
      <div className="map-container">
        <iframe
          className="map-iframe"
          src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d55655.120337735054!2d120.10270200000001!3d29.327951!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x344953f159a7bfdb%3A0x28f2492c19449a99!2sYiwu%20Museum!5e0!3m2!1sen!2sus!4v1681701471330!5m2!1sen!2sus"
          width="100%"
          height="100%"
          style={{ border: 0 }}
          allowFullScreen=""
          loading="lazy"
          referrerPolicy="no-referrer-when-downgrade"
        ></iframe>
      </div>
    </div>
  );
};

export default MapBox;
