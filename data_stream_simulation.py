import numpy as np

def generate_data_stream(size=1000, noise_level=0.1):
    """
    Simulate a data stream with seasonal patterns, random noise,
    and occasional spikes or drops to represent real-world metrics.

    Parameters:
    size (int): The number of data points to generate.
    noise_level (float): The standard deviation of the noise added to the data.

    Returns:
    np.ndarray: An array containing the generated data stream.
    """
    time = np.arange(size)  # Create an array of time points
    seasonality = 10 * np.sin(2 * np.pi * time / 50)  # Seasonal pattern
    trend = 0.05 * time  # Linear trend
    noise = noise_level * np.random.randn(size)  # Random noise
    
    # Introduce occasional spikes and drops
    spikes = np.random.choice([0, 20, -20], size=size, p=[0.95, 0.025, 0.025])
    
    return seasonality + trend + noise + spikes  # Combine all components into the final data stream