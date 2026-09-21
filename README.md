# 🚀 Flask To-Do App — Automated DevOps CI/CD Pipeline & Cloud Deployment

---

![Flask](https://img.shields.io/badge/Flask-3.10-000000?style=for-the-badge&logo=flask&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitLab CI/CD](https://img.shields.io/badge/GitLab_CI%2FCD-Automated_Pipeline-FC6D26?style=for-the-badge&logo=gitlab&logoColor=white)
![Render](https://img.shields.io/badge/Render-Cloud_Deploy-46E3B7?style=for-the-badge&logo=render&logoColor=white)

An end-to-end **DevOps & Cloud Infrastructure project** demonstrating a full-stack Flask task management application. It features automated schema initialization for PostgreSQL, containerization using Docker, automated unit testing, container image registry management, and continuous deployment to Render.com.

---

## 📌 CI/CD Pipeline Architecture

The automated GitLab CI/CD pipeline (`.gitlab-ci.yml`) is structured into **5 sequential stages**:

1. ⚙️ **Build:** Installs all Python dependencies listed in `requirements.txt`.
2. 🧪 **Test:** Executes automated unit tests (`tests/test_api.py`) via `unittest` to verify API endpoint integrity.
3. 🐳 **Docker Build:** Builds a lightweight production-ready Docker container image using `python:3.10-slim`.
4. 📦 **Release/Push:** Authenticates and pushes the container image to the GitLab Container Registry.
5. 🚀 **Deploy:** Automatically triggers the live web deployment on Render.com.

---

## 🛠️ Project Structure & Key Files

```text
To-Dolist-DevOps/
├── app/
│   ├── templates/      # HTML views (index.html, edit.html)
│   ├── __init__.py      # Flask Application Factory & DB initialization
│   ├── routes.py        # Task management API endpoints & CRUD logic
│   └── db.py            # Low-level PostgreSQL connection & table schema creation
├── tests/
│   └── test_api.py      # Automated unit tests for API endpoints
├── .gitlab-ci.yml       # Complete CI/CD pipeline definitions
├── Dockerfile           # Docker container image build instructions
├── render.yaml          # Render cloud deployment specification
├── requirements.txt     # Python package dependencies
└── run.py               # Main application entry point

```

---

## ⚔️ DevOps Benchmarking: GitLab vs. Azure DevOps

| Feature                    | GitLab DevOps                             | Azure DevOps                                            |
| -------------------------- | ----------------------------------------- | ------------------------------------------------------- |
| **CI/CD Execution**        | ✅ Smooth 5-stage pipeline execution       | ⚠️ Blocked by free-tier parallelism limits              |
| **Container Registry**     | ✅ Built-in Container Registry             | ❌ Requires external/paid setup                          |
| **Agile Task Tracking**    | 🟢 Basic Issues & Kanban boards           | ✅ Advanced sprint & work item tracking via Azure Boards |
| **Deployment Integration** | ✅ Direct seamless integration with Render | ⚠️ Restricted student subscription access               |

---

## 🌐 Live Demo & Links

* 🔗 **Live Web Application:** [to-dolist-ii06.onrender.com](https://www.google.com/url?sa=E&q=https%3A%2F%2Fto-dolist-ii06.onrender.com)
* 🐙 **Source Code Repository:** [GitHub - MalakElyan/To-Dolist-DevOps](https://www.google.com/url?sa=E&q=https%3A%2F%2Fgithub.com%2FMalakElyan%2FTo-Dolist-DevOps)

---

## 📄 Documentation

* **DevOps Architecture & Benchmarking Report:** [Read Report (PDF)](Docs/malakelyan__DevOpsFinalProject.pdf)

---

## 🔗 Connect with Me 
- 🐙 **GitHub:** [@MalakElyan](https://github.com/MalakElyan)
- 💼 **LinkedIn:** [Malak Elyan](https://www.linkedin.com/in/malak-elyan)

---

*Developed by* **Malak Elyan** *as part of the Software Development & DevOps curriculum at UCAS Gaza.*

---

## 🔒 Copyright & Terms of Use
© 2026 **Malak Elyan**. All rights reserved.

---

⭐ If you found this project useful, feel free to star it!

