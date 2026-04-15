def detect_cbt_patterns(text):
    text = text.lower()

    patterns = {
    "Always thinking negative": {
        "keywords": [
            "always", "never", "everytime", "nothing ever works",
            "everything goes wrong", "this always happens",
            "i always fail", "i never succeed", "nothing works for me",
            "it never gets better", "i am always unlucky",
            "things always go bad", "i always mess up",
            "nothing ever improves", "i always get it wrong",
            "it always ends badly", "i never do anything right",
            "i keep failing", "same thing happens every time",
            "nothing changes", "i am stuck like this forever"
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
            "there’s no way this works",
            "this is going to be terrible", "i am doomed",
            "it will end badly", "nothing good will happen",
            "i can’t see any good outcome", "it’s going to fall apart",
            "everything will collapse", "i expect the worst",
            "this will turn into a disaster"
        ],
        "description": "You assume the worst possible outcome."
    },

    "Blaming yourself": {
        "keywords": [
            "my fault", "because of me", "i am the reason",
            "i caused this", "it's all on me", "i messed up",
            "i ruined everything", "this happened because of me",
            "i am responsible for this", "i should have done better",
            "i always mess things up",
            "i am to blame", "it’s my mistake",
            "i shouldn’t have done that", "i failed everyone",
            "i let everyone down", "i am the problem",
            "i could have prevented this", "this is on me",
            "i take the blame", "i did everything wrong"
        ],
        "description": "You take responsibility for things not fully in your control."
    },

    "Assuming others think badly": {
        "keywords": [
            "they hate me", "everyone hates me", "they think i'm stupid",
            "they think badly of me", "people are judging me",
            "they are judging me", "no one likes me",
            "people don't like me", "they are talking about me",
            "they think i'm useless", "everyone is against me",
            "they must think i’m weird", "they are laughing at me",
            "people are criticizing me", "they think i’m a failure",
            "others see me as weak", "they don’t respect me",
            "they are ignoring me", "they don’t care about me",
            "everyone is watching me", "they are disappointed in me"
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
            "i failed completely",
            "it’s either success or failure",
            "i have to be perfect", "anything less is failure",
            "there’s no in-between", "i am either good or bad",
            "it’s black or white", "everything is lost",
            "i must succeed or i am nothing",
            "if i fail once, i am a failure"
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