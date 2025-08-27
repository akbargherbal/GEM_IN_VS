### **`app_summary.md`**

**Project Name:** The Gemini CLI VS Code Bridge

**One-Line Description:** A background utility that connects a live, interactive Gemini CLI session to a set of text files, allowing a developer to use VS Code as the primary interface for the CLI.

**Target User:** A developer who is highly proficient and comfortable within the VS Code environment but finds the standard terminal to be a high-friction interface for reading and writing. They want to leverage the power of the stateful, conversational Gemini CLI without disrupting their established workflow.

**The Problem It Solves:**
The Gemini CLI is a powerful tool, but its terminal-based UI is not conducive to writing complex, multi-line prompts or reading long, formatted responses. This forces the user out of their preferred development environment (VS Code), breaking their concentration and slowing them down. This project eliminates that friction entirely.

**Core Value Proposition:**
The bridge allows the user to have a complete, stateful, and context-aware conversation with the Gemini CLI without ever leaving VS Code. It transforms the CLI interaction model from a clunky terminal session into a seamless, file-based workflow, dramatically improving efficiency and user experience.

---

### **`visual_mockup.md`**

**Mockup Type:** File I/O Simulation
**Description:** This mockup simulates the user's experience within VS Code. The user interacts with two files in their editor panel: `prompt.md` (for writing) and `response.md` (for reading).

#### **Scenario: A two-prompt conversation**

**1. User writes the first prompt and saves the file.**

The user's VS Code window looks like this:

| `prompt.md`                | `response.md`      |
| :------------------------- | :----------------- |
| `markdown_# What is HTMX?` | `markdown_(empty)` |

**2. A few moments later, the bridge script catches the change and appends Gemini's response.**

The user's VS Code window now looks like this:

| `prompt.md`                | `response.md`                                                                                                                                                                                                               |
| :------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `markdown_# What is HTMX?` | `markdown_HTMX is a library that allows you to access modern browser features directly from HTML, rather than using javascript. It enables you to build modern user interfaces with the simplicity and power of hypertext.` |

**3. User clears the prompt file, writes a follow-up question, and saves.**

The user's VS Code window now looks like this:

| `prompt.md`                                                    | `response.md`                                                                                                                                                                                                               |
| :------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `markdown_Why is it a good fit for a Python/Django developer?` | `markdown_HTMX is a library that allows you to access modern browser features directly from HTML, rather than using javascript. It enables you to build modern user interfaces with the simplicity and power of hypertext.` |

**4. The bridge appends the new response to the `response.md` file.**

The user's final VS Code window looks like this, showing the complete, appended log of responses:

| `prompt.md`                                                    | `response.md`                                                                                                                                                                                                                |
| :------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `markdown_Why is it a good fit for a Python/Django developer?` | ```markdown_HTMX is a library that allows you to access modern browser features directly from HTML, rather than using javascript. It enables you to build modern user interfaces with the simplicity and power of hypertext. |

It's an excellent fit for Django developers because it aligns perfectly with the server-side rendering paradigm. You can keep all your rendering logic, state management, and business logic in Python on the backend, and simply send HTML snippets over the wire, which HTMX will seamlessly place in the DOM. This avoids the need for a complex frontend JavaScript framework like React or Vue.``` |

---

### **`feature_list.md`**

**Description:** A comprehensive "brain dump" of all desired features for the Gemini CLI VS Code Bridge, to be prioritized in Stage 3 of the planning process.

#### **Core Functionality (MVP)**

- The script must launch the `gemini` command as a persistent, background subprocess.
- The script must capture the `stdin` and `stdout` of the `gemini` process.
- The script must watch a designated `prompt.md` file for modifications.
- Upon detecting a change, the script must read the entire content of `prompt.md` and pipe it to the `gemini` process's `stdin`.
- The script must continuously listen to the `gemini` process's `stdout`.
- The script must append any output received from `stdout` to a designated `response.md` file.
- The script must handle a clean shutdown (e.g., via `Ctrl+C`), terminating the child `gemini` process.

#### **Enhanced Features & Quality of Life (Post-MVP)**

- **Robust Error Handling:** Capture the `stderr` stream from the Gemini process and append any errors to `response.md` with a clear `[ERROR]:` marker.
- **Configuration File:** Use a simple `.json` or `.ini` file to configure the names of the prompt and response files, instead of hardcoding them.
- **Session Management:** Implement a special command (e.g., `/new_session`) that, when typed into `prompt.md`, will terminate the current `gemini` process and start a fresh one, clearing the conversational context without restarting the bridge script itself.
- **Status Logging:** Provide clear, real-time status updates in the terminal window where the bridge script is running (e.g., "Bridge started," "Detected change in prompt.md," "Wrote response to response.md").
- **"Typing" Indicator:** As a stretch goal, write a temporary "Gemini is typing..." message to `response.md` when a prompt is received and remove it when the final answer is appended.
- **Startup Check:** On startup, check if `gemini` is a valid command and is available in the system's PATH, providing a clear error message if it's not found.
