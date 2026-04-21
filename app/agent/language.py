def detect_language(text: str):

    text = text.lower()

    # Hindi keywords
    hindi_words = ["hai", "karna", "book", "doctor", "appointment", "kal", "aaj"]

    # Tamil keywords (basic heuristic)
    tamil_words = ["doctor", "venum", "book", "appointment", "indha", "naala"]

    if any(w in text for w in hindi_words):
        return "hi"

    if any(w in text for w in tamil_words):
        return "ta"

    return "en"