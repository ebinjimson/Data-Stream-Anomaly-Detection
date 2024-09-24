import matplotlib.pyplot as plt

def visualize_data_stream(data, anomalies):
    """
    Visualize the data stream and highlight detected anomalies.
    
    Args:
        data (numpy.ndarray): Data stream values.
        anomalies (numpy.ndarray): Array of anomaly labels (-1 for anomaly, 1 for normal).
    """
    plt.figure(figsize=(10, 6))
    plt.plot(data, label='Data Stream', color='blue')
    plt.scatter(np.where(anomalies == -1)[0], data[anomalies == -1], color='red', label='Anomalies')
    plt.title('Data Stream with Anomalies')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.show()
    