# Module 1 — Introduction to Python and Basic Operations

**Course:** Edumentry Python Fundamentals (AI-Era Track)  
**Duration:** ~3 hours (lecture + lab)  
**Prerequisites:** None  
**Next:** Module 2 — Variables, Data Types, and Type Conversion

---

# Slide 1 — Title

## Introduction to Python and Basic Operations

**Your destination:**  
Confident Python developer who can build, debug, and **verify AI-generated code** for:

- Backend / FastAPI  
- AI / LLM apps  
- Data & automation  
- DevOps scripting  

**Today:** the absolute foundation every path shares.

---

# Slide 2 — How This Curriculum Works (AI Era)

### Old mindset
"Memorize syntax → pass exam."

### Our mindset
```
UNDERSTAND → TRACE → PREDICT → VERIFY → WRITE → APPLY
```

**Vibe coding is a power tool — not a substitute for thinking.**

In interviews and jobs you will be asked:

1. What does this code do?  
2. Why is it wrong?  
3. How do you fix it?  
4. How would you use this in an API / AI pipeline?

AI can draft code. **You** must own correctness.

---

# Slide 3 — Learning Objectives

By the end of this module you will:

1. Explain why Python dominates AI + backend careers  
2. Install Python and run REPL + `.py` scripts  
3. Use `print()` like a professional debugging tool  
4. Use `input()` and understand the "always string" rule  
5. Perform all basic arithmetic operators  
6. Write comments that explain **why**  
7. Read beginner error messages  
8. Map each concept to FastAPI / AI / automation previews  

---

# Slide 4 — WHY Python in 2026?

| Role | Why Python |
|------|------------|
| Backend (FastAPI) | Fast APIs, clear code, huge ecosystem |
| AI / LLM apps | PyTorch, LangChain, Hugging Face, OpenAI SDKs |
| Data Science | Pandas, NumPy, notebooks |
| Automation / DevOps | Scripts, CI hooks, infra glue |

**Interview angle:**  
"Python is the common language across AI and backend teams."

---

# Slide 5 — WHAT Is Python?

High-level, **interpreted**, dynamically typed language (Guido van Rossum, 1991).

| Trait | Meaning for you |
|-------|-----------------|
| Readable | Easier code reviews + AI collaboration |
| Interpreted | Instant feedback while learning |
| Huge libraries | Same language from script → production API |

**Always use Python 3** (Python 2 is dead).

```bash
python --version
# expect: Python 3.x
```

---

# Slide 6 — Setup (Your Professional Toolkit)

1. Install Python 3 + **Add to PATH** (Windows)  
2. Editor: VS Code **or Cursor** (AI-assisted)  
3. Verify:

```bash
python --version
pip --version
```

**venv preview** (every real project uses this later):

```bash
python -m venv .venv
```

**AI-era tip:** Use Cursor/ChatGPT to *explain* errors — then fix them yourself.

---

# Slide 7 — Two Ways to Run Code

### REPL (experiment)
```bash
python
>>> print("hi")
```

### Script (real work)
```bash
python hello.py
```

| REPL | Script |
|------|--------|
| Quick checks | Projects, APIs, AI jobs |
| Line by line | Full programs |

**Career link:** FastAPI apps and AI training scripts are always `.py` files / modules.

---

# Slide 8 — Hello, World! + WHY It Matters

```python
print("Hello, World!")
```

Looks tiny. Mentally it is:

```
program → output channel → human / log / terminal
```

**Real-world cousins:**

| Today | Later |
|-------|-------|
| `print("Server started")` | FastAPI startup log |
| `print("Model loaded")` | AI inference script |
| `print("Job done")` | Automation / cron |

---

# Slide 9 — print() as a Debugging Superpower

```python
print("Welcome to Python!")
print("Score:", 95, "Grade:", "A")
print("2026", "07", "23", sep="-")
print("Loading", end="...")
print(" Done!")
```

### AI / API applications (preview)

```python
# Debugging an AI pipeline (concept)
print("[INFO] prompt received")
print("[INFO] tokens used:", 120)

# Debugging an API handler (concept)
print("[DEBUG] request path:", "/users")
```

**Interview skill:** When AI-generated code fails, your first move is often strategic `print`s (or a logger later).

---

# Slide 10 — Trace print()

```python
print("A", "B", sep="-")
print("X", end="")
print("Y")
```

**Trace:**

1. Prints `A-B` then newline  
2. Prints `X` with no newline  
3. Prints `Y` then newline  

**Output:**
```
A-B
XY
```

Ask class: predict before running. This is how you verify AI output.

---

# Slide 11 — Comments: Talk to Humans (and Future You)

```python
# Explain WHY, not obvious WHAT
temperature_c = 36  # sensor reading in Celsius
```

**AI-era rule:**  
If AI writes clever code you don't understand — **don't ship it**. Add comments only after you understand.

Docstrings (preview):

```python
"""Module: startup demo for beginners."""
```

---

# Slide 12 — Arithmetic: The Language of Metrics

```python
a, b = 10, 5
a + b    # 15
a - b    # 5
a * b    # 50
a / b    # 2.0  float division
a // b   # 2    floor
a % b    # 0    remainder
a ** b   # 100000
```

