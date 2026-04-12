# Model Card: TuneTailor AI

## 1. System Overview

**What is TuneTailor AI trying to do?**  
TuneTailor AI is a lightweight music recommendation system that turns natural-language user requests into structured music preferences and then recommends songs from a small dataset. It extends the earlier Music Recommender Simulation by adding prompt interpretation, confidence scoring, recommendation explanations, and reliability testing.

**What inputs does TuneTailor AI take?**  
The system takes a natural-language user prompt, such as “I want calm acoustic music for studying,” and a local CSV file of songs. It also uses Python source files for parsing and recommendation logic.

**What outputs does TuneTailor AI produce?**  
The system outputs inferred user preferences, a confidence score, matched signals from the prompt, and a ranked list of recommended songs with explanations.

---

## 2. Retrieval / Recommendation Design

**How does the system work?**  
TuneTailor AI uses a content-based recommendation approach. First, it parses a natural-language prompt into structured preferences such as genre, mood, target energy, and acoustic preference. Then it loads songs from `songs.csv`, scores each song against the inferred profile, sorts the songs by score, and returns the top matches.

**How are songs scored?**  
The scoring system uses weighted feature matching:

- **+2.0** points for a genre match
- **+1.5** points for a mood match
- up to **+2.0** points based on how close the song’s energy is to the target energy
- up to **+1.0** point depending on whether the song matches the user’s acoustic preference

This makes the recommendation logic easy to understand and explain.

**Why did I choose this design?**  
I chose a rule-based parser and a content-based recommender because both are transparent, easy to test, and reproducible. A more advanced system could use an LLM or collaborative filtering, but this design made it easier to clearly show how the system makes decisions.

---

## 3. Strengths

- The system is easy to understand because the recommendation logic is transparent.
- It can accept natural-language prompts instead of requiring a hand-built user profile.
- It includes recommendation explanations, which makes the output more interpretable.
- It includes confidence scoring and matched-signal reporting, which make the system more honest about uncertainty.
- It includes automated tests, which improves reliability.

---

## 4. Limitations

- The dataset is very small, so recommendation diversity is limited.
- The parser relies on hand-written rules and keywords, which may miss more nuanced language.
- The system does not use listening history, collaborative filtering, lyrics, or artist similarity.
- Exact labels such as genre and mood can strongly affect ranking and reduce diversity.
- The scoring weights are manually chosen, so they reflect human assumptions and may introduce bias.

---

## 5. Reliability and Testing

**How did I test the system?**  
I tested both the parser and the recommendation logic using automated unit tests. These tests check whether the parser recognizes common prompt types and whether the recommender continues to return valid ranked outputs.

**Examples of what was tested**
- study-related prompts map to lofi/chill preferences
- gym/workout prompts map to higher energy
- happy/upbeat prompts are recognized correctly
- vague prompts still return safe default values
- acoustic preference is detected
- recommender tests pass for both functional and OOP implementations

**Current result**  
`7 tests passed`

**What worked well?**  
The system performed best when the prompt included clear signals such as “study,” “gym,” “happy,” “upbeat,” or “acoustic.” In those cases, the inferred preferences and final recommendations aligned well with the request.

**What did not work as well?**  
The system is weaker on vague prompts because it has to rely more heavily on default values. This keeps the system usable, but the recommendations may be less personalized.

---

## 6. AI Collaboration Reflection

**Where was AI helpful?**  
AI was helpful for brainstorming the structure of the upgraded system, improving explanation wording, and organizing documentation. It also helped speed up iteration when refining the README, parser logic, and section organization.

**Where was AI misleading?**  
AI could be misleading when it suggested code or wording that sounded polished but did not fully match the project requirements or the current code behavior. Because of that, I had to verify each suggestion against the rubric and test results instead of assuming the first output was correct.

**How did I use judgment while working with AI?**  
I treated AI as a support tool rather than a final authority. I checked whether suggestions matched the assignment, ran the code after making changes, and used tests to confirm that the system still worked as expected.

---

## 7. Ethical Considerations

This system is transparent, but it still reflects design choices that can shape the results. For example, the choice of weights, labels, and parser rules can privilege some music features over others. Because the dataset is small and the rules are hand-designed, the system may oversimplify user taste and should not be treated as a full representation of real musical preference. This project is best understood as a prototype that demonstrates interpretable AI system design rather than a production recommendation engine.

---

## 8. What This Project Taught Me

This project taught me that building an AI system is not just about producing output. It is also about deciding how the system interprets user input, how it explains its results, and how it handles uncertainty. I also learned that even a relatively simple system becomes much stronger when it includes testing, confidence signals, and clearer reasoning. Overall, this project helped me think more carefully about building AI systems that are functional, interpretable, and reliable.