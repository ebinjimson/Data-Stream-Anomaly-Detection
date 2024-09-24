from anomaly_detector import detect_anomalies_in_stream

def process_stream(size=1000):
    """
    Process a data stream and print detected anomalies.
    
    Args:
        size (int, optional): Size of the data stream. Defaults to 1000.
    """
    data_stream, anomalies = detect_anomalies_in_stream(size)
    
    for i in range(size):
        if anomalies[i] == -1:  # -1 indicates an anomaly
            print(f"Anomaly detected at index {i}: {data_stream[i]}")