import subprocess
import time


def start_gemini_process():
    """Starts the gemini CLI as a persistent subprocess."""
    print("Starting gemini CLI process...")
    process = subprocess.Popen(
        ["gemini"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,  # Use text mode for easier I/O
        bufsize=1,  # Line-buffered
    )
    print("Gemini CLI process started successfully.")
    return process


if __name__ == "__main__":
    gemini_process = start_gemini_process()
    try:
        while True:
            # Keep the script alive to maintain the subprocess
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down bridge...")
        gemini_process.terminate()
        gemini_process.wait()
        print("Bridge shut down.")
