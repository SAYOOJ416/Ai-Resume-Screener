from django.shortcuts import render, redirect
from .utils import extract_text_from_pdf, extract_skills_spacy, SKILLs_DB, compute_similarity


def home(request):
    # Default: no results shown
    context = {
        "score": None,
        "matched_skills": [],
        "missing_skills": [],
        "error": None
    }

    if request.method == "POST":
        resume_file = request.FILES.get("resume")
        job_desc = request.POST.get("job_description", "")

        if not resume_file or not job_desc.strip():
            context["error"] = "Please upload a resume and provide a job description."
            return render(request, "matcher/home.html", context)

        try:
            # 1️⃣ Extract text
            resume_text = extract_text_from_pdf(resume_file)

            # 2️⃣ Extract skills
            resume_skills = extract_skills_spacy(resume_text)
            job_skills = extract_skills_spacy(job_desc)

            matched_skills = list(resume_skills & job_skills)
            missing_skills = list(job_skills - resume_skills)

            # 3️⃣ Compute similarity
            similarity = compute_similarity(resume_text, job_desc)

            # 4️⃣ Final score
            skill_score = len(matched_skills) / len(job_skills) if job_skills else 0
            combined_score = (similarity + skill_score) / 2
            score = min(100, round(combined_score * 100, 2))

            # 🔁 Store results in session temporarily
            request.session["result"] = {
                "score": score,
                "matched_skills": matched_skills,
                "missing_skills": missing_skills
            }

            # 🔁 Redirect to GET
            return redirect("home")

        except Exception as e:
            context["error"] = f"Error processing PDF: {str(e)}"
            return render(request, "matcher/home.html", context)

    # 🟢 GET request: show result only once
    result = request.session.pop("result", None)

    if result:
        context.update(result)

    return render(request, "matcher/home.html", context)
