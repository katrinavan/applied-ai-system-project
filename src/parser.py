def parse_user_prompt(prompt: str) -> dict:
    text = prompt.lower()

    genre = None
    mood = None
    energy = 0.5
    likes_acoustic = False
    matched_signals = [] 

    if "study" in text or "focus" in text or "lofi" in text:
        genre = "lofi"
        mood = "chill"
        energy = 0.3
        matched_signals.append("study/focus/lofi")

    if "gym" in text or "workout" in text:
        mood = "energetic"
        energy = 0.9
        matched_signals.append("gym/workout")

    if "chill" in text or "calm" in text or "rain" in text:
        mood = "chill"
        energy = min(energy, 0.4)
        likes_acoustic = True
        matched_signals.append("chill/calm/rain")

    if "happy" in text or "upbeat" in text:
        mood = "happy"
        energy = max(energy, 0.75)
        matched_signals.append("happy/upbeat")

    if "acoustic" in text:
        likes_acoustic = True
        matched_signals.append("acoustic")

    if genre is None:
        genre = "pop"
    if mood is None:
        mood = "happy"

    confidence = min(1.0, 0.25 * len(matched_signals) + 0.25)

    return {
        "genre": genre,
        "mood": mood,
        "energy": energy,
        "likes_acoustic": likes_acoustic,
        "confidence": confidence,
        "matched_signals": matched_signals,
    }