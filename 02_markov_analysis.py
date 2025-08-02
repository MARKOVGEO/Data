import pandas as pd
import numpy as np
from scipy.linalg import eig

# Load processed data
df = pd.read_csv("../data/processed/mining_trajectories.csv")

# Initialize transition count matrix
states = ["Prospect", "Active", "Past Producer", "Closed"]
transition_counts = np.zeros((len(states), len(states))

# Count transitions
for _, row in df.iterrows():
    state_sequence = list(map(int, row['states'].split(';')))
    for i in range(len(state_sequence) - 1):
        from_state = state_sequence[i]
        to_state = state_sequence[i+1]
        transition_counts[from_state][to_state] += 1

# Calculate transition probabilities
transition_matrix = transition_counts / transition_counts.sum(axis=1)[:, np.newaxis]

# Save transition matrix
pd.DataFrame(transition_matrix, columns=states, index=states).to_csv("../results/transition_matrix.csv")

# Calculate stationary distribution
eigenvalues, eigenvectors = eig(transition_matrix.T)
stationary_idx = np.argmin(np.abs(eigenvalues - 1.0))
stationary_vector = np.real(eigenvectors[:, stationary_idx])
stationary_vector /= stationary_vector.sum()

# Save results
pd.DataFrame({"State": states, "Probability": stationary_vector}).to_csv("../results/stationary_vector.csv", index=False)