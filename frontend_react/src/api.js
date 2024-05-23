import axios from 'axios';

const BASE_URL = 'http://localhost:5000'; // Replace with your actual server URL

const api = axios.create({
  baseURL: BASE_URL,
  timeout: 5000, // Set a reasonable timeout
});

export const predictDevicePrice = async (deviceData) => {
  try {
    console.log(deviceData)
    const response = await api.post('/predict', deviceData);
    return response.data; // Assuming your server returns the predicted price range
  } catch (error) {
    console.error('Error predicting device price:', error);
    throw error;
  }
};
