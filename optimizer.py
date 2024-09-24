from sklearn.ensemble import IsolationForest

def optimize_isolation_forest(data, n_estimators=100):
    """
    Optimize the Isolation Forest algorithm for the input data.
    
    Args:
        data (numpy.ndarray): Input data array.
        n_estimators (int, optional): Number of trees in the forest. Defaults to 100.
    
    Returns:
        sklearn.ensemble._iforest.IsolationForest: Optimized Isolation Forest model.
    """
    model = IsolationForest(n_estimators=n_estimators, contamination=0.05)
    data_reshaped = data.reshape(-1, 1)  # Reshape for model input
    model.fit(data_reshaped)
    return model