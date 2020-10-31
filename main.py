from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time

downloadsFolder = r'C:\Users\Windows\Downloads'


class DownloadsFolderListener(FileSystemEventHandler):
    def on_modified(self, event):
        for file in os.listdir(downloadsFolder):
            parts = file.split('.')
            length = len(parts)

            directoryPath = downloadsFolder + "\\" + parts[length - 1]

            if not os.path.exists(directoryPath):
                os.makedirs(directoryPath)

            try:
                os.rename(downloadsFolder + "\\" + file, directoryPath + "\\" + file)
            except PermissionError as error:
                pass


event_handler = DownloadsFolderListener()
observer = Observer()
observer.schedule(event_handler, downloadsFolder, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
