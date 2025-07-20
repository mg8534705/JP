import fugashi

def tokenize_japanese(text):
    tagger = fugashi.Tagger()
    return ' '.join([word.surface for word in tagger(text)])

def detect_honorific(text):
    if "さま" in text or "様" in text or "ございます" in text:
        return "formal"
    return "neutral"
