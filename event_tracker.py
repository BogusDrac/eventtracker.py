import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import json
import os
from plyer import notification

DATA_FILE = "events.json"

#------------Helper functions-------------
def load_events():
    #loads saved events from the JSON file.
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return[]

def save_events(events):
    #save all events back to events.json
    with open(DATA_FILE, "w") as f:
        json.dump(events, f, indent=4)

def notify(events):
    #send notifications for today's events.
    today = datetime.now().strftime("%Y-%m-%d")
    for event in events:
        if event["date"] == today:
            notification.notify(
                title="Event Reminder!!!",
                message=f"{event['title']} - {event['note']}",
                timeout=10 
            )

            