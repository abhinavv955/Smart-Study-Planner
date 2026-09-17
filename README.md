# Smart-Study-Planner
A Simple Web-Based Study Planner and Task Scheduling System for Students

# 📚 StudyFlow – Smart Study Planner and Task Scheduler

> **Plan • Track • Test • Analyze • Succeed**

StudyFlow is a web-based academic productivity platform designed to help students organize their study schedules, track their learning activities, evaluate their subject knowledge, and analyze their academic progress in one place.

The project combines study planning, task scheduling, study logging, weekly assessments, and performance analytics into a single user-friendly platform.

---

## 👥 Team Members

This Capstone Project was developed by:

- **Abinav V.P**
- **Bhupesh**
- **Pranay**

---

## 🎯 Problem Statement

Students often struggle to effectively manage multiple subjects, study hours, assignments, and examination preparation.

Traditional methods such as handwritten timetables and basic task lists do not provide sufficient tracking or performance analysis. Students may plan their studies but have difficulty determining whether they are actually following the plan.

StudyFlow addresses this problem by providing a centralized platform where students can:

- Create study plans
- Schedule academic tasks
- Record actual study time
- Compare planned and studied hours
- Take subject-wise tests
- Analyze their academic progress

---

## 💡 Proposed Solution

StudyFlow provides an integrated academic planning system that connects **planning, tracking, testing, and analysis**.

A student can create a study plan by entering the subject, available study hours, difficulty level, and examination date.

The system stores the planned study information and allows the student to later record the actual time spent studying.

The Summary section then compares the planned study time with the actual study time and presents useful performance information.

Students can also take subject-wise weekly tests to evaluate their understanding and view their examination performance through the summary dashboard.

---

# 🚀 Features

## 📅 Smart Study Planner

Create structured study plans by providing:

- Subject
- Available study hours
- Difficulty level
- Examination date

The system calculates and stores the planned study hours for each subject.

---

## 📝 Study Log

Record daily learning activities including:

- Date
- Subject
- Hours studied
- Completion status

This allows students to maintain a record of their actual study activities.

---

## 📊 Planned vs Studied Analysis

StudyFlow compares the amount of time planned for a subject with the amount of time actually studied.

The system can identify whether a student is:

- **On Track**
- **Behind Schedule**

This provides a simple way to understand study consistency.

---

## 📈 Subject Progress

The Summary page provides subject-wise progress indicators based on recorded study activity.

Students can quickly identify which subjects have received more or less study time.

---

## 🧠 Weekly Tests

Students can take subject-wise MCQ tests.

Currently supported subjects include:

- Operating Systems (OS)
- Analysis of Algorithms (AOA)
- Mathematics

After completing a test, the system calculates:

- Score
- Total questions
- Pass/Fail result

---

## 📋 Exam Performance Summary

The system maintains examination results and provides:

- Total exams attempted
- Latest exam score
- Latest exam result
- Average score
- Pass count
- Fail count

---

## 🎨 Modern User Interface

StudyFlow includes a modern responsive interface featuring:

- Gradient backgrounds
- Glassmorphism cards
- Animated buttons
- Responsive navigation
- Progress bars
- Hover effects
- Scroll animations
- Mobile-friendly layout

---

# 🛠️ Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

# 🏗️ Project Structure

```text
StudyFlow/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   ├── home.html
│   ├── planner.html
│   ├── study_log.html
│   ├── summary.html
│   ├── weekly_test.html
│   └── schedule.html
│
└── static/
    └── style.css
