from sklearn.ensemble import IsolationForest

def detect_anomalies(data, contamination=0.05):
    """
    Detect anomalies in the input data using Isolation Forest algorithm.
    
    Args:
        data (numpy.ndarray): Input data array.
        contamination (float, optional): Percentage of anomalies in the data. Defaults to 0.05.
    
    Returns:
        numpy.ndarray: Array of anomaly labels (-1 for anomaly, 1 for normal).
    """
    model = IsolationForest(contamination=contamination)
    data_reshaped = data.reshape(-1, 1)  # Reshape for model input
    model.fit(data_reshaped)
    anomalies = model.predict(data_reshaped)
    return anomalies