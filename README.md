---

### 📄 `README.md`

```markdown
# 🧮 Age Calculator – Manual Date Logic in Python

This is a beginner-friendly Python project that calculates a person's age in **years**, **months**, and **exact number of days**, based on their full date of birth. Unlike typical implementations, this project **manually computes** leap years, days in each month, and date differences **without using `datetime`** — making it ideal for learning date logic and condition handling in Python.

---

## 🚀 Live Features

- 📅 Input full birth date (year, month, day)
- 🧠 Calculates:
  - ✅ Exact years (with birthday check)
  - ✅ Approximate months lived
  - ✅ **Exact** number of days lived
- 🗓️ Manual leap year and month length handling
- 🧩 No use of `datetime` module – built entirely using `time` and `calendar`

---

## 🛠 Tech Stack

| Language | Modules Used        |
|----------|---------------------|
| Python   | `time`, `calendar`  |

---

## 📷 Demo

```

\==== Age Calculator ====
Enter your name: Pavan
Enter your birth year (e.g., 2001): 2001
Enter your birth month (1-12): 7
Enter your birth day (1-31): 4

\==== Result ====
Pavan's age is:
➡️ 24 years
➡️ 288 months (approximate)
➡️ 8766 days (exact)

````

---

## 🧠 How it Works

1. Takes input for **birth year, month, and day**
2. Gets the **current date** using the `time` module
3. Calculates:
   - ✅ Years lived (checks if birthday has occurred this year)
   - ✅ Months (counts full months completed)
   - ✅ Days (manually adds days from each year and month using `calendar.isleap()`)
4. Outputs results in a clean and readable format

---

## 💻 How to Run Locally

1. Clone the repository or copy the code into a `.py` file:

```bash
git clone https://github.com/yourusername/age-calculator-python.git
cd age-calculator-python
python age_calculator.py
````

2. Or run it using any Python IDE (e.g., VSCode, PyCharm)

---

## 📚 Concepts Covered

* Leap year calculation (`calendar.isleap`)
* Days per month logic
* Time-based calculations using `time.localtime()`
* Basic conditionals, loops, and input/output handling

---

## 📁 Project Structure

```
📁 age-calculator-python
├── age_calculator.py   # Main source code
└── README.md           # Project description
```
