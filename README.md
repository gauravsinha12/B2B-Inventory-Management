# B2B Inventory Management

A Django-powered web application for managing products, orders, enquiries, and user profiles in a business-to-business environment.  
The project uses HTMX and Tailwind CSS for dynamic frontend interactions and a responsive UI.

---

## 🧩 Project Structure

- `app_fireworks/` – Django project settings and ASGI/WSGI entrypoints.
- `base/` – Main application containing models, views, templates, and static assets.
  - `models/` – Data definitions (users, products, orders, addresses, enquiries, cart items).
  - `views/` – HTMX components, auth flows, page controllers, and token utilities.
  - `templates/` – HTML templates for pages, partials, icons, and admin UI.
  - `static/` – CSS, JS (alpine.js, htmx), images, and Tailwind build files.
  - `templatetags/` – Custom template filters/tags.
  - `migrations/` – Django schema migrations.

Other top-level files:

- `manage.py` – Django CLI.
- `requirements.txt` – Python dependencies.
- `tailwind.config.js` – Tailwind CSS configuration.
- `vercel.json` – Deployment settings (presumably for Vercel).
- `build.sh` – Build script (probably for assets).
- `.vscode/settings.json` – Workspace settings.
- `todo.md` – Project TODO list.

---

## 🚀 Getting Started

1. **Clone the repo**  
   ```bash
   git clone <your-repo-url>
   cd B2B-Inventory-Management
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python -m venv .venv
   .venv\Scripts\activate     # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Collect static files (if needed)**  
   ```bash
   python manage.py collectstatic
   ```

6. **Run the development server**  
   ```bash
   python manage.py runserver
   ```

7. **Access the app**  
   Open `http://127.0.0.1:8000` in your browser.

---

## 🛠️ Features

- User authentication (signup, login, profile, password reset).
- Product catalogue with categories, brands, featured items.
- Shopping cart and checkout workflows using HTMX for seamless updates.
- Order management and enquiry tracking.
- Admin dashboard for managing products, orders, users, enquiries.
- Responsive UI built with Tailwind CSS and HTMX for partial page updates.
- Custom template tags for reusable functionality.
- Token-based account activation and email templates.

---

## 📝 Development Notes

- Templates are split into partials and icon components for reusability.
- HTMX components in `base/views/Htmx.py` handle many AJAX-like interactions.
- Staff/admin pages reside under `templates/admin` and `views/pages/admin.py`.
- `base/models/constants.py` contains shared constants (e.g. status choices).
- Static assets include Alpine.js, HTMX, and custom styles.

---

## ✅ Deployment

Configuration exists for Vercel (`vercel.json`). Ensure environment variables are set, run `build.sh` to compile assets, and push to your hosting provider.

---

## 📌 TODO & Improvements

See [`todo.md`](todo.md) for ongoing tasks and enhancement ideas, such as:

- Add API endpoints.
- Improve mobile layout.
- Add comprehensive test coverage (`base/tests.py`).
- Optimize performance and caching.

---

## 📄 License

Specify your project license here (e.g. MIT, GPL).

---

Feel free to expand this README with additional setup instructions, architecture decisions, or contribution guidelines as the project evolves!
