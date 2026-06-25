# Name: Abdul haadi    Roll No: 90      CYS(S)-2026-90
import time

#Crenditails
ADMIN_USER  = "ecat_admin"
ADMIN_PASS  = "ecat@2024"
STUDENT_USER = "student"
STUDENT_PASS = "student123"

CORRECT_MARKS  =  4
WRONG_MARKS    = -1
SKIP_MARKS     =  0
MIN_QUESTIONS  = 10

all_results = []   # list of dicts — one per student attempt

questions = [
    {
        "id": 1,
        "subject": "Math",
        "question": "5 * 2 + 3 = ?",
        "choices": ["A. 16", "B. 11", "C. 13", "D. 5"],
        "answer": "C"
    },
    {
        "id": 2,
        "subject": "Physics",
        "question": "How many laws of motion did Newton give?",
        "choices": ["A. 3", "B. 2", "C. 5", "D. 1"],
        "answer": "A"
    },
    {
        "id": 3,
        "subject": "English",
        "question": "Antonym of 'smooth' is?",
        "choices": ["A. Clear", "B. Rough", "C. Clean", "D. Ice"],
        "answer": "B"
    },
    {
        "id": 4,
        "subject": "Physics",
        "question": "Which one is a base quantity?",
        "choices": ["A. Force", "B. Length", "C. Power", "D. Gravitational Force"],
        "answer": "B"
    },
    {
        "id": 5,
        "subject": "Math",
        "question": "100 / 2 - 30 = ?",
        "choices": ["A. 10", "B. 15", "C. 20", "D. 25"],
        "answer": "C"
    },
    {
        "id": 6,
        "subject": "Computer",
        "question": "Which one is NOT an input device?",
        "choices": ["A. Mouse", "B. Keyboard", "C. LED", "D. Microphone"],
        "answer": "C"
    },
    {
        "id": 7,
        "subject": "English",
        "question": "Plural of 'Child' is?",
        "choices": ["A. Children", "B. Childs", "C. Child", "D. Childer"],
        "answer": "A"
    },
    {
        "id": 8,
        "subject": "Chemistry",
        "question": "Chemical formula of Nitrogen gas is?",
        "choices": ["A. N2", "B. O2", "C. Og", "D. X"],
        "answer": "A"
    },
    {
        "id": 9,
        "subject": "Math",
        "question": "18 - 5 = ?",
        "choices": ["A. 13", "B. 12", "C. 14", "D. 7"],
        "answer": "A"
    },
    {
        "id": 10,
        "subject": "Physics",
        "question": "SI unit of acceleration is?",
        "choices": ["A. ms⁻¹", "B. N", "C. ms⁻²", "D. V"],
        "answer": "C"
    },
]

# Grade Calculator
def grade(percent):
    if percent >= 80:
        return "EXCELLENT"
    elif percent >= 65:
        return "GOOD"
    elif percent >= 50:
        return "AVERAGE"
    else:
        return "BELOW AVERAGE"

#  STUDENT PORTAL
def show_rules():
    print("               EXAM RULES")
    print(f"  Correct Answer  : +{CORRECT_MARKS} marks")
    print(f"  Wrong Answer    : {WRONG_MARKS} mark")
    print(f"  Skipped Question:  {SKIP_MARKS} marks")
    print()
    print("  - Enter A / B / C / D to answer a question.")
    print("  - Enter S to skip a question (can revisit later).")
    print("  - Enter SUBMIT at any time to end the exam early.")
    print("  - Exam auto-submits when all questions are done.")

def exam():
    name = input("Enter Your Full Name : ").strip()
    roll = input("Enter Your Roll No   : ").strip()

    answers = {}
    exam_start = time.strftime("%d-%b-%Y  %I:%M %p")

    print("\nExam started! Good luck.\n")
    time.sleep(1)

    for i in range(len(questions)):
        print(f"  Question {i + 1} of {len(questions)}  |  Subject: {questions[i]['subject']}")
        print(f"  {questions[i]['question']}\n")
        for c in questions[i]["choices"]:
            print(f"    {c}")
        print()

        while True:
            ans = input("  Your Answer (A/B/C/D | S=Skip | SUBMIT=End): ").strip().upper()
            if ans in ("A", "B", "C", "D", "S", "SUBMIT"):
                break
            print("  Invalid input. Please enter A, B, C, D, S, or SUBMIT.")

        if ans == "SUBMIT":
            print("\n  Exam submitted early.")
            break

        answers[i] = ans

    correct  = 0
    wrong    = 0
    skipped  = 0

    for i in range(len(questions)):
        given = answers.get(i, "S")
        if given == "S":
            skipped += 1
        elif given == questions[i]["answer"]:
            correct += 1
        else:
            wrong += 1

    score   = (correct * CORRECT_MARKS) + (wrong * WRONG_MARKS)
    total   = len(questions) * CORRECT_MARKS
    percent = (score / total) * 100

    result = {
        "Name"       : name,
        "Roll No"    : roll,
        "Score"      : score,
        "Total"      : total,
        "Correct"    : correct,
        "Wrong"      : wrong,
        "Skipped"    : skipped,
        "Percentage" : round(percent, 2),
        "Grade"      : grade(percent),
        "Date/Time"  : exam_start,
        "Answers"    : answers     # per-question breakdown stored here
    }

    all_results.append(result)

