import pandas as pd
import numpy as np

np.random.seed(42)
n_routes = 200

data = {
    'source': np.random.choice(['A', 'B', 'C', 'D'], n_routes),
    'destination': np.random.choice(['E', 'F', 'G', 'H'], n_routes),
    'latency_ms': np.random.uniform(10, 200, n_routes),
    'bandwidth_mbps': np.random.uniform(1, 100, n_routes),
    'traffic_load': np.random.uniform(0, 1, n_routes),
    'hop_count': np.random.randint(2, 8, n_routes)
}

df = pd.DataFrame(data)

df['score'] = (
    (0.4 * (200 - df['latency_ms'])) + 
    (0.4 * df['bandwidth_mbps']) + 
    (0.2 * (1 - df['traffic_load']) * 100)
)

df.to_csv('data/routing_data.csv', index=False)
print("Routing data simulated and saved to data/routing_data.csv")
