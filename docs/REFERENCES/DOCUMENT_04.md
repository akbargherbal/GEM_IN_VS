# Development Execution Plan: Gemini CLI VS Code Bridge

## Execution Overview

- **Total Development Timeline**: 3 weeks
- **Development Phases**: 3 phases
- **Key Technical Risks**:
  1.  Platform-specific differences in subprocess `stdout` buffering.
  2.  Unexpected instability or changes in the `gemini` CLI tool.
  3.  CPU usage of the polling loop on low-power devices.
- **Success Validation Strategy**: Progress will be measured by completing the phased feature list, validated by a `pytest` suite with >=85% coverage and successful execution of the core 5-turn conversation user journey.

## Sprint/Milestone Structure

### Phase 1: Core Workflow "Steel Thread" - Week 1

**Goal**: Implement the absolute minimum functionality to validate the core user journey: a user can save a prompt in `prompt.md` and see a stateful response appear in `response.md`.
**Duration**: 5 days
**Entry Criteria**:

- Python >= 3.8 installed.
- `gemini` CLI tool installed and authenticated.
- `bridge.py`, `prompt.md`, `response.md` files created.

**Exit Criteria**:

- A 5-turn contextual conversation with the `gemini` CLI can be completed successfully using only file edits.
- All Phase 1 features are implemented and pass basic manual tests.
- The core logic is contained within a single `bridge.py` script.

**Key Features/Tasks**:

- **[P1.T1] Persistent Gemini CLI Process Launch** (Est: 0.5 days)
  - **Acceptance Criteria**: The `bridge.py` script successfully starts the `gemini` command as a long-running child process using `subprocess.Popen`. The process's `stdin` and `stdout` are piped.
  - **Dependencies**: None.
  - **Risk Level**: Low.
- **[P1.T2] Input File (`prompt.md`) Monitoring** (Est: 1 day)
  - **Acceptance Criteria**: The script checks the modification time of `prompt.md` every 200ms. A change is detected reliably.
  - **Dependencies**: None.
  - **Testing Requirements**: Unit test to verify that a file modification updates the internal state.
- **[P1.T3] Stdin/Stdout Bridging** (Est: 2 days)
  - **Acceptance Criteria**: When a file change is detected, the full content of `prompt.md` is written to the `gemini` process's `stdin`. Data from the process's `stdout` is read in a non-blocking manner.
  - **Dependencies**: P1.T1, P1.T2.
  - **Risk Level**: Medium - This is where I/O buffering issues may first appear.
- **[P1.T4] Append-Only Output Logging (`response.md`)** (Est: 1 day)
  - **Acceptance Criteria**: All data read from the `gemini` process's `stdout` is immediately appended to `response.md`. The file is never overwritten.
  - **Dependencies**: P1.T3.
  - **Testing Requirements**: Unit test to ensure file is opened in append mode and content is written correctly.

**Quality Gates**:

- [ ] Manual test: A 5-turn conversation is completed successfully.
- [ ] Code is formatted with `black`.
- [ ] Basic unit tests for file I/O and time checking are written.

**Risk Mitigation**:

- **Risk**: The core loop feels unresponsive due to I/O blocking.
- **Mitigation**: Implement non-blocking reads for `stdout` from the beginning. Validate responsiveness at the end of each day.
- **Contingency**: If non-blocking reads are problematic, increase the polling interval slightly (e.g., to 300ms) as a temporary measure.

---

### Phase 2: Reliability & Hardening - Week 2

**Goal**: Make the core workflow robust enough for daily, uninterrupted use by handling common errors and edge cases gracefully.
**Duration**: 5 days
**Entry Criteria**:

- All Phase 1 Exit Criteria are met.
- A functional "steel thread" prototype is committed to the `develop` branch.

**Exit Criteria**:

- The bridge automatically restarts the `gemini` process if it crashes.
- The script handles file creation and exits cleanly on `Ctrl+C`.
- The tool is verified to work on Windows and a primary Linux/macOS environment.
- Test coverage reaches at least 60%.

**Key Features/Tasks**:

- **[P2.T1] Process Crash Detection & Restart** (Est: 2 days)
  - **Acceptance Criteria**: The main loop checks `process.poll()`. If the process has terminated, it is restarted. Implement a simple backoff delay (e.g., 2s, 4s, 8s) for restarts. After 3 failed attempts, the script exits with an error.
  - **Dependencies**: Phase 1 implementation.
  - **Risk Level**: Medium - Logic can be tricky to test effectively.
- **[P2.T2] Graceful Shutdown (Ctrl+C)** (Est: 1 day)
  - **Acceptance Criteria**: Wrapping the main loop in a `try...finally` block ensures the child `gemini` process is terminated when the bridge script is stopped with `Ctrl+C`. No orphaned processes are left.
  - **Dependencies**: Phase 1 implementation.
  - **Testing Requirements**: Manual test is required to verify process termination.
