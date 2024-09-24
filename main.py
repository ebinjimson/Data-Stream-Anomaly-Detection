import numpy as np
from data_stream import generate_data_stream
from anomaly_detection import AnomalyDetector
from visualization import visualize_data

def main():
    """
    Main function to execute the anomaly detection process.

    This function generates a simulated data stream, fits an anomaly detector,
    detects anomalies in the generated stream, and visualizes the results.
    """
    
    # Generate a simulated data stream with specified size and noise level
    data_stream = generate_data_stream(size=1000)

    # Initialize and fit anomaly detector with a contamination rate of 5%
    detector = AnomalyDetector(contamination=0.05)
    detector.fit(data_stream)

    # Detect anomalies in the generated data stream
    anomalies = detector.detect_anomalies(data_stream)

    # Visualize the results: full data stream and detected anomalies
    visualize_data(data_stream, anomalies)

if __name__ == "__main__":
    main()  # Execute main function when script is run directly