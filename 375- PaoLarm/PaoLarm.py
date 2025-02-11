import time
from datetime import datetime

alarm_time = input("Enter alarm time (HH:MM): ")

def trigger_alarm():
    print("🔔 ALARM RINGING! Solve this challenge to stop it.")
    challenge = "The quick brown fox jumps over the lazy dog"
    print(f"Read this sentence: {challenge}")

    while True:
        user_input = input("Type the sentence to stop the alarm: ")
        if user_input.strip().lower() == challenge.lower():
            print("✅ Correct! Alarm stopped.")
            break
        else:
            print("❌ Incorrect! Try again.")

while True:
    now = datetime.now().strftime("%H:%M")
    if now == alarm_time:
        trigger_alarm()
        break
    time.sleep(30)
