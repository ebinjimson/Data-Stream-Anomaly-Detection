from data_stream_simulation import generate_data_stream
from anomaly_detection import detect_anomalies

def detect_anomalies_in_stream(size=1000):
    """
    Detect anomalies in a simulated data stream.
    
    Args:
        size (int, optional): Size of the data stream. Defaults to 1000.
    
    Returns:
        numpy.ndarray: Array of data stream values.
        numpy.ndarray: Array of anomaly labels (-1 for anomaly, 1 for normal).
    """
    data_stream = generate_data_stream(size)
    anomalies = detect_anomalies(data_stream)
    return data_stream, anomalies