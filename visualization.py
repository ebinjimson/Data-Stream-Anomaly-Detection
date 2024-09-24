import matplotlib.pyplot as plt

def visualize_data(data_stream, anomalies):
    """
    Visualize the data stream and highlight detected anomalies.

    Parameters:
    data_stream (np.ndarray): The complete data stream to visualize.
    anomalies (np.ndarray): An array containing detected anomalies.
    
    This function creates a line plot of the data stream and overlays 
    scatter points for detected anomalies in red.
    """
    
    plt.figure(figsize=(12, 6))  # Set figure size
    plt.plot(data_stream, label='Data Stream', color='blue')  # Plot the full data stream
    
    if len(anomalies) > 0:
        anomaly_indices = np.where(np.isin(data_stream, anomalies))[0]
        plt.scatter(anomaly_indices, anomalies, color='red', label='Anomalies', zorder=5)  # Highlight anomalies
    
    plt.title('Data Stream with Detected Anomalies')  # Title of the plot
    plt.xlabel('Time')  # X-axis label
    plt.ylabel('Value')  # Y-axis label
    plt.axhline(y=np.mean(data_stream) + 3*np.std(data_stream), color='orange', linestyle='--', label='Upper Threshold') 
    plt.axhline(y=np.mean(data_stream) - 3*np.std(data_stream), color='purple', linestyle='--', label='Lower Threshold')
    
    plt.legend()  # Show legend
    plt.grid()   # Add grid for better readability
    plt.show()   # Display the plot