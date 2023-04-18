// import React from "react";
// // import "./MapBox.css";

// const MapBox = () => {
//   return (
//     <div className="map-wrapper">
//       <div className="map-heading">Our Offices in China</div>
//       <div className="map-container">
//         <iframe
//           className="map-iframe"
//           src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d55655.120337735054!2d120.10270200000001!3d29.327951!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x344953f159a7bfdb%3A0x28f2492c19449a99!2sYiwu%20Museum!5e0!3m2!1sen!2sus!4v1681701471330!5m2!1sen!2sus"
//           width="100%"
//           height="100%"
//           style={{ border: 0 }}
//           allowFullScreen=""
//           loading="lazy"
//           referrerPolicy="no-referrer-when-downgrade"
//         ></iframe>
//       </div>
//     </div>
//   );
// };

// export default MapBox;


import React from "react";

const MapBox = () => {
  return (
    <div className="map-container">
      <h2 className="title">Visit Our Office</h2>
      <div className="map-wrapper">
        <iframe
          title="Google Maps"
          src="https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d55655.120337735054!2d120.10270200000001!3d29.327951!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x344953f159a7bfdb%3A0x28f2492c19449a99!2sYiwu%20Museum!5e0!3m2!1sen!2sus!4v1681701471330!5m2!1sen!2sus"
          frameBorder="0"
          style={{ border: 0, height: "100%", width: "100%" }}
          allowFullScreen=""
          loading="lazy"
        ></iframe>
        <div className="info-box">
          <h3>Our Office</h3>
          <p>Yiwu Jinhua</p>
          <p>Futian, dist 4, block 20</p>
          <p>Phone: 555-555-5555</p>
          <p>Days of Work: Mon-Sun</p>
        </div>
      </div>
    </div>
  );
};

export default MapBox;

