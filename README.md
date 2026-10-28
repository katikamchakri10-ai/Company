# Django Multi-Page Website

A multi-page website built with **Python and Django**, using Django templates, static assets, and a database to manage website content. The project includes Home, About, Services, Portfolio, Pricing, Blog, Contact, Team, and Testimonials pages, along with separate men's, women's, and electronics URL sections.

## 🚀 Features

- **Multi-page website:** Separate pages for different sections of the website.
- **Dynamic content:** Website information is loaded from Django database models.
- **Contact form:** Accepts user messages and stores valid submissions in the database.
- **Django Admin:** Manage website content and review contact form submissions.
- **Static and media files:** Supports CSS, JavaScript, images, and uploaded media.
- **Reusable templates:** Uses Django's template system to organize website pages.

## 🛠️ Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite
- Django Templates

## 📂 Project Structure

```text
amazon/
├── amazon/
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── index/
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── mens/
├── womens/
├── electronics/
├── templates/
├── static/
├── media/
├── manage.py
└── README.md
```

*Note: The exact files and folders may vary depending on your current project version.*

## 📄 Website Pages

| Page | URL |
|---|---|
| Home | `/` |
| About | `/about/` |
| Services | `/services/` |
| Portfolio | `/portfolio/` |
| Pricing | `/pricing/` |
| Blog | `/blog/` |
| Contact | `/contact/` |
| Service Details | `/servicedetails/` |
| Team | `/team/` |
| Testimonials | `/testimonials/` |
| Django Admin | `/admin/` |

The project also contains URL sections for men's products, women's products, and electronics.

## 🗄️ Database Models

The `index` application contains models for managing website content:

- **about1** — Stores home-page title, description, and image.
- **ourteam** — Stores team member information and images.
- **client** — Stores client-related information and images.
- **article** — Stores blog/article content.
- **price** — Stores pricing-page information.
- **contactforms** — Stores contact form submissions, including name, email, subject, message, and submission timestamp.

## 📩 Contact Form Workflow

1. A visitor opens the Contact page.
2. The visitor submits their name, email, subject, and message.
3. Django processes the form using a POST request and CSRF protection.
4. Valid submissions are saved to the `contactforms` database table.
5. An administrator can review saved messages through Django Admin.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd amazon
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

If you use Command Prompt instead:

```cmd
venv\Scripts\activate
```

### 3. Install dependencies

Install Django:

```bash
python -m pip install django
```

If your project uses image uploads, install Pillow as well:

```bash
python -m pip install Pillow
```

### 4. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin login.

### 6. Run the development server

```bash
python manage.py runserver
```

Open the website at:

`http://127.0.0.1:8000/`

Open the Django Admin panel at:

`http://127.0.0.1:8000/admin/`

## 📝 Important Notes

- Add the required database records through Django Admin before using pages that expect existing records.
- Configure your static and media files correctly for your environment.
- The men's, women's, and electronics routes currently include simple text responses in the reviewed source; they may need additional development to become full category pages.
- Before deployment, set `DEBUG = False`, use a secure environment-based `SECRET_KEY`, configure `ALLOWED_HOSTS`, and follow Django's production deployment checklist.
- Do not upload passwords, API keys, secret keys, or other sensitive configuration to GitHub.

## 🔮 Future Improvements

- Add complete product category pages.
- Improve form validation and error handling.
- Add product search and filtering.
- Improve mobile responsiveness and accessibility.
- Add automated tests.
- Configure production hosting and deployment.

## 👨‍💻 Author

**Your Name**

GitHub: [Your GitHub Profile](https://github.com/)

---

*Built as a Django web development project to practice routing, templates, database models, form handling, and Django Admin integration.*
