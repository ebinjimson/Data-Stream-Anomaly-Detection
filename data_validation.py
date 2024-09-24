import numpy as np

def validate_data(data):
    """
    Validate the input data for anomaly detection.
    
    Args:
        data (numpy.ndarray): Input data array.
    
    Raises:
        ValueError: If the input data is not a numpy array.
    """
    if not isinstance(data, np.ndarray):
        raise ValueError("Data must be a numpy array.")