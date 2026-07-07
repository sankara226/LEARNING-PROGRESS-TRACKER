# 02 — Prompt Quality Checker

**Type:** Interactive HTML artifact
**File:** `prompt-quality-checker.html`

## What it does

Paste any prompt and instantly get scored on the **3-ingredient quality framework**:

| Ingredient | What it measures |
|---|---|
| **Context** | Does the prompt set the scene? Role, situation, constraints, goal. |
| **Task** | Is the ask clear? Strong action verb, scope, success criteria. |
| **Format** | Is the output shape defined? List, table, length, code block, etc. |

Each criterion is scored 1–10, plus an overall score and a personalized list of actionable tips.

## Scoring logic

The scorer uses **weighted pattern matching** against 8 signals per criterion:

- **Context signals**: role assignment (`"You are a..."`), expertise level, goal statement, audience mention, constraint keywords
- **Task signals**: creation/analysis/improvement verbs, specificity adverbs, exclusion clauses (`"do not"`, `"avoid"`), scope-narrowing phrases
- **Format signals**: list/table/JSON keywords, length constraints (`"brief"`, `"under 200 words"`), section/heading references, output-only requests

Scores are normalized across all signals and clamped to 1–10. A length bonus rewards prompts that are specific enough to carry real information (>60 characters).

**Color coding:**
- Green (7–10): strong
- Yellow (4–6): could be improved
- Red (1–3): needs work

## How to use

1. Open `prompt-quality-checker.html` in any browser.
2. Paste your prompt in the textarea.
3. Click **Score My Prompt** (or press `Ctrl+Enter` / `Cmd+Enter`).
4. Read the per-criterion scores and the "How to improve" tips.
5. Revise your prompt, paste it again, and watch the score go up.

## Example prompts to try

**Weak:** `tell me about python`

**Strong:** `You are a senior Python developer. I'm a beginner who just learned loops. Explain list comprehensions in 3 bullet points with one code example each. Keep it under 200 words.`
