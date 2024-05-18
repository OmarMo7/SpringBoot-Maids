package com.omar.demo.controller;

import com.omar.demo.DeviceSpecs;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.HttpStatus;
import java.net.HttpURLConnection;
import java.net.URL;

@RestController
@RequestMapping("/api")
public class PricePrediction {

    @PostMapping("/predict")
    public String predictPrice(@RequestBody DeviceSpecs deviceSpecs) {
        try {
            String predictedPriceRange = callPythonModel(deviceSpecs);
            return predictedPriceRange;
        } catch (Exception e) {
            // Handle exceptions (e.g., model server error)
            return "Error predicting price: " + e.getMessage();
        }
    }

    private String callPythonModel(DeviceSpecs deviceSpecs) {
        String pythonModelUrl = "http://localhost:5000/predict";
        RestTemplate restTemplate = new RestTemplate();

        ResponseEntity<String> response = restTemplate.postForEntity(pythonModelUrl, deviceSpecs, String.class);
        if (response.getStatusCode() == HttpStatus.OK) {
            return response.getBody();
        } else {
            throw new RuntimeException("Model server returned an error: " + response.getStatusCode());
        }
    }
}
