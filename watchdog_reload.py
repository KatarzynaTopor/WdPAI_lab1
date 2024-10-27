from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import subprocess

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(self.command, shell=True)

    def on_modified(self, event):
        # Check if the modified file is a Python, CSS, JS, or HTML file
        if event.src_path.endswith((".py", ".css", ".js", ".html")):
            print(f"Detected change in {event.src_path}. Restarting server...")
            self.process.terminate()  # Stop the current server process
            self.process = subprocess.Popen(self.command, shell=True)  # Restart the server

if __name__ == "__main__":  
    path = "."  # Monitor the current directory
    command = "python python_server/server.py"  # Replace with your server command

    event_handler = ChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    print(f"Starting server with hot reload at {path}")
    observer.start()

    try:
        while True:
            time.sleep(1)  # Keep the script running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
