# Project Title: Vital Signs Health Assessment Program


# 1) Overview:

This project is an user friendly yet functional command-line Python application that helps assess vital signs to determine the general health status of an individual. It prompts the user to enter four key indicators: respiratory rate, heart rate, blood pressure, and body temperature. Based on the values provided, the program evaluates whether each sign falls within a normal range or indicates a potential health concern. It also calculates a total score and provides health recommendations ranging from self-care to emergency actions accordingly.
This program is designed as part of a `CS50P final project` to demonstrate a practical understanding of Python programming, conditional logic, error handling, and user interaction.

# 2) Features:

- Respiratory Rate Check: Detects if breathing is slow (bradypnea), fast (tachypnea), or normal (eupnea).
- Heart Rate Analysis: Identifies if the heart rhythm is slow (bradycardia), fast (tachycardia), or a normal (eucardia).
- Blood Pressure Evaluation: Checks for low (hypotension), high (hypertension), or normal (eutension) blood pressure using systolic and diastolic input.
- Body Temperature Scan: Flags low (hypothermia), high (hyperthermia), or a healthy (euthermia) temperature.
- Score System: Assigns points based on vitals and gives a recommendation based on the final score.
- Emergency Detection: If either the respiratory or heart rate is zero, the program exits and advises CPR immediately.
- Error Handling: Gracefully handles invalid input using 'try/except' blocks and exits with a friendly message.

# 3) How It Works:

When executed, the user is prompted to input:
A. Respiratory rate: breaths per minute.
B. Heart rate: beats per minute.
C. Blood pressure in systolic/diastolic format (e.g., '120/80').
D. Body temperature in Fahrenheit (°F).

Each input is evaluated using separate functions, each of which adjusts a shared health *score* variable. If vitals are within normal ranges, the score is maintained the same. If the inputs values are outside healthy limits, points are subtracted.
The score thresholds are:
- Score < 6: Go to the ER or Call 911
- Score 6–9: Doctor visit is recommended
- Score > 9: All clear – Keep it up!
If the respiratory rate or heart rate is '0', the program stops and recommends immediate CPR using the standard 30:2 compression-to-breath ratio.

# 4) File Structure:

 project.py       # Main Program: Python script with all health logic
 README.md        # Project documentation (this file)
 test_project.py  # Unit tests for functions: pytest script to test health logic

# 5) Requirements:

- Python 3.x
- 'sys' module
- 'pytest' for testing
- No external packages required

# 6) Health Categories:

- *Respiratory Rate*: Bradypnea, Eupnea, Tachypnea
- *Heart Rate*: Bradycardia, Eucardia, Tachycardia
- *Blood Pressure*: Hypotention, Eutention, Hypertention
- *Body Temperature*: Hypothermia, Euthermia, Hyperthermia

# 7) Output Messages:

- `🚨 Start CPR(30:2) 🧰` — If heart/respiratory rate is zero
- `🏥 Go to ER or Call 911 🚑` — Score below 6
- `🩺 Doctor visit is recommended 🩹` — Score 6–9
- `🌿🧘 All clear - Keep it up 🏃🍎` — Score 10

# 8) Example Usage:

project/ $ python project.py
What's the respiratory rate per min? 18
What's the heart rate per min? 75
What's the blood pressure? 118/76
What's the body temperature in F? 98.6
Eupnea
Eucardia
Eutention
Euthermia
🌿🧘 All clear - Keep it up 🏃🍎

#### Acknowledgments:

- Inspired by real-world health triage principles, and CS50’s emphasis on real-world problem-solving using code.
- Designed with care for educational use.
- Thanks to the CS50 staff for providing such an empowering learning experience, and to the broader developer community for best practices and examples.

##### 👨‍💻 Author 💻:

This project was completed by `Ismail Belhachemi`, a CS50 student exploring the intersection of coding and healthcare.
