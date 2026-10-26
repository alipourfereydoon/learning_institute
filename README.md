<div align="center">

# 🎓 Hooshnoo Learning Institute

### A Modern Learning Management System Built with Django

A responsive, Persian-first educational platform for discovering courses, managing enrollments, and supporting the learning journey of students, instructors, parents, and administrators.

<p>
  <a href="https://github.com/alipourfereydoon/learning_institute">
    <img src="https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github" alt="GitHub repository">
  </a>
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Django-4.2%20to%204.x-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Interface-Responsive-0EA5E9?style=for-the-badge" alt="Responsive interface">
</p>

<p>
  <b>Explore courses · Learn at your own pace · Manage learning in one place</b>
</p>

</div>

---

## 📌 Table of Contents

- [✨ Overview](#-overview)
- [🚀 Features](#-features)
- [🧰 Technology Stack](#-technology-stack)
- [🗂️ Project Structure](#️-project-structure)
- [⚙️ Getting Started](#️-getting-started)
- [🔐 Admin Access and Security](#-admin-access-and-security)
- [🧭 Using the Application](#-using-the-application)
- [🎨 Interface and Customization](#-interface-and-customization)
- [🛠️ Development Notes](#️-development-notes)
- [🧪 Testing](#-testing)
- [🚢 Deployment Checklist](#-deployment-checklist)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [📬 Contact](#-contact)

## ✨ Overview

**Hooshnoo Learning Institute** is a Django-based website and learning management system (LMS) designed to make course discovery and educational administration straightforward. Its visual direction uses a cheerful pastel palette, while its Persian-first interface supports right-to-left (RTL) layouts.

The project brings together a public-facing institute website, a course catalog, account features, and learning-management components in a single Django application. The intended audience includes learners roughly **12–24 years old**, alongside instructors, parents, and administrators.

### 🎯 Project Goals

- Make published courses easy to discover.
- Provide course details and enrollment entry points.
- Support account-based access and role-oriented user experiences.
- Give administrators a central place to manage site settings and educational content.
- Deliver a responsive interface with Persian/RTL support.

## 🚀 Features

### 📚 Course Discovery

- **Dynamic homepage:** displays published course cards.
- **Course catalog:** browse available courses.
- **Live filtering:** filter courses by age, level, category, and search terms.
- **Course details:** view course information and topics before enrolling.
- **Admin-managed content:** courses published through the admin interface can appear on the public homepage.

### 👥 Accounts and Learning Management

- Custom account structure intended for students, instructors, parents, and administrators.
- Registration and login pages.
- User profile and dashboard functionality.
- LMS components for lessons, assignments, quizzes, and assignment submissions.
- Course enrollment workflow.

> The exact permissions and workflow available to each role depend on the implementation in the repository.

### 🎨 User Experience

- Responsive layouts for different screen sizes.
- Persian-first, right-to-left (RTL) interface.
- Bootstrap 5 RTL styling.
- Vazirmatn font support.
- Pastel-inspired visual design and animated decorative particles.
- Floating consultation modal.
- Site-level settings for institute information.

### ⚙️ Site Administration

The Django admin area includes site settings for items such as:

- Institute name and slogan
- Phone number and email address
- Page and site address settings

Administrators can also manage relevant content through the available Django admin models.

## 🧰 Technology Stack

| Technology | Purpose |
| --- | --- |
| [Python](https://www.python.org/) | Application programming language |
| [Django](https://www.djangoproject.com/) | Web framework, routing, models, and administration |
| [Pillow](https://python-pillow.org/) | Image processing support |
| [Bootstrap 5 RTL](https://getbootstrap.com/) | Responsive, right-to-left interface styling |
| HTML, CSS, JavaScript | Templates, styling, and client-side interactions |
| SQLite | Default local development database |

### Requirements

- Python **3.10 or newer**
- `pip`
- Git (recommended)
- A modern web browser

The dependencies declared by this repository are:

```text
Django >= 4.2, < 5.0
Pillow >= 10.0
```

## 🗂️ Project Structure

```text
learning_institute/
├── accounts/          # Custom user accounts and profile-related features
├── core/              # Homepage, about, contact, FAQ, and site settings
├── courses/           # Course categories, courses, and enrollment
├── hooshnoo_core/     # Main Django settings and URL configuration
├── lms/               # Lessons, assignments, quizzes, and submissions
├── static/            # CSS, JavaScript, and static assets
├── templates/         # Django HTML templates
├── db.sqlite3         # SQLite database included in the repository
├── manage.py          # Django management utility
├── requirements.txt   # Python dependencies
└── README.md
```

*This tree highlights the main directories and files; individual modules may contain additional files.*

## ⚙️ Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/alipourfereydoon/learning_institute.git
cd learning_institute
```

### 2. Create and Activate a Virtual Environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure the Database

The repository includes an SQLite database file with sample data. If you want to initialize or update the database using Django migrations, run:

```bash
python manage.py migrate
```

If you prefer a clean local database, back up any data you need and follow your usual Django SQLite reset workflow before migrating. Do not delete a database that contains data you want to keep.

### 5. (Optional) Load Sample Data

The repository documents a `seed_data` management command for creating sample courses and an administrator account:

```bash
python manage.py seed_data
```

If Django reports that the command is unavailable, check the installed app's management commands and the current repository version.

### 6. Create an Administrator Account

To create your own administrator account, run:

```bash
python manage.py createsuperuser
```

Follow the prompts to enter a username, email address, and password.

### 7. Start the Development Server

```bash
python manage.py runserver
```

Open the following addresses in your browser:

| Area | URL |
| --- | --- |
| Public website | http://127.0.0.1:8000/ |
| Django admin | http://127.0.0.1:8000/admin/ |

To stop the server, press `Ctrl+C` in the terminal.

## 🔐 Admin Access and Security

The repository's existing documentation mentions a sample administrator account:

- **Username:** `admin`
- **Password:** `admin1234`

Treat these credentials as **development-only**. They may not work if the database or sample data has changed. Do not deploy a site with a known or default password.

Before exposing the application to the internet:

- Create a new administrator account or change all sample credentials.
- Set a strong, unique `SECRET_KEY` using environment variables.
- Set `DEBUG = False`.
- Configure `ALLOWED_HOSTS` for your deployment domain.
- Use HTTPS and secure cookie settings.
- Keep database files, secrets, and user uploads out of public source control where appropriate.
- Review access permissions, authentication, and upload handling.
- Back up production data and use a production-appropriate database configuration.

## 🧭 Using the Application

### For Visitors and Learners

1. Open the homepage to explore published courses.
2. Browse the course catalog.
3. Use the available filters to narrow results by age, level, category, or search query.
4. Open a course details page to review its information and topics.
5. Register or sign in to access account-related features and follow the available enrollment flow.

### For Administrators

1. Open `/admin/` and sign in with an administrator account.
2. Manage course-related content using the available admin models.
3. Publish courses intended to appear on the public homepage.
4. Update institute information through the site settings section.
5. Review user and learning-related records according to the permissions configured by the project.

## 🎨 Interface and Customization

The project is designed around a friendly educational identity, with a pastel color palette and Persian RTL presentation.

Common customization areas include:

- **Templates:** `templates/`
- **Stylesheets and JavaScript:** `static/`
- **Site configuration and routing:** `hooshnoo_core/`
- **Homepage, contact, and site settings:** `core/`
- **Course catalog and enrollment:** `courses/`
- **Accounts and profiles:** `accounts/`
- **Lessons and assessments:** `lms/`

The admin interface can be used to adjust supported institute settings without editing templates directly.

## 🛠️ Development Notes

### Useful Django Commands

```bash
# Apply database migrations
python manage.py migrate

# Create a new migration after model changes
python manage.py makemigrations

# Create an administrator account
python manage.py createsuperuser

# Run the local development server
python manage.py runserver

# Run the project's automated tests
python manage.py test

# Check the project for common configuration issues
python manage.py check
```

### Static Files

During local development, Django can serve static files according to the project's configuration. For production, configure `STATIC_ROOT`, run `collectstatic`, and serve static assets using an appropriate web server or storage service.

```bash
python manage.py collectstatic
```

Run this command after configuring the project's static-file settings for your target environment.

## 🧪 Testing

Run Django's test suite with:

```bash
python manage.py test
```

For a more reliable release, also verify the following manually:

- [ ] Homepage and published course cards load correctly.
- [ ] Course search and filters behave as expected.
- [ ] Course details and enrollment flows work.
- [ ] Registration, login, logout, and profile pages behave correctly.
- [ ] Lesson, assignment, quiz, and submission workflows work where implemented.
- [ ] Admin users can update supported site settings.
- [ ] RTL layouts remain usable on desktop and mobile.
- [ ] Forms show appropriate validation and error messages.

## 🚢 Deployment Checklist

Before deploying to a production environment:

- [ ] Use a supported Python and dependency configuration.
- [ ] Set `DEBUG = False`.
- [ ] Load secrets from environment variables or a secret manager.
- [ ] Configure `ALLOWED_HOSTS` and, where applicable, `CSRF_TRUSTED_ORIGINS`.
- [ ] Configure HTTPS and secure session/CSRF cookies.
- [ ] Configure static and media file storage.
- [ ] Back up and protect the database.
- [ ] Replace all sample credentials.
- [ ] Run migrations as part of the release process.
- [ ] Run `python manage.py check --deploy` and address relevant warnings.
- [ ] Confirm logging, backups, and recovery procedures.

**Important:** `python manage.py runserver` is intended for development, not production hosting. Follow the official [Django deployment checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/) before going live.

## 🤝 Contributing

Contributions, bug reports, and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature
   ```

3. Make focused changes and add or update tests where appropriate.
4. Run the test suite and project checks.
5. Commit your changes:

   ```bash
   git commit -m "Add: describe your change"
   ```

6. Push your branch and open a Pull Request with a clear description of the changes.

For larger changes, consider opening an issue first to discuss the proposed approach.

## 📄 License

No license information was identified in the repository's current README. Unless a license file or explicit license is added by the owner, reuse and redistribution permissions should not be assumed.

If you maintain this project, consider adding a `LICENSE` file with the terms you intend to apply.

## 📬 Contact

For questions, suggestions, or project-related discussions, please use the repository's GitHub page:

**Repository:** https://github.com/alipourfereydoon/learning_institute

---

<div align="center">

**Built to make learning more accessible, organized, and engaging.** 🎓

<sub>If you find this project useful, consider giving the repository a ⭐ on GitHub.</sub>

</div>
