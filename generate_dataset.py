import pandas as pd
import numpy as np
import random

def generate_data(num_rows=5000):
    data = []
    
    dummy_texts = [
        "I feel great today, everything went well.",
        "Nothing matters anymore, it's all ruined.",
        "I guess today was okay, just normal.",
        "It's my fault they are mad at me.",
        "I will never succeed, this always happens.",
        "I had a good time with my friends.",
        "They probably think I'm stupid.",
        "If it's not perfect, it's a total failure.",
        "I am so stressed and tired of this.",
        "Things are getting better step by step."
    ]

    for i in range(num_rows):
        # Base sentiment
        is_negative = random.choice([True, False, False])  # 33% chance of being very negative
        
        if is_negative:
            sentiment_compound = round(random.uniform(-1.0, -0.1), 3)
            sentiment_label = "Negative"
            text = random.choice([dummy_texts[1], dummy_texts[3], dummy_texts[4], dummy_texts[6], dummy_texts[7], dummy_texts[8]])
        else:
            is_positive = random.choice([True, False])
            if is_positive:
                sentiment_compound = round(random.uniform(0.1, 1.0), 3)
                sentiment_label = "Positive"
                text = random.choice([dummy_texts[0], dummy_texts[5], dummy_texts[9]])
            else:
                sentiment_compound = round(random.uniform(-0.1, 0.1), 3)
                sentiment_label = "Neutral"
                text = dummy_texts[2]

        # Generate cognitive distortions based on sentiment
        distortion_always_negative = 1 if sentiment_compound < -0.3 and random.random() > 0.5 else 0
        distortion_expecting_worst = 1 if sentiment_compound < -0.4 and random.random() > 0.6 else 0
        distortion_blaming_yourself = 1 if sentiment_compound < -0.2 and random.random() > 0.7 else 0
        distortion_assuming_others = 1 if sentiment_compound < -0.2 and random.random() > 0.7 else 0
        distortion_all_or_nothing = 1 if sentiment_compound < -0.5 and random.random() > 0.6 else 0
        
        total_distortions = sum([
            distortion_always_negative, distortion_expecting_worst, 
            distortion_blaming_yourself, distortion_assuming_others, distortion_all_or_nothing
        ])

        # Past days history (0 to 7 consecutive negative days)
        if sentiment_compound < 0:
            consecutive_negative_days = random.randint(1, 7)
        else:
            consecutive_negative_days = random.randint(0, 2)
            
        # Determine risk level based on logical conditions
        if total_distortions >= 2 and consecutive_negative_days >= 3 and sentiment_compound < -0.5:
            risk_level = "High"
        elif total_distortions >= 1 or consecutive_negative_days >= 2 or sentiment_compound < -0.2:
            risk_level = "Medium"
        else:
            risk_level = "Low"
            
        data.append({
            "text": text,
            "sentiment_compound": sentiment_compound,
            "sentiment_label": sentiment_label,
            "distortion_always_negative": distortion_always_negative,
            "distortion_expecting_worst": distortion_expecting_worst,
            "distortion_blaming_yourself": distortion_blaming_yourself,
            "distortion_assuming_others": distortion_assuming_others,
            "distortion_all_or_nothing": distortion_all_or_nothing,
            "consecutive_negative_days": consecutive_negative_days,
            "risk_level": risk_level
        })
        
    df = pd.DataFrame(data)
    df.to_csv("data/mental_health_dataset.csv", index=False)
    print(f"Generated data/mental_health_dataset.csv with {num_rows} rows.")

if __name__ == "__main__":
    generate_data(5000)
