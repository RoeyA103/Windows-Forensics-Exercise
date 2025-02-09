print("Welcome to the Forensic Investigation Challenge! 🚨\n")
print("Submit your answers and test your incident response skills.\nLet's see if you can solve the case step by step! 💻🔍\n")
print("In every question (except questions 2,5) you can write the word \"hint\" to get a hint to the answer.\nGood luck\n")
print("If you have already answered questions\nyou can find them in question_memory.json\nOr you can delete it and start over")

# Load and save answered questions
import json

FILENAME = "question_memory.json"

# Load existing answered questions from file if available
def load_memory():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Save updated memory back to file
def save_memory(memory_list):
    with open(FILENAME, "w") as file:
        json.dump(memory_list, file)

# Main list for storing answered questions
answered_questions = load_memory()

def memory(question_text):
    """Store answered questions in the list and save to file if not already present."""
    if question_text not in answered_questions:
        answered_questions.append(question_text)
        save_memory(answered_questions)
        print("Question added to memory.")
    else:
        print("Question already in memory.")

questions = [
    {"text": "Question 1: What is the name of the vulnerable SMTP server?\nm******.exe", "answer": "mercury.exe", "id": "Question 1:mercury.exe", "hint": "\"windows.pslist.Pslist.txt\"."},
    {"text": "Question 2: what is its PID?\n****", "answer": "1004", "id": "Question 2:1004", "hint": None},
    {"text": "Question 3: Can you find the processes related to mercury?\np*********.exe", "answer": "powershell.exe", "id": "Question 3:powershell.exe", "hint": "The first two columns indicate the PID and PPID. Filter for PID 1004 and search it in PPID."},
    {"text": "Question 4: The \"mercury\" has created a connection to a specific IP. Can you find it and the port?\nip,port", "answer": "192.168.47.132,4444", "id": "Question 4:192.168.47.132,4444", "hint": "windows.netstat.NetStat.txt"},
    {"text": "Question 5: Now can you find if there was another connection through the process you found in question 3?\nip,port", "answer": "192.168.47.132,5555", "id": "Question 5:192.168.47.132,5555", "hint": None},
    {"text": "Question 6: Can you find out which attack tool the attacker used?\nm*********", "answer": "metasploit", "id": "Question 6:metasploit", "hint": "Investigate SysmonLog and filter for event ID 3 and look for \"RuleName\""},
    {"text": "Question 7: What is the ProcessGuid that appears in the powershell connection?\na3bd57c0-****-****-****-***********", "answer": "a3bd57c0-35b9-679b-bc01-000000002600", "id": "Question 7:a3bd57c0-35b9-679b-bc01-000000002600", "hint": "Leave the filter for network connection and search for powershell."},
    {"text": "Question 8: What is the event ID of the hushdump?", "answer": "8", "id": "Question 8:8", "hint": "Search for SourceProcessId 6576 in the logs."},
    {"text": "Question 9: Now let's find the persistent backdoor in the registry.", "answer": "hku\\s-1-5-21-3076537077-2267025316-4006280282-1000\\software\\microsoft\\windows\\currentversion\\run\\poa0xjvc", "id": "Question 9:hku\\s-1-5-21-3076537077-2267025316-4006280282-1000\\software\\microsoft\\windows\\currentversion\\run\\poa0xjvc", "hint": "Search for \"Run\" in the registry comparison file."},
    {"text": "Question 10: What protocol did the attacker use to connect to another server?\n***", "answer": "ftp", "id": "Question 10:ftp", "hint": "analyze PCAP data Filter for the IPs you found in the previous questions.\n(look for Cleartext protocol)"},
    {"text": "Question 11: What is the username that the attacker managed to obtain?\n***", "answer": "dan", "id": "Question 11:dan", "hint": "Go to the PCAP file and filter FTP. Right-click -> Follow -> TCP stream."},
    {"text": "Question 12: Password?\n******", "answer": "dandan", "id": "Question 12:dandan", "hint": "Go to the PCAP file and filter FTP. Right-click -> Follow -> TCP stream."},
    {"text": "Question 13: What is the name of the file the attacker uploaded via FTP?\n***_*_*****.***", "answer": "not_a_virus.exe", "id": "Question 13:not_a_virus.exe", "hint": "Go to the PCAP file and filter FTP. Right-click -> Follow -> TCP stream."},
    {"text": "Question 14: What username did the attacker create to maintain access?", "answer": "hacker", "id": "Question 14:hacker", "hint": "Filter event ID 4720 in the security log."}
]

# Skip already answered questions and continue
for question in questions:
    if question["id"] not in answered_questions:
        while True:
            print(question["text"])
            try:
                user_input = input("Enter your answer: ").strip().lower()
                if user_input == "hint" and question["hint"]:
                    print(question["hint"])
                elif user_input != question["answer"].lower():
                    print("Wrong answer, try again.")
                else:
                    print("Correct answer!")
                    memory(question["id"])
                    break
            except Exception:
                print("Unexpected error. Please try again.")
else:
    print("You have answered all questions.")
