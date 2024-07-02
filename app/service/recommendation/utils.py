import pickle
import pandas as pd

# Load the KNN model
with open('knn_model.pkl', 'rb') as model_file:
    loaded_knn = pickle.load(model_file)

# Load the scaler
with open('scaler.pkl', 'rb') as scaler_file:
    loaded_scaler = pickle.load(scaler_file)

def get_genre_by_energy_and_valence(data: dict) -> str:
    """
    Predicts the genre based on energy and valence using a pre-trained KNN model.

    Args:
        data (dict): A dictionary containing the features for prediction.

    Returns:
        str: The predicted genre.
    """
    df = pd.DataFrame(data)
    scaled_data = loaded_scaler.transform(df)
    prediction = loaded_knn.predict(scaled_data)[0]
    return prediction
