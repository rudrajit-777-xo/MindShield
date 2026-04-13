def detect_cbt_patterns(text):
    text = text.lower()

    patterns = {
    "Always thinking negative": {
        "keywords": [
            "always", "never", "everytime", "nothing ever works",
            "everything goes wrong", "this always happens",
            "i always fail", "i never succeed", "nothing works for me",
            "it never gets better", "i am always unlucky",
            "things always go bad", "i always mess up"
        ],
        "description": "You feel like bad situations happen all the time."
    },

    "Expecting the worst": {
        "keywords": [
            "worst", "disaster", "ruin", "everything is over",
            "nothing is left", "it's finished", "it's all over",
            "there is no hope", "hopeless", "it will fail",
            "this will go wrong", "i know it will fail",
            "something bad will happen", "it’s ruined",
            "there’s no way this works"
        ],
        "description": "You assume the worst possible outcome."
    },

    "Blaming yourself": {
        "keywords": [
            "my fault", "because of me", "i am the reason",
            "i caused this", "it's all on me", "i messed up",
            "i ruined everything", "this happened because of me",
            "i am responsible for this", "i should have done better",
            "i always mess things up"
        ],
        "description": "You take responsibility for things not fully in your control."
    },

    "Assuming others think badly": {
        "keywords": [
            "they hate me", "everyone hates me", "they think i'm stupid",
            "they think badly of me", "people are judging me",
            "they are judging me", "no one likes me",
            "people don't like me", "they are talking about me",
            "they think i'm useless", "everyone is against me"
        ],
        "description": "You assume what others think without evidence."
    },

    "All or nothing thinking": {
        "keywords": [
            "perfect", "completely", "totally", "all or nothing",
            "either this or nothing", "if not perfect then useless",
            "total failure", "completely failed",
            "nothing matters", "everything is ruined",
            "no middle ground", "either i win or lose",
            "i failed completely"
        ],
        "description": "You see situations as all good or all bad."
    }
}
    detected = []

    for name, data in patterns.items():
        for keyword in data["keywords"]:
            if keyword in text:
                detected.append({
                    "pattern": name,
                    "description": data["description"]
                })
                break

    if detected:
        return detected
    else:
        return [{
            "pattern": "Healthy thinking",
            "description": "No strong negative thinking pattern detected."
        }]