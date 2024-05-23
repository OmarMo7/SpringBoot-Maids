import React, { useState } from 'react';
import { predictDevicePrice } from '../api';

const DeviceForm = () => {
  const [deviceData, setDeviceData] = useState({
    battery_power: 1002,
    blue: 1,
    clock_speed: 2.9,
    dual_sim: 1,
    fc: 0,
    four_g: 0,
    int_memory: 9,
    m_dep: 0.1,
    mobile_wt: 182,
    n_cores: 5,
    pc: 1,
    px_height: 248,
    px_width: 874,
    ram: 3946,
    sc_h: 5,
    sc_w: 2,
    talk_time: 2,
    three_g: 7,
    touch_screen: 0,
    wifi: 0
    });

  const handlePredict = async () => {
    try {
      const predictedPriceRange = await predictDevicePrice(deviceData);
      alert(`Predicted price range: ${predictedPriceRange}`);
    } catch (error) {
      alert('Error predicting price. Please try again later.');
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setDeviceData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  return (
    <div>
      {Object.keys(deviceData).map((key) => (
        <div key={key}>
          <label htmlFor={key}>{key}</label>
          <input
            type="text"
            id={key}
            name={key}
            value={deviceData[key]}
            onChange={handleChange}
            placeholder={key}
          />
        </div>
      ))}
      <button onClick={handlePredict}>Predict</button>
    </div>
  );
};

export default DeviceForm;