from stream_processor import process_stream
from visualization import visualize_data_stream

def main():
    """
    Main entry point of the application.
    """
    process_stream(size=1000)
    
    # Visualize the data stream and anomalies
    data_stream, anomalies = detect_anomalies_in_stream(size=1000)
    visualize_data_stream(data_stream, anomalies)

if __name__ == "__main__":
    main()