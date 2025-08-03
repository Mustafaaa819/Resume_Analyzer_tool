# Resume Analyzer Tool 🔍📄

This tool ranks candidates based on how well their resumes match your required **skills, education, and experience** — it *understands meaning* using **AI embeddings**.

---

## 📁 Inside Folder Directory:

- `semantic_version.py` → main code with OpenAI’s embeddings + semantic matching
- `resume_data.csv` → (dummy) resume info for testing
- `.env` → your OpenAI key lives here, keep it secret 🤫

---

## 🧠 What This Tool Does

- Ask user to enter:
  - Skills (e.g. Python, SQL)
  - Education (e.g. BS, MS)
  - Degrees (e.g. Computer Science, AI)

- It reads resume data from a CSV file.
- It calculates a score for every candidate.
- Finally, it ranks them by how well they match your criteria.

---

## ⚙️ How It Scores Candidates

1. **Skills Matching**
   - Every skill you input is compared with the skills in each resume.
   - If they're close in meaning (not just spelling), they get points.
   - This is done using **embeddings** — think of them as smart number versions of text.

   > ✍️ *Embeddings = words turned into number-vectors so the computer can "understand" their meaning.*

2. **Cosine Similarity**
   - Measures **how similar two skills are in meaning**, not just the words.
   - If the angle between their vectors is small (similar), score goes up.

   > ✍️ *Cosine similarity = like checking if two thoughts are pointing in the same direction.*

3. **Education & Degrees**
   - If a resume contains your required degrees, extra points are given.
   - Advanced degrees = higher score (PhD > MS > BS).

4. **Experience**
   - Years of experience × 5 = score boost.

---

## 🛡️ Safety First

- `.env` contains your API key — never upload it.
- `.gitignore` takes care of hiding it and your real resume data.

---

## 🔮 Final Thoughts

> ✨ *This tool doesn’t just look at words... it tries to “understand” what you're looking for.*

You write the requirements — it does the matchmaking.

---

## dev: mustafaa🌹
