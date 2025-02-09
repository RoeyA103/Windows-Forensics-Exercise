# Welcome to My GitHub!

### Brief Introduction

I started practicing on HTB Sherlock, and after solving a few exercises, I thought to myself, "Why don't I make one myself?" So, I present to you my first exercise! I hope you enjoy it.(I wanted to upload the full Memory Dump file, but due to size restrictions, I only uploaded 2 images of it.)


# Backdoor 🚨

Test your forensic and incident response skills in this investigative
challenge!

## 🕵️ Scenario

A cyber incident has occurred on a Windows machine, where a hacker
infiltrated the system and left traces of malicious activity. Your
mission is to uncover the attack vector, identify persistence
mechanisms, track attacker connections, and find the malicious payload.

## 🎯 Objectives

Identify the vulnerable service used for the attack.

Analyze attacker tools and tactics.

Track network connections established by the attacker.

Detect persistence methods and registry changes.

Extract critical forensic artifacts including usernames and passwords.

## 🧩 Exercise Details

You will receive the following investigation artifacts:

Memory Dump: "windows.pslist.Pslist.txt" + "windows.netstat.NetStat.txt"  extracted by Volatility.

Sysmon Logs: Investigate attacker events.

Registry Comparison Files: Identify persistence mechanisms.

PCAP File: Examine network communications.

Security Event Logs: Uncover unauthorized user creation.

## 🛠️ Tools Recommended


Wireshark (for PCAP analysis)

Event Viewer (for log inspection)

Your investigative intuition!

## 🚀 How to Start

Run the interactive forensic challenge script:

python3 challenge.py

Follow the prompts, provide your answers, and use hints when needed.

### 💡 Hints

Use \"hint\" during the questions to get clues about the answers. Think
creatively and explore different angles during your investigation.

### 📬 Submitting Your Solution

When you\'ve solved all questions, feel free to share feedback or your
experience at roey6922@gmail.com.

### Good luck and happy investigating! 🕵️‍♂️