# Print Result
    print("                  YOUR RESULT")
    print(f"  Name        : {name}")
    print(f"  Roll No     : {roll}")
    print(f"  Score       : {score} / {total}")
    print(f"  Correct     : {correct}   Wrong: {wrong}   Skipped: {skipped}")
    print(f"  Percentage  : {round(percent, 2)}%")
    print(f"  Grade       : {grade(percent)}")
    print(f"  Date / Time : {exam_start}")

# Per-Question Answer Review
    print("\n  ANSWER REVIEW")
    print(f"  {'Q#':<4} {'Subject':<12} {'Your Ans':<10} {'Correct':<10} {'Result'}")
    for i in range(len(questions)):
        given   = answers.get(i, "S")
        correct_ans = questions[i]["answer"]
        if given == "S":
            outcome = "SKIPPED"
        elif given == correct_ans:
            outcome = "CORRECT ✓"
        else:
            outcome = "WRONG   ✗"
        print(f"  {i+1:<4} {questions[i]['subject']:<12} {given:<10} {correct_ans:<10} {outcome}")

def student_login():
    attempts = 3
    while attempts > 0:
        print("\n      Student Login    ")
        user     = input("  Username : ").strip()
        password = input("  Password : ").strip()

        if user == STUDENT_USER and password == STUDENT_PASS:
            print("  Login Successful!\n")
            time.sleep(0.5)

            while True:
                print("  STUDENT MENU")
                print("  1. Start Exam")
                print("  2. View Exam Rules")
                print("  3. Logout")
                choice = input("\n  Enter Choice: ").strip()

                if choice == "1":
                    exam()
                elif choice == "2":
                    show_rules()
                elif choice == "3":
                    print("  Logged out.\n")
                    return
                else:
                    print("  Invalid choice.")
            return

        attempts -= 1
        print(f"  Wrong credentials! Attempts left: {attempts}")

    print("  Account LOCKED after 3 failed attempts.\n")


#  ADMIN PORTAL
def view_all_questions():
    print("  ALL QUESTIONS IN QUESTION BANK")
    if not questions:
        print("  No questions found.")
        return
    for i, q in enumerate(questions):
        print(f"\n  [{i + 1}] Subject: {q['subject']}")
        print(f"      Q: {q['question']}")
        for c in q["choices"]:
            print(f"         {c}")
        print(f"      Correct Answer: {q['answer']}")

def add_question():
    print("  ADD NEW QUESTION")
    subject  = input("  Subject          : ").strip()
    question = input("  Question Text    : ").strip()
    print("  Enter 4 choices (include the letter, e.g.  A. Rome)")
    ch_a = input("  Choice A         : ").strip()
    ch_b = input("  Choice B         : ").strip()
    ch_c = input("  Choice C         : ").strip()
    ch_d = input("  Choice D         : ").strip()

    while True:
        answer = input("  Correct Answer (A/B/C/D): ").strip().upper()
        if answer in ("A", "B", "C", "D"):
            break
        print("  Please enter A, B, C, or D only.")

    new_id = questions[-1]["id"] + 1 if questions else 1
    new_q  = {
        "id"      : new_id,
        "subject" : subject,
        "question": question,
        "choices" : [ch_a, ch_b, ch_c, ch_d],
        "answer"  : answer
    }
    questions.append(new_q)
    print(f"\n  Question added successfully! (Total: {len(questions)})")

def delete_question():
    print("  DELETE A QUESTION")
    if not questions:
        print("  No questions to delete.")
        return

    view_all_questions()
    try:
        num = int(input("  Enter question number to delete (0 to cancel): ").strip())
        if num == 0:
            return
        if 1 <= num <= len(questions):
            removed = questions.pop(num - 1)
            print(f"  Deleted: \"{removed['question']}\"")
        else:
            print("  Invalid number.")
    except ValueError:
        print("  Please enter a valid number.")

def question_bank_stats():
    print("  QUESTION BANK STATISTICS")
    print(f"  Total Questions : {len(questions)}")
    subject_count = {}
    for q in questions:
        subj = q["subject"]
        subject_count[subj] = subject_count.get(subj, 0) + 1
    print("\n  Breakdown by Subject:")
    for subj, count in subject_count.items():
        print(f"    {subj:<15} : {count} question(s)")

def view_all_results():
    print("  ALL STUDENT RESULTS")
    if not all_results:
        print("  No results recorded yet.")
        return
    print(f"  {'#':<4} {'Name':<18} {'Roll':<8} {'Score':<8} {'%':<8} {'Grade':<14} {'Date/Time'}")
    for i, r in enumerate(all_results):
        print(f"  {i+1:<4} {r['Name']:<18} {r['Roll No']:<8} {r['Score']:<8} {str(r['Percentage'])+'%':<8} {r['Grade']:<14} {r['Date/Time']}")


