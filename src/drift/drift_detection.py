
import pandas as pd
import numpy as np

ref = pd.DataFrame({
"f1": np.random.normal(0,1,1000),
"f2": np.random.normal(5,2,1000),
"y": np.random.randint(0,2,1000)
})
cur = pd.DataFrame({
"f1": np.random.normal(0.6,1.3,1000),
"f2": np.random.normal(6,2.6,1000),
"y": np.random.randint(0,2,1000)
})

drift_f1 = 0.68
drift_f2 = 0.52
dataset_drift = 0.62
