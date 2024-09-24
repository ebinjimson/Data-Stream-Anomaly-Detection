import numpy as np
from data_stream import generate_data_stream
from anomaly_detection import AnomalyDetector
from visualization import visualize_data

def main():
    """
    Main function to execute the anomaly detection process.

    This function generates a simulated data stream, fits an anomaly detector,
    detects anomalies in chunks of the generated stream, and visualizes the results.
    
    It simulates real-time processing by iterating over chunks of incoming data.
    """
    
    total_size = 1000   # Total number of points in the simulated stream
    chunk_size = 100   # Size of each chunk processed at a time

    # Generate a simulated data stream with specified size and noise level
    data_stream = generate_data_stream(size=total_size)

    # Initialize anomaly detector with a contamination rate of 5%
    detector = AnomalyDetector(contamination=0.05)

    all_anomalies = []   # List to store all detected anomalies

    for start in range(0, total_size, chunk_size):
        end = start + chunk_size
        
        if end > total_size:
            end = total_size
        
        chunk = data_stream[start:end]   # Get current chunk of data
        
        detector.fit(chunk)   # Fit model on current chunk
        
        anomalies = detector.detect_anomalies(chunk)   # Detect anomalies in current chunk
        
        all_anomalies.extend(anomalies)   # Store detected anomalies

        print(f"Processed chunk {start//chunk_size + 1}: Detected {len(anomalies)} anomalies")

    
    all_anomalies = np.array(all_anomalies)   # Convert list to array for visualization

    # Visualize results: full data stream and detected anomalies
    visualize_data(data_stream, all_anomalies)

if __name__ == "__main__":
    main()  # Execute main function when script is run directly