def view_detailed_result():
    print("  VIEW DETAILED RESULT (PER STUDENT)")
    if not all_results:
        print("  No results recorded yet.")
        return

    view_all_results()
    try:
        num = int(input("  Enter student number to view detail (0 to cancel): ").strip())
        if num == 0:
            return
        if 1 <= num <= len(all_results):
            r = all_results[num - 1]
            print(f"  Name        : {r['Name']}")
            print(f"  Roll No     : {r['Roll No']}")
            print(f"  Score       : {r['Score']} / {r['Total']}")
            print(f"  Correct     : {r['Correct']}   Wrong: {r['Wrong']}   Skipped: {r['Skipped']}")
            print(f"  Percentage  : {r['Percentage']}%")
            print(f"  Grade       : {r['Grade']}")
            print(f"  Date / Time : {r['Date/Time']}")
            print("  Per-Question Breakdown:")
            print(f"  {'Q#':<4} {'Subject':<12} {'Question':<35} {'Given':<8} {'Correct':<8} {'Result'}")
            answers = r.get("Answers", {})
            for i in range(len(questions)):
                given       = answers.get(i, "S")
                correct_ans = questions[i]["answer"]
                if given == "S":
                    outcome = "SKIPPED"
                elif given == correct_ans:
                    outcome = "CORRECT"
                else:
                    outcome = "WRONG"
                q_text = questions[i]["question"][:33] + ".." if len(questions[i]["question"]) > 33 else questions[i]["question"]
                print(f"  {i+1:<4} {questions[i]['subject']:<12} {q_text:<35} {given:<8} {correct_ans:<8} {outcome}")
        else:
            print("  Invalid number.")
    except ValueError:
        print("  Please enter a valid number.")


def class_result_stats():
    print("  CLASS RESULT STATISTICS")
    if not all_results:
        print("  No results recorded yet.")
        return

    scores      = [r["Score"] for r in all_results]
    percentages = [r["Percentage"] for r in all_results]
    total_marks = all_results[0]["Total"]

    highest = max(scores)
    lowest  = min(scores)
    average = sum(scores) / len(scores)

    pass_count = sum(1 for p in percentages if p >= 50)
    fail_count = len(all_results) - pass_count

    grade_dist = {"EXCELLENT": 0, "GOOD": 0, "AVERAGE": 0, "BELOW AVERAGE": 0}
    for r in all_results:
        grade_dist[r["Grade"]] += 1

    print(f"  Total Students  : {len(all_results)}")
    print(f"  Highest Score   : {highest} / {total_marks}")
    print(f"  Lowest Score    : {lowest} / {total_marks}")
    print(f"  Average Score   : {round(average, 2)} / {total_marks}")
    print(f"  Passed (>=50%)  : {pass_count}")
    print(f"  Failed  (<50%)  : {fail_count}")
    print("\n  Grade Distribution:")
    for g, cnt in grade_dist.items():
        print(f"    {g:<15} : {cnt} student(s)")


def admin_menu():
    while True:
        print("  ADMIN MENU")
        print("  1. View All Questions")
        print("  2. Add New Question")
        print("  3. Delete a Question")
        print("  4. Question Bank Statistics")
        print("  5. View All Student Results")
        print("  6. View Detailed Result (Per Student)")
        print("  7. Class Result Statistics")
        print("  8. Logout")

        choice = input("  Enter Choice: ").strip()

        if choice == "1":
            view_all_questions()
        elif choice == "2":
            add_question()
        elif choice == "3":
            delete_question()
        elif choice == "4":
            question_bank_stats()
        elif choice == "5":
            view_all_results()
        elif choice == "6":
            view_detailed_result()
        elif choice == "7":
            class_result_stats()
        elif choice == "8":
            print("  Admin logged out.\n")
            break
        else:
            print("  Invalid choice. Please enter 1–8.")


def admin_login():
    attempts = 3
    while attempts > 0:
        print("\n  --- Admin Login ---")
        user     = input("  Admin Username : ").strip()
        password = input("  Admin Password : ").strip()

        if user == ADMIN_USER and password == ADMIN_PASS:
            print("  Admin Login Successful!\n")
            time.sleep(0.5)
            admin_menu()
            return

        attempts -= 1
        print(f"  Wrong credentials! Attempts left: {attempts}")

    print("  Admin account LOCKED after 3 failed attempts.\n")

#  MAIN MENU
def main():
    while True:
        print("         ECAT EXAM SYSTEM — DUAL PORTAL")
        print("  1. Student Portal")
        print("  2. Admin Portal")
        print("  3. Exam Rules")
        print("  4. Exit")

        choice = input("  Enter Your Choice: ").strip()

        if choice == "1":
            student_login()
        elif choice == "2":
            admin_login()
        elif choice == "3":
            show_rules()
        elif choice == "4":
            print("\n  Thank you for using ECAT Exam System. Goodbye!\n")
            break
        else:
            print("  Invalid choice. Please enter 1–4.")


main()