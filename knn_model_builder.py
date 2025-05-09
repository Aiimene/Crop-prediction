import numpy as np
from sklearn.neighbors import NearestNeighbors

def build_knn_models(crop_environments, weights):
    """
    Build KNN models for each crop type and select best initial environment (medoid).
    
    Args:
    - crop_environments (dict): A dictionary where keys are crop types and values are lists of environments.
    - weights (list): List of weights for each feature for weighted Manhattan distance.
    
    Returns:
    - knn_models (dict): A dictionary where keys are crop types and values are KNN models.
    - crop_initial_envs (dict): A dictionary where keys are crop types and values are the best initial environment (medoid).
    """
    knn_models = {}
    crop_initial_envs = {}

    for crop_type, environments in crop_environments.items():
        env_array = np.array(environments)
        n_samples = len(env_array)

        if n_samples > 1:
            n_neighbors = min(3, n_samples)  # Always select 3 as the best number of neighbors

            # Define custom weighted Manhattan distance function to respect the weight when selecting the neighboring
            def weighted_manhattan_distance(x, y):
                weighted_diff = np.abs(x - y) * weights
                return np.sum(weighted_diff)

            # Create KNN model using the custom weighted distance metric
            knn = NearestNeighbors(
                n_neighbors=n_neighbors,
                algorithm='auto',
                metric=weighted_manhattan_distance
            )
            knn.fit(env_array)
            knn_models[crop_type] = knn

            # Compute pairwise distances and find the medoid (same as before)
            dists = np.sum(np.abs(env_array[:, None, :] - env_array[None, :, :]), axis=2)
            medoid_index = np.argmin(np.sum(dists, axis=1))
            crop_initial_envs[crop_type] = environments[medoid_index]

    return knn_models, crop_initial_envs