- **[P2.T3] Automatic File Creation & UTF-8 Support** (Est: 1 day)
  - **Acceptance Criteria**: On startup, the script checks for `prompt.md` and `response.md` and creates them if they don't exist. All file I/O and subprocess communication explicitly uses `encoding='utf-8'`.
  - **Dependencies**: None.
  - **Testing Requirements**: Unit test with a temporary directory to verify file creation. Test with non-ASCII characters.
- **[P2.T4] Cross-Platform Validation** (Est: 1 day)
  - **Acceptance Criteria**: The full user journey is tested and confirmed to be working on both Windows and a Unix-like system (macOS or Linux).
  - **Dependencies**: All other Phase 2 tasks.
  - **Risk Level**: Medium - This is the primary mitigation for the `stdout` buffering risk.

**Quality Gates**:

- [ ] All unit tests passing with >60% coverage.
- [ ] Code review completed and approved.
- [ ] Manual testing checklist for crash recovery and shutdown completed on target platforms.

**Risk Mitigation**:

- **Risk**: Subprocess `stdout` buffering behaves differently on Windows vs. Linux/macOS.
- **Mitigation**: Dedicate a full day to testing on both platforms. Use a test prompt that generates a multi-line response to check if the output is captured completely and promptly.
- **Contingency**: Research platform-specific flags or libraries for managing non-blocking I/O if standard methods fail.

---

### Phase 3: Documentation & Release - Week 3

**Goal**: Finalize the tool for public use with clear documentation, high-quality code, and robust test coverage.
**Duration**: 3-5 days
**Entry Criteria**:

- All Phase 2 Exit Criteria are met.
- The tool is stable and functionally complete for the MVP scope.

**Exit Criteria**:

- A clear `README.md` is written with setup and usage instructions.
- Code is well-commented, especially the polling and subprocess logic.
- Final test coverage is >= 85%.
- A startup confirmation message is implemented.

**Key Features/Tasks**:

- **[P3.T1] Increase Test Coverage to >= 85%** (Est: 2 days)
  - **Acceptance Criteria**: Write `pytest` tests for process restart logic, edge cases in file handling, and error conditions. Use `pytest-mock` to isolate components.
  - **Dependencies**: All code from Phase 1 & 2.
- **[P3.T2] Write `README.md`** (Est: 1 day)
  - **Acceptance Criteria**: The `README` includes a project summary, setup steps, usage instructions (the side-by-side editor workflow), and a troubleshooting section. A new user can be operational in under 5 minutes.
  - **Dependencies**: None.
- **[P3.T3] Code Cleanup and Commenting** (Est: 1 day)
  - **Acceptance Criteria**: Add inline comments explaining complex parts (e.g., non-blocking reads, restart backoff). Ensure all code adheres to `black` and `pylint` standards. Implement the "Startup Confirmation Message" feature.
  - **Dependencies**: All code from Phase 1 & 2.

**Quality Gates**:

- [ ] All unit tests passing with >=85% coverage.
- [ ] `README.md` is reviewed by a peer for clarity.
- [ ] Final manual test of the full user journey using only the `README` for instructions.

**Risk Mitigation**:

- **Risk**: The project is "functionally done" but not "user-ready."
- **Mitigation**: Adhere strictly to the documentation and code cleanup tasks. The "test with the README" quality gate is non-negotiable.
- **Contingency**: If the timeline is tight, prioritize the `README` over reaching exactly 85% coverage, as user-facing documentation is more critical for release.

## Development Workflow

### Daily Development Process

**Morning Routine** (15 minutes):

1.  Pull the latest from the `develop` branch.
2.  Review the task board for today's highest priority task from the current phase.
3.  Run the existing test suite (`pytest`) to ensure a clean starting point.

**Core Development Cycle** (6-7 hours):

1.  **Create a Feature Branch**: `git checkout -b feature/[task-name]`
2.  **Test-Driven Implementation**:
    - Write a failing test in `tests/` that defines the acceptance criteria for the new feature.
    - Write the implementation code in `bridge.py` until the test passes.
    - Refactor the code for clarity and simplicity.
3.  **Run Full Suite**: Run `pytest --cov=bridge` to ensure no regressions and check coverage.
4.  **Format and Lint**: Run `black .` and `pylint bridge.py`.

**Evening Wrap-up** (15 minutes):

- Commit work with a conventional commit message.
- Push the feature branch.
- Open a Pull Request to `develop` for review.
- Update the task board with progress.

### Weekly Progress Validation

**End-of-Week Review** (Friday, 1 hour):

- Validate that all planned tasks for the week's phase are complete and merged to `develop`.
- Execute the manual testing checklist for the current phase.
- Review test coverage and address any significant gaps.
- Plan the next week's tasks based on the next phase's goals.

### Code Organization Strategy

#### Repository Structure```

gemini-bridge/
├── .gitignore
├── bridge.py # The main application script
├── prompt.md # User input file (created automatically)
├── response.md # Application output file (created automatically)
├── README.md # Project documentation
├── requirements.txt # For development dependencies (pytest, black)
└── tests/
    └── test_bridge.py # Unit and integration tests

