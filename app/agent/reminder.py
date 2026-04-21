import threading
import time

reminders = []


def add_reminder(text, delay_sec):
    reminders.append((text, time.time() + delay_sec))


def start_reminder_loop():

    def loop():
        while True:
            now = time.time()

            for r in reminders[:]:
                text, t = r
                if now >= t:
                    print("🔔 REMINDER:", text)
                    reminders.remove(r)

            time.sleep(1)

    thread = threading.Thread(target=loop, daemon=True)
    thread.start()