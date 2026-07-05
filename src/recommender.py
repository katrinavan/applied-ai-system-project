from typing import List, Dict, Tuple
from dataclasses import dataclass
import csv


@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


def _describe_energy_match(energy_diff: float) -> str:
    if energy_diff <= 0.10:
        return "is very close to your target energy"
    if energy_diff <= 0.25:
        return "is fairly close to your target energy"
    return "is less aligned with your target energy"


def _describe_acoustic_match(likes_acoustic: bool, acousticness: float) -> str:
    if likes_acoustic:
        if acousticness >= 0.7:
            return "strongly matches your acoustic preference"
        if acousticness >= 0.4:
            return "somewhat matches your acoustic preference"
        return "only lightly matches your acoustic preference"
    else:
        if acousticness <= 0.3:
            return "fits your preference for less acoustic songs"
        if acousticness <= 0.6:
            return "somewhat fits your preference for less acoustic songs"
        return "is more acoustic than your usual preference"


def _build_dict_explanation(song: Dict, user_prefs: Dict) -> str:
    reasons = []

    if song["genre"].lower() == user_prefs["genre"].lower():
        reasons.append(f"it matches your preferred genre of {user_prefs['genre']}")

    if song["mood"].lower() == user_prefs["mood"].lower():
        reasons.append(f"it fits the {user_prefs['mood']} mood you asked for")

    energy_diff = abs(song["energy"] - user_prefs["energy"])
    reasons.append(_describe_energy_match(energy_diff))

    reasons.append(
        _describe_acoustic_match(
            user_prefs.get("likes_acoustic", False),
            song["acousticness"],
        )
    )

    return "Recommended because " + ", ".join(reasons) + "."


def _score_song_dict(song: Dict, user_prefs: Dict) -> Tuple[float, str]:
    score = 0.0

    if song["genre"].lower() == user_prefs["genre"].lower():
        score += 2.0

    if song["mood"].lower() == user_prefs["mood"].lower():
        score += 1.5

    energy_diff = abs(song["energy"] - user_prefs["energy"])
    energy_score = max(0.0, 2.0 - (energy_diff * 2))
    score += energy_score

    likes_acoustic = user_prefs.get("likes_acoustic", False)
    if likes_acoustic:
        acoustic_score = song["acousticness"]
    else:
        acoustic_score = 1.0 - song["acousticness"]

    score += acoustic_score

    explanation = _build_dict_explanation(song, user_prefs)
    return score, explanation


def _score_song_object(song: Song, user: UserProfile) -> float:
    score = 0.0

    if song.genre.lower() == user.favorite_genre.lower():
        score += 2.0

    if song.mood.lower() == user.favorite_mood.lower():
        score += 1.5

    energy_diff = abs(song.energy - user.target_energy)
    score += max(0.0, 2.0 - (energy_diff * 2))

    if user.likes_acoustic:
        score += song.acousticness
    else:
        score += 1.0 - song.acousticness

    return score


class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = []

        for song in self.songs:
            score = _score_song_object(song, user)
            scored_songs.append((song, score))

        scored_songs.sort(key=lambda item: item[1], reverse=True)
        return [song for song, _ in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append(f"it matches your preferred genre of {user.favorite_genre}")

        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append(f"it fits the {user.favorite_mood} mood you prefer")

        energy_diff = abs(song.energy - user.target_energy)
        reasons.append(_describe_energy_match(energy_diff))
        reasons.append(_describe_acoustic_match(user.likes_acoustic, song.acousticness))

        return "Recommended because " + ", ".join(reasons) + "."


def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)

    return songs


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5
) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []

    for song in songs:
        score, explanation = _score_song_dict(song, user_prefs)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)
    return scored_songs[:k]