### Where this appears later

| Concept | Real application |
|---------|------------------|
| `/` `*` | API pricing, token cost estimates |
| `//` `%` | Pagination (`page // size`), batching |
| `% 2` | Even/odd checks, alternating tasks |
| `**` | Growth, compound metrics |

**FastAPI preview (idea only):**  
`total = price * quantity` inside a billing endpoint.

**AI preview:**  
`cost = tokens * price_per_token`

---

# Slide 13 — Trace Arithmetic (Interview Style)

```python
items = 17
batch = 5
print(items // batch)  # full batches
print(items % batch)   # leftover
```

**Trace:** 17 = 5×3 + 2 → `3` and `2`

This exact pattern appears in:

- splitting training data into batches  
- chunking API uploads  
- DevOps disk/alert thresholds  

---

# Slide 14 — input(): Receiving Data

```python
name = input("Enter name: ")
print("Hello,", name)
```

**Critical rule:** `input()` **always returns `str`**.

```python
age = input("Age: ")  # user types 25
# age is "25" not 25
```

### Real-world cousins

| Today | Later |
|-------|-------|
| `input()` | CLI args, forms, chat prompts |
| typed text | FastAPI request body / query params |
| user prompt | LLM user message string |

**Pattern forever:**  
`receive → convert/validate → process → respond`

---

# Slide 15 — The Classic Trap (Must Master)

```python
a = input("First: ")   # "5"
b = input("Second: ")  # "3"
print(a + b)           # "53"  ❌
```

Fix (Module 2 deep dive; preview now):

```python
a = int(input("First: "))
b = int(input("Second: "))
print(a + b)           # 8 ✅
```

**Interview favorite.** Also a common AI-generated bug if types are ignored.

---

# Slide 16 — Mini Program: Receive → Process → Respond

```python
# Conceptual API-shaped script
name = input("User: ")
print("status: ok")
print("message: welcome", name)
```

Same shape as:

```text
HTTP request → handler → JSON response
Chat message → AI function → answer
```

You are learning software architecture with 3 lines.

---

# Slide 17 — Indentation Preview

```python
if True:
    print("inside")
print("outside")
```

Python uses **indentation** instead of `{}`.

Wrong indent → `IndentationError`  
AI tools sometimes mis-indent — you must spot it.

---

# Slide 18 — Reading Errors Like a Pro

| Error | Meaning |
|-------|---------|
| `SyntaxError` | Typo / missing `:` `()` |
| `NameError` | Used name before creating it |
| `TypeError` | Wrong types together (`5 + "a"`) |
| `IndentationError` | Spacing wrong |

**Method:**

1. Read **last line** of traceback  
2. Jump to the file/line  
3. Fix → rerun  

This skill beats "ask AI to rewrite everything."

---

# Slide 19 — AI-Era Workflow (Practice This Forever)

```
1. State the goal in plain English
2. Write or generate a small draft
3. TRACE expected output on paper
4. RUN and compare
5. If mismatch → debug with prints / errors
6. Only then accept the code
```

**Confidence = verification ability.**

---

# Slide 20 — Map of Where You're Going

```
Module 1  print/input/math     → logs, prompts, metrics
Module 2  types/casting        → request validation
Module 3  strings              → prompts, JSON text, paths
...
Later     FastAPI / AI SDKs    → production systems
```

We go **sequential**. No skipping. Strong roots → strong AI usage.

---

# Slide 21 — Common Beginner Mistakes

1. Ignoring that `input()` is always `str`  
2. Using `/` vs `//` incorrectly  
3. Shipping AI code you cannot explain  
4. Fear of error messages  
5. Writing comments that restate the obvious  

---

# Slide 22 — Interview Warm-Ups

Be ready to answer:

1. Why Python for AI/backend?  
2. Difference between REPL and script?  
3. Output of `"5" + "3"` vs `5 + 3`?  
4. What does `%` do?  
5. How do you debug a wrong print?

---

# Slide 23 — Concept Recap

- Python 3 + ecosystem powers AI & APIs  
- REPL vs script  
- `print` / `sep` / `end`  
- comments  
- `+ - * / // % **`  
- `input` → always `str`  
- errors are teachers  
- verify everything (especially AI drafts)  

---

# Slide 24 — Syntax Cheat Sheet

```python
print("a", "b", sep="-", end="\n")
name = input("Name: ")
print(10 // 3, 10 % 3, 2 ** 3)
# comment
```

---

# Slide 25 — Lab Directions

1. Study `module.py`  
2. Complete `module_exercises.md` (all levels)  
3. Take `module_quiz.json`  
4. Bonus: ask an AI for a snippet, then **trace + verify** it yourself  

---

# Slide 26 — What “Confident” Looks Like After Module 1

You can:

- Run Python without fear  
- Predict simple program output  
- Spot the `input()` string trap  
- Use arithmetic for real metrics  
- Debug with prints and error reading  
- Explain how today’s ideas show up in APIs/AI later  

---

*End of Module 1 teaching slides (AI-Era Track)*
