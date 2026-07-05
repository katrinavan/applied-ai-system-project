from src.parser import parse_user_prompt


def test_study_prompt_maps_to_lofi_chill():
    result = parse_user_prompt("I want calm acoustic music for studying")
    assert result["genre"] == "lofi"
    assert result["mood"] == "chill"
    assert result["likes_acoustic"] is True
    assert result["confidence"] > 0.5 


def test_gym_prompt_maps_to_high_energy():
    result = parse_user_prompt("Give me workout songs for the gym")
    assert result["mood"] == "energetic"
    assert result["energy"] >= 0.8


def test_happy_prompt_detected():
    result = parse_user_prompt("Play happy upbeat songs")
    assert result["mood"] == "happy"
    assert result["energy"] >= 0.75


def test_vague_prompt_uses_defaults():
    result = parse_user_prompt("Recommend something")
    assert "genre" in result
    assert "mood" in result
    assert 0.0 <= result["confidence"] <= 1.0


def test_acoustic_keyword_detected():
    result = parse_user_prompt("Recommend acoustic songs")
    assert result["likes_acoustic"] is True