from sklearn.ensemble import IsolationForest
import numpy as np

class AnomalyDetector:
    """
    A class for detecting anomalies in a data stream using the Isolation Forest algorithm.

    Attributes:
    model (IsolationForest): The Isolation Forest model used for anomaly detection.
    """

    def __init__(self, contamination=0.05):
        """
        Initialize the AnomalyDetector with a specified contamination rate.

        Parameters:
        contamination (float): The proportion of outliers in the data set.
        """
        self.model = IsolationForest(contamination=contamination)

    def fit(self, data_stream):
        """
        Fit the Isolation Forest model to the provided data stream.

        Parameters:
        data_stream (np.ndarray): The input data stream to fit the model.
        """
        self.model.fit(data_stream.reshape(-1, 1))  # Reshape for fitting

    def detect_anomalies(self, data_stream):
        """
        Detect anomalies in the incoming data stream.

        Parameters:
        data_stream (np.ndarray): The input data stream to check for anomalies.

        Returns:
        np.ndarray: An array containing the detected anomalies.
        """
        scores = self.model.predict(data_stream.reshape(-1, 1))  # Predict anomalies
        anomalies = data_stream[scores == -1]  # Extract anomalies (-1 indicates anomaly)
        return anomalies