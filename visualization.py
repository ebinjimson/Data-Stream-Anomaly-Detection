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
    plt.figure(figsize=(10, 5))  # Set figure size
    plt.plot(data_stream, label='Data Stream')  # Plot the full data stream
    if len(anomalies) > 0:
        plt.scatter(np.where(data_stream == anomalies)[0], anomalies, color='red', label='Anomalies')  # Highlight anomalies
    plt.title('Data Stream with Anomalies')  # Title of the plot
    plt.xlabel('Time')  # X-axis label
    plt.ylabel('Value')  # Y-axis label
    plt.legend()  # Show legend
    plt.show()  # Display the plot