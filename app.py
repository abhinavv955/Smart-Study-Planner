from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------- TEMP STORAGE ----------------
study_logs = []
planned_study = []
exam_results = []

# ---------------- SUBJECT-WISE MCQs ----------------
weekly_questions = {
    "OS": [
        {
            "question": "Which scheduling algorithm gives minimum average waiting time?",
            "options": ["FCFS", "SJF", "Round Robin", "Priority"],
            "answer": "SJF"
        },
        {
            "question": "What is a process?",
            "options": [
                "Program in execution",
                "Program stored in memory",
                "Thread",
                "CPU register"
            ],
            "answer": "Program in execution"
        },
        {
            "question": "Which OS component manages hardware resources?",
            "options": ["Kernel", "Shell", "File System", "User Interface"],
            "answer": "Kernel"
        }
    ],

    "AOA": [
        {
            "question": "Which algorithm follows divide and conquer technique?",
            "options": ["Merge Sort", "Bubble Sort", "Selection Sort", "Insertion Sort"],
            "answer": "Merge Sort"
        },
        {
            "question": "What is the time complexity of Binary Search?",
            "options": ["O(n)", "O(log n)", "O(n log n)", "O(1)"],
            "answer": "O(log n)"
        },
        {
            "question": "Worst case time complexity of Quick Sort is?",
            "options": ["O(n log n)", "O(n)", "O(n²)", "O(log n)"],
            "answer": "O(n²)"
        }
    ],

    "Maths": [
        {
            "question": "Derivative of x² is?",
            "options": ["2x", "x", "x²", "1"],
            "answer": "2x"
        },
        {
            "question": "Value of sin(90°) is?",
            "options": ["0", "1", "-1", "∞"],
            "answer": "1"
        },
        {
            "question": "Integral of 1 dx is?",
            "options": ["x + C", "1", "0", "C"],
            "answer": "x + C"
        }
    ]
}

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('home.html')

# ---------------- STUDY PLANNER ----------------
@app.route('/planner', methods=['GET', 'POST'])
def planner():
    timetable = {}

    if request.method == 'POST':
        subject = request.form.get('subject')
        difficulty = request.form.get('difficulty')
        exam_date = request.form.get('exam_date')
        hours = int(request.form.get('hours'))

        if difficulty == "High":
            recommended = hours + 2
        elif difficulty == "Medium":
            recommended = hours
        else:
            recommended = max(hours - 1, 1)

        timetable = {
            "subject": subject,
            "difficulty": difficulty,
            "exam_date": exam_date,
            "hours": hours,
            "recommended": recommended
        }

       
        plan = {
            "subject": subject,
            "hours": hours
        }

        planned_study.append(plan)

    return render_template('planner.html', timetable=timetable)

# ---------------- STUDY LOG ----------------
@app.route('/study-log', methods=['GET', 'POST'])
def study_log():
    message = None

    if request.method == 'POST':
        log = {
            "date": request.form.get('date'),
            "subject": request.form.get('subject'),
            "hours": int(request.form.get('hours')),
            "status": request.form.get('status')
        }

        study_logs.append(log)
        message = "Study record saved successfully!"

    return render_template('study_log.html', message=message, logs=study_logs)


# ---------------- WEEKLY TEST ----------------
@app.route('/weekly-test', methods=['GET', 'POST'])
def weekly_test():

    selected_subject = request.form.get('subject')
    questions = []
    score = None
    total = 0

    if selected_subject in weekly_questions:
        questions = weekly_questions[selected_subject]
        total = len(questions)

    if request.method == 'POST' and 'q0' in request.form:

        score = 0
        for i, q in enumerate(questions):
            if request.form.get(f"q{i}") == q["answer"]:
                score += 1

        result = {
            "subject": selected_subject,
            "score": score,
            "total": total,
            "status": "Pass" if score >= total * 0.6 else "Fail"
        }

        exam_results.append(result)

    return render_template(
        'weekly_test.html',
        subjects=weekly_questions.keys(),
        selected_subject=selected_subject,
        questions=questions,
        score=score,
        total=total
    )


# ---------------- SUMMARY ----------------
@app.route('/summary')
def summary():

    total_hours = 0
    subject_hours = {}
    completed = 0
    not_completed = 0

    for log in study_logs:
        hours = log['hours']
        total_hours += hours

        subject = log['subject']
        subject_hours[subject] = subject_hours.get(subject, 0) + hours

        if log['status'] == "Completed":
            completed += 1
        else:
            not_completed += 1

    most_studied = max(subject_hours, key=subject_hours.get) if subject_hours else None
    least_studied = min(subject_hours, key=subject_hours.get) if subject_hours else None

    # Planned hours
    planned_hours = {}
    for p in planned_study:
        subject = p['subject']
        planned_hours[subject] = planned_hours.get(subject, 0) + p['hours']

    # Progress bars
    progress_data = {}
    if subject_hours:
        max_hours = max(subject_hours.values())
        for subject, hrs in subject_hours.items():
            percent = int((hrs / max_hours) * 100)
            progress_data[subject] = percent

    # Exam analytics
    total_exams = len(exam_results)
    last_score = exam_results[-1] if exam_results else None

    avg_score = None
    pass_count = 0
    fail_count = 0

    if exam_results:
        avg_score = sum(r['score'] for r in exam_results) / total_exams

        for r in exam_results:
            if r['status'] == "Pass":
                pass_count += 1
            else:
                fail_count += 1

    return render_template(
        'summary.html',
        total_hours=total_hours,
        subject_hours=subject_hours,
        planned_hours=planned_hours,
        progress_data=progress_data,
        completed=completed,
        not_completed=not_completed,
        most_studied=most_studied,
        least_studied=least_studied,
        total_exams=total_exams,
        last_score=last_score,
        avg_score=avg_score,
        pass_count=pass_count,
        fail_count=fail_count
    )


# ---------------- RUN SERVER ----------------
if __name__ == '__main__':
    app.run(debug=True)