import React, { useState } from 'react';

function TrackingBox() {
  const [trackingNumber, setTrackingNumber] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`Tracking number submitted: ${trackingNumber}`);
    // Here you can add the logic to handle the submission of the tracking number, like sending an API request to retrieve the tracking information.
  };

  return (
    <div className="tracking-container">
      <h1 className="tracking-title">Track Your Shipment</h1>
      <form className="tracking-form" onSubmit={handleSubmit}>
        <label className="tracking-label">
          Tracking Number:
          <input className="tracking-input" type="text" value={trackingNumber} onChange={(event) => setTrackingNumber(event.target.value)} />
        </label>
        <button className="tracking-button" type="submit">Track Package</button>
      </form>
    </div>
  );
}

export default TrackingBox;
