import pandas as pd
import random

data = []

for _ in range(5000):
    # Generate features
    compound = round(random.uniform(-1, 1), 3)
    cbt_score = random.randint(0, 5)

    # Logic for risk (with some randomness for realism)
    if compound < -0.6 and cbt_score >= 3:
        risk = "High"
    elif compound < -0.2 and cbt_score >= 1:
        risk = random.choice(["Medium", "High"])
    elif compound >= 0.2 and cbt_score == 0:
        risk = "Low"
    else:
        risk = random.choice(["Low", "Medium"])

    data.append([compound, cbt_score, risk])

# Create DataFrame
df = pd.DataFrame(data, columns=["compound", "cbt_score", "risk"])

# Save CSV
df.to_csv("data/dataset.csv", index=False)

print("Dataset created with 5000 rows!")