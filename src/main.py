"""
Command line runner for the Applied AI music recommender.

This version extends the original recommender by allowing
natural-language prompts to be converted into structured
user preferences before generating recommendations.
"""

from src.recommender import load_songs, recommend_songs
from src.parser import parse_user_prompt


def run_prompt(prompt: str, songs: list[dict], k: int = 5) -> None:
    parsed = parse_user_prompt(prompt)

    user_prefs = {
        "genre": parsed["genre"],
        "mood": parsed["mood"],
        "energy": parsed["energy"],
        "likes_acoustic": parsed["likes_acoustic"],
    }

    recommendations = recommend_songs(user_prefs, songs, k=k)

    print(f"\nPrompt: {prompt}")
    print("Inferred preferences:")
    print(user_prefs)
    print(f"Confidence: {parsed['confidence']:.2f}")
    print(f"Matched signals: {parsed['matched_signals']}\n")

    for song, score, explanation in recommendations:
        print(f"{song['title']} - Score: {score:.2f}")
        print(f"Because: {explanation}")
        print()


def main() -> None:
    songs = load_songs("data/songs.csv")

    prompts = [
        "Give me happy upbeat songs for a fun drive",
        "I want calm acoustic music for studying",
        "Recommend chill rainy day songs",
    ]

    for prompt in prompts:
        run_prompt(prompt, songs, k=5)


if __name__ == "__main__":
    main() 