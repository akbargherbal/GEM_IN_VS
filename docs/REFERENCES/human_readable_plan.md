
# Gemini CLI Bridge – Easy-to-Understand Project Tracker

**Last Updated:** August 28, 2025  
**Project Phase:** Kickoff (Starting Point)

---

## 1. What This Document Is

This document is the official guide for tracking our progress as we build the **Gemini CLI VS Code Bridge**.  

If something in the plan needs to change:
1. The AI Assistant will point it out and suggest an update.
2. We check how that update affects the rest of the plan.
3. The Developer must approve the change.
4. The main plan is updated first.
5. Then, this tracker is updated.

This keeps everything aligned – no confusion about what's correct.

---

## 2. Where We Are Now

- **Progress:** 0% – just starting.  
- **Current Phase:** Phase 1 – Building the Core Connection (Week 1).  
- **Today’s Focus:** Start with Task 1 – Getting the Gemini tool to run and stay open.  
- **Project Setup:** Basic folder and files still need to be created.

---

## 3. Work Breakdown (By Phase)

### Phase 1: Core Connection (Week 1)

**Goal:**  
Get the simplest version of the tool running. A user can write something in `prompt.md`, and the response shows up in `response.md` – keeping context for multiple turns.

**What we need before starting (Entry Criteria):**
- Python 3.8 or higher installed.  
- Gemini command-line tool installed and logged in.  
- Starter files created: `bridge.py`, `prompt.md`, `response.md`.

**When we know we’re done (Exit Criteria):**
- Can have a 5-turn back-and-forth conversation using only file edits.  
- All features for this phase work and pass simple tests.  
- All main logic is inside one file: `bridge.py`.

**Tasks:**
1. **Persistent Gemini Process (0.5 days)** – Get the Gemini tool running as a background process.  
2. **File Watcher (1 day)** – Check `prompt.md` every 0.2 seconds and notice when it changes.  
3. **Data Bridge (2 days)** – Send prompt text into Gemini and capture the output.  
4. **Response Logging (1 day)** – Add Gemini’s responses to `response.md` without erasing old text.

**Quality Checks (Quality Gates):**
- Try a manual 5-turn conversation and confirm it works.  
- Code formatted neatly.  
- Small automated tests confirm file handling and timing logic.

---

### Phase 2: Reliability & Hardening (Week 2)

**Goal:**  
Make the tool stable for daily use – handle crashes, restarts, and cross-platform issues.

**Tasks:**  
- Detect if Gemini crashes and restart it automatically.  
- Shut down cleanly if user presses `Ctrl+C`.  
- Create missing files automatically.  
- Test on both Windows and macOS/Linux.

**Quality Checks:**  
- Over 60% of code tested.  
- All major bugs caught before release.  
- Manual tests confirm crash recovery, shutdown, and file creation.

---

### Phase 3: Documentation & Release (Week 3)

**Goal:**  
Prepare for public use – clear instructions, strong test coverage, and final polish.

**Tasks:**  
- Increase test coverage to at least 85%.  
- Write a beginner-friendly `README.md` so new users can start in under 5 minutes.  
- Add helpful comments to tricky code and ensure style consistency.

**Final Quality Checks:**  
- Manual test of full setup using only the README.  
- All tests pass with high coverage.

---

## 4. Possible Risks

- **High:** Process output might get “stuck” because of how different operating systems handle it.  
  - **Plan:** Test early on Windows and macOS/Linux.  

- **Medium:** Gemini tool might crash or change unexpectedly.  
  - **Plan:** Add restart logic in Phase 2.

---

## 5. Quick Start Guide for a Work Session

```

Project: Gemini CLI VS Code Bridge
Phase: Phase 1 – Core Connection
Task: See tracker for current task
Tech: Python 3.8+, Gemini CLI, file monitoring
Goal: Watch prompt.md → Send to Gemini → Save reply to response.md

```

---

## 6. Current Folder Plan

```

gemini-bridge/
├── PROJECT\_TRACKER.md     # This tracker
├── bridge.py              # Main script (to be created)
├── prompt.md              # User input file
├── response.md            # Gemini responses
├── README.md              # User guide (later phase)
├── requirements.txt       # Needed Python tools (to be created)
└── tests/
└── test\_bridge.py     # Automated tests (Phase 1)

```

---

## Next Steps
- Start Task 1: Run Gemini tool as a persistent process.  
- Create initial project structure.  
