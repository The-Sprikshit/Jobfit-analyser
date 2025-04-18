# 🧠 Resume Analyzer Using OCR & Python

## 📌 Project Overview

This project is a Resume Analyzer that uses Optical Character Recognition (OCR) with Tesseract and Python to extract and evaluate information from resume images. It automatically checks if a resume meets the requirements for specific job roles such as Software Developer or Data Analyst, based on skills, experience, and education.

---

## 🛠️ Technologies Used

- Python
- Pillow (PIL) – for image handling  
- pytesseract – for OCR (Tesseract engine)
- Regular Expressions (re) – for pattern matching experience

---

## 🎯 Features

- Extracts text from resume images using OCR.
- Analyzes resumes for:
  - ✅ Required skills
  - 🌟 Preferred skills
  - 📊 Years of experience
  - 🎓 Educational qualifications
- Calculates a match score.
- Provides personalized recommendations to improve the resume.
- Displays the expected salary range for the role.

---

## 📂 Supported Roles

- Software Developer  
- Data Analyst  

Each role has predefined requirements for skills, experience, and education.

---

## 💡 How It Works

1. User inputs the path to a resume image and selects a job role.
2. OCR extracts text from the image.
3. The script analyzes the resume content against job-specific requirements.
4. It returns:
   - Skill match
   - Experience match
   - Education relevance
   - Overall fit score
   - Recommendations for improvement

---

## 📷 Sample Input

Enter resume image path: "resume1.png"  
Enter target role: software developer

---

## ✅ Sample Output

Overall Match: 75.0%

Skills Analysis:  
Required Skills Found: python, git  
Preferred Skills Found: docker

Experience: 2 years  
Required: 2 years

Education Fields Found: computer science

Recommendations:  
1. Add these crucial skills: java, javascript, sql  
2. Add education in: software engineering, it

Salary Range: $70,000 - $120,000

---

## 🚀 Future Scope

- Support for PDF resumes.
- GUI interface for ease of use.
- Integration with resume databases.
- Advanced NLP for deeper text understanding.

---

## 📎 How to Run

1. Make sure you have Tesseract-OCR installed:  
   https://github.com/tesseract-ocr/tesseract

2. Install dependencies:
   pip install pytesseract Pillow

3. Run the script:
   python resume_analyzer.py

---

## 👩‍💻 Author

Made with ❤️ by a BCA fresher passionate about automation and self-growth.