```

#### Git Workflow
**Branch Strategy**:
- `main`: Contains only tagged, stable releases.
- `develop`: The primary integration branch. All feature branches merge here.
- `feature/[task-name]`: Individual branches for each task. E.g., `feature/P2.T1-process-restart`.

**Commit Standards**:
```

feat(P1.T1): Add automatic process restart with exponential backoff
fix(P1.T3): Correctly handle UTF-8 characters in prompt file
test(P2.T1): Add unit tests for file monitoring logic
docs(P3.T2): Update README with setup instructions

````

**Merge Process**:
1.  Develop on a `feature/` branch.
2.  Open a Pull Request against `develop`.
3.  PR must pass all automated checks (if any) and a peer review.
4.  Squash and merge into `develop`. Delete the feature branch.
5.  At the end of Phase 3, `develop` is merged into `main` and tagged as `v1.0`.

### Testing and Quality Assurance

#### Unit Testing Strategy
**Coverage Requirements**:
- **Core Logic (polling, file I/O)**: 90%+
- **Subprocess Management (start, restart)**: 80%+ (some parts are hard to unit test)
- **Overall Project**: 85%

**Testing Patterns**:
- Use `pytest` fixtures and the `tmp_path` fixture for all filesystem interactions.
- Use `pytest-mock`'s `mocker` fixture to patch `subprocess.Popen` and `time.sleep` to test logic without external dependencies or delays.

```python
// Example test for process restart
import pytest
from unittest.mock import MagicMock, patch

def test_restarts_crashed_process(mocker):
    """Ensures the bridge attempts to restart a terminated process."""
    # Arrange
    mocker.patch('time.sleep') # Prevent delays in tests
    mock_popen = mocker.patch('subprocess.Popen')

    # Simulate a process that has terminated (poll() returns a non-None value)
    mock_process = MagicMock()
    mock_process.poll.return_value = 1 # Crashed
    mock_popen.return_value = mock_process

    bridge = GeminiBridge() # Assumes logic is in a class

    # Act
    bridge.check_process_status()

    # Assert
    # It should have been called once to start, and once to restart.
    assert mock_popen.call_count == 2
````

#### Manual Testing Checklists

**Phase 1 (Core Workflow) Checklist**:

- [ ] Can start the script successfully.
- [ ] Writing "Hello" to `prompt.md` and saving results in a response in `response.md`.
- [ ] A follow-up question that relies on context gets a correct answer.
- [ ] A multi-line prompt is processed correctly.

**Phase 2 (Hardening) Checklist**:

- [ ] `Ctrl+C` terminates both the script and the child `gemini` process.
- [ ] Deleting `prompt.md` and `response.md` and restarting the script recreates them.
- [ ] Manually killing the `gemini` process causes the script to log a restart attempt.
- [ ] A prompt with emojis or non-ASCII characters (e.g., "你好") works correctly.
- [ ] All of the above works on both Windows and macOS/Linux.

## Risk Management Framework

### High-Risk Areas Requiring Special Attention

#### Technical Risks

**1. Subprocess I/O Buffering - Risk Level: HIGH**

- **Description**: Different operating systems buffer `stdout` from child processes differently. A response might be "stuck" in a buffer and not appear in `response.md` until the buffer is full or the process exits.
- **Impact**: The tool will feel broken or unresponsive, violating a core user requirement.
- **Early Warning Signs**: During Phase 1, responses appear delayed or incomplete.
- **Mitigation Strategy**:
  - Test on both Windows and macOS/Linux early in Phase 2.
  - Ensure the `gemini` CLI flushes its output stream (if it's a configurable option).
  - Implement non-blocking reads from the start.
- **Contingency Plan**: Research OS-specific solutions for unbuffered I/O or, as a last resort, switch to a temporary file-based output from the `gemini` process if it supports it.

**2. `gemini` CLI Instability - Risk Level: MEDIUM**

- **Description**: The external `gemini` tool may be buggy, crash frequently for reasons outside our control, or have breaking changes in an update.
- **Impact**: Our bridge will be unreliable, even if our code is perfect.
- **Mitigation Strategy**:
  - The process restart logic in Phase 2 is the primary mitigation.
  - Clearly document the required version of the `gemini` CLI in the `README`.
- **Contingency Plan**: Add more robust error logging to `response.md` to capture `stderr` from the child process, making it easier for users to diagnose issues.

#### Process Risks

**1. Scope Creep - Risk Level: LOW**

- **Description**: The simplicity of the tool might invite "just one more feature" requests (e.g., customizable filenames, timestamps).
- **Mitigation**: Adhere strictly to the "Scope Protection Framework" from the MVP document. Any new feature request is automatically deferred to a post-MVP v1.1.
- **Contingency**: Maintain a backlog of "Could Have" features to show that ideas are captured but not derailing the MVP.