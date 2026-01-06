# Ai-Resume-Screener

AI Resume Screener is a **Django-based web application** that evaluates resumes against job descriptions using **Natural Language Processing (NLP)**. The app calculates a **match percentage**, identifies **matched skills**, and highlights **missing skills**, helping users quickly assess resume-job fit.

---

## 🚀 Features

- **Resume vs Job Description Matching** – Upload a resume and provide a job description; the app calculates a match score.
- **Skill Analysis** – Shows which key skills are present in the resume and which are missing.
- **Semantic Similarity** – Uses **TF-IDF and spaCy NLP** for intelligent text comparison.
- **Interactive UI** – Clean, responsive interface built with **Tailwind CSS**, including animated progress bar for match percentage.
- **Error Handling** – Handles invalid inputs or unsupported PDFs gracefully.

---

## 🛠 Technologies Used

- **Backend:** Django, Python  
- **NLP & Text Processing:** spaCy, TF-IDF, cosine similarity  
- **Frontend:** Tailwind CSS  
- **PDF Handling:** PyPDF2

---

## 📂 Project Structure

Resume_Screener/
│
├── matcher/ # Django app
├── resume_screener/ # Django project folder
├── utils/ # Skills extractor, similarity, parser
├── manage.py
├── requirements.txt # Python dependencies
├── README.md
└── .gitignore


---

## ⚡ Screenshots

**Landing Page / Upload**
![Landing Page](Screenshots/Landing.png)

**Resume Upload / Analyze**
![Analyze Page](Screenshots/Analyze.png)

**Result Page / Skill Match**
![Result Page](Screenshots/Result.png)

---

## 💻 Setup Instructions

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/ai-resume-screener.git

2. Navigate into the project folder:

cd ai-resume-screener


3. Create and activate a virtual environment (Python 3.11 recommended):

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux


4 .Install dependencies:

pip install -r requirements.txt


5. Run the Django server:

python manage.py runserver


6. Open in browser:
http://127.0.0.1:8000

--- 

## 📝 How to Use

1. Upload a **resume (PDF)**  
2. Paste a **job description** in the text box  
3. Click **Analyze**  
4. View:
   - **Match Percentage**
   - **Matched Skills**
   - **Missing Skills**

---

## 📌 License

This project is **open source** and available under the MIT License.  

---

## 🎯 Next Steps / Improvements

- Add support for **multiple resume formats** (DOCX, TXT)  
- Include **weightage for different skills** in scoring  
- Improve semantic similarity using **transformer-based embeddings (BERT)**  
- Deploy on cloud with **Nginx / Docker** for production  

---



