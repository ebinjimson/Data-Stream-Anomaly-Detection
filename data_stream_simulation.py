import numpy as np

def generate_data_stream(size=1000, noise_level=0.1):
    """
    Simulate a data stream with seasonal patterns and random noise.

    Parameters:
    size (int): The number of data points to generate.
    noise_level (float): The standard deviation of the noise added to the data.

    Returns:
    np.ndarray: An array containing the generated data stream.
    """
    time = np.arange(size)  # Create an array of time points
    seasonality = 10 * np.sin(2 * np.pi * time / 50)  # Seasonal pattern
    trend = 0.05 * time  # Linear trend over time
    noise = noise_level * np.random.randn(size)  # Random noise
    return seasonality + trend + noise  # Combine all components into the final data stream