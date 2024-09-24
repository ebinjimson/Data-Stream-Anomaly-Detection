import numpy as np

def generate_data_stream(size=1000):
    """
    Generate a simulated data stream with seasonal patterns and noise.
    
    Args:
        size (int, optional): Size of the data stream. Defaults to 1000.
    
    Returns:
        numpy.ndarray: Simulated data stream.
    """
    time = np.arange(size)
    seasonal_pattern = np.sin(time / 50)  # Seasonal component
    noise = np.random.normal(0, 0.5, size)  # Random noise
    data_stream = seasonal_pattern + noise
    return data_stream