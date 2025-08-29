import subprocess
import time
import os

# The exact path to the Gemini CLI executable found via the 'where' command.
GEMINI_EXECUTABLE_PATH = r"C:\Users\DELL\AppData\Roaming\npm\gemini.cmd"

PROMPT_FILE = "prompt.md"
POLL_INTERVAL = 0.2  # 200ms


def start_gemini_process():
    """Starts the gemini CLI as a persistent subprocess."""
    print("Starting gemini CLI process...")
    if not os.path.exists(GEMINI_EXECUTABLE_PATH):
        print(f"--- FATAL ERROR ---")
        print(f"Gemini executable not found at the specified path:")
        print(f"  {GEMINI_EXECUTABLE_PATH}")
        print(f"Please update the GEMINI_EXECUTABLE_PATH variable in bridge.py")
        exit(1)

    process = subprocess.Popen(
        [GEMINI_EXECUTABLE_PATH],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,  # Use text mode for easier I/O
        bufsize=1,  # Line-buffered
    )
    print("Gemini CLI process started successfully.")
    return process


if __name__ == "__main__":
    print(f"Monitoring {PROMPT_FILE} for changes...")
    last_mod_time = 0
    gemini_process = start_gemini_process()
    try:
        while True:
            try:
                current_mod_time = os.path.getmtime(PROMPT_FILE)
                if current_mod_time > last_mod_time:
                    print(f"Change detected in {PROMPT_FILE}.")
                    last_mod_time = current_mod_time
            except FileNotFoundError:
                # Don't spam the console if the file doesn't exist yet
                pass
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print("\nShutting down bridge...")
        gemini_process.terminate()
        gemini_process.wait()
        print("Bridge shut down.")
