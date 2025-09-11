from datetime import datetime

mood = input("How are you feeling today (e.g., happy, tired)?")
entry =input("Write a short entry about your day:")

today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
journal_entry = f"""Date: {today}
Mood: {mood}
Entry: {entry}
{'-'*40}
"""

with open("journal.txt","a", encoding= "utf-8") as file:
    file.write(journal_entry)

print("Your entry has been saved to journal.txt!")
