# 💻 The Engineer’s Library

**The Engineer’s Library** is a Django web app that lets users explore a curated catalog of essential software engineering literature. This project demonstrates practical use of pagination, search filters, responsive UI, and structured data loading all built using Django and Bootstrap 5.


## 🚀 Objective

To build a fully functional Django application that:

* Loads a dataset of software engineering books
* Displays records with paginated views
* Offers flexible filtering by author, title, or publication year
* Supports responsive, Bootstrap-styled interfaces


## 💡 Discussion Questions & Answers

### 1. **Why is pagination important for large datasets?**

Pagination is more than a design pattern. It's a performance safeguard. Without pagination, attempting to render thousands of records can slow down or even crash the browser or server. Here’s why it's indispensable:

* **Performance Optimization**: Django queries only the necessary records per request, which means your database isn’t under strain and your page loads faster even if there are tens of thousands of entries behind the scenes.

* **User Experience**: Pagination breaks down content into manageable chunks. Instead of overwhelming the user, it invites them to navigate with intention especially important in libraries or catalogs where discovery matters.

* **Network Load Reduction**: Particularly for mobile users or those on limited bandwidth, pagination ensures only a subset of data is transferred, reducing latency and improving perceived speed.

* **Scalability**: Pagination prepares your application to grow. Whether your library has 50 books or 50,000, the frontend behavior remains consistent and predictable.

For instance in our project, we use Django's `Paginator` class:

```python
paginator = Paginator(books, per_page)
page_obj = paginator.get_page(page_number)
```

If we skipped pagination, visiting `/books/` would attempt to render **all books at once**, which would:

* Slow down the page load
* Overwhelm users with too much content
* Waste bandwidth, especially on mobile

Instead, by paginating 5, 10, or 20 books per page, we:

✅ Improve frontend performance

✅ Maintain a clean, readable UI

✅ Avoid loading unnecessary data

Example in action: When visiting `/books/?per_page=5`, only 5 books render on the page, regardless of total count. This was tested with 50+ records from a JSON fixture.

---

### 2. **How would you customize items per page dynamically?**

Customizing how many items show per page gives control to the user and flexibility to the developer. Here's how it's approached in a Django context:

* **User-Controlled Dropdown**: A dropdown in the UI allows the user to pick between, say, 5, 10, or 20 results per page. This value is captured via a GET parameter and passed to Django’s Paginator.

* **Responsive Design Consideration**: You can vary the default per_page based on screen size showing more items on large screens and fewer on mobile. While Django doesn't inherently know the screen size, JavaScript can be used to set a hidden field or redirect accordingly.

* **Preference Persistence**: You can store the user's choice in a session or cookie. That way, even if they return later, the interface respects their preferred layout.

* **Backed by Logic, Not Guesswork**: This isn’t just cosmetic. When implemented thoughtfully, it also feeds into your view logic, ensuring performance and UX scale together.

Making reference to the code base, we implemented a `<select>` dropdown in our template:

```html
<select name="per_page" id="per_page" class="form-select" onchange="this.form.submit()">
  {% for num in per_page_choices %}
    <option value="{{ num }}" {% if per_page|stringformat:'s' == num|stringformat:'s' %}selected{% endif %}>{{ num }}</option>
  {% endfor %}
</select>
```

This allows users to control how much data they see at once.

#### Unique Codebase Insight:

* The user's selection is captured as a `GET` param and used directly in the view.
* It gracefully defaults to 10 items if an invalid value is passed:

  ```python
  try:
      per_page = int(per_page)
  except ValueError:
      per_page = 10
  ```

This makes the feature resilient and adaptable to any screen size or user need.

---

### 3. **What happens if a page is invalid?**

Invalid pages can happen for many reasons: someone types a wrong page number in the URL, deletes a query string, or arrives via a broken link. Django’s Paginator gives us several graceful ways to manage it:

* **Fallback to the Last Valid Page**: If the user requests a page beyond the maximum number (e.g., page=9999 when only 10 pages exist), the app can redirect or render the last page available.

* **Default to Page 1**: A common approach is to treat an invalid request as a first-time visit and show page one. This avoids confusion and keeps users oriented.

* **Show a Custom Message**: Instead of crashing or silently failing, show a friendly message: “Oops! That page doesn’t exist. Let’s take you back.” Maybe add a "Go to first page" button.

* **Raise a 404 for APIs**: For public-facing APIs, strict behavior is usually better. Returning a 404 makes it clear that the client requested something outside of bounds.

This app opts for usability-first behavior keeping users within the experience flow and avoiding any dead ends.Django handles invalid pages using `get_page()` which prevents `404` errors and returns the **nearest valid page**.

Example:
If the user visits `/books/?page=999`, but only 4 pages exist, it shows page 4 rather than crashing.

This improves UX by:

* Keeping users on the site
* Avoiding confusing error messages
* Guiding them back to content instead of dead ends

Additionally, we display:

```html
<span class="page-link">Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>
```

to help users see where they are in the pagination flow.

This design choice keeps our app beginner-friendly and robust for edge cases.

---

## 🔧 Project Features

**✅ Django Setup & App Structure**
* A clean Django project with a dedicated books app.

* Fully functional Book model with fields for title, author, and published year.

* Admin interface registration for easy data management.

**✅ AI-Populated Book Dataset**
* Database populated with realistic software engineering-themed book entries.

* Fixture file created using AI to simulate a production-ready dataset.

**✅ Book List View with Pagination**
* Books are listed in alphabetical order.

* Pagination implemented using Django’s built-in Paginator.

* Dynamic items-per-page selection for user control.

**✅ Smart Filtering & Search**
* Users can filter books by:

* Author name

* Book title

* Year of publication

* Filter UI adapts based on the selected filter type.

* Uses HTML5 datalists for autocomplete functionality.

* Inputs validated to accept only alphabetic characters where applicable.
  ```javascript
  const regex = /^[A-Za-z\s]+$/;
  if (!regex.test(input.value)) alert('Only alphabetic characters allowed.');
  ```

**✅ Bootstrap-Based Responsive UI**
* Entire interface styled with Bootstrap 5.

* Fully responsive layout optimized for mobile and desktop.

* Custom CSS for enhanced card and pagination styling.

**✅ Template & Static Structure**
* HTML templates structured with clean separation of logic and presentation.

* Stylesheet extracted into a dedicated static CSS file.

* Static asset handling follows Django best practices.

**✅ Dark Mode for both the user and admin panel**

* Dark mode has been optionally applied using custom CSS:
* Location: `books/static/books/dark-mode.css`
* Automatically toggled on the public `/books/` view via a 🌙/☀️ icon

---

## 🔐 Django Admin Panel (Superuser Access)

The Engineer’s Library Admin interface provides a powerful way to manage your app’s data through a built-in UI. This section walks through the complete setup and enhancements made for the `Book` model in your project.

---

### 🚀 Step 1: Create a Superuser

To log in and manage data through the admin panel, you must first create an admin (superuser) account.

```bash
python manage.py createsuperuser
```

**Follow the prompts:**

* **Username:** `admin`
* **Email address:** l.ojoawo@alustudent.com
* **Password:** `admin'

This user will have full access to your project’s admin dashboard.

---

### 🌐 Step 2: Accessing the Admin Panel

Start the Django development server:

```bash
python manage.py runserver
```

Open your browser and go to:

🔗 [`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/)

> Use the credentials you just created (`admin` / `admin`) to log in.

---

### 📘 Step 3: Admin Registration for the `Book` Model

Your `Book` model has been enhanced for a better admin experience. The following customization is located in `books/admin.py`:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_year')  # Visible columns
    search_fields = ('title', 'author')                   # Search functionality
    list_filter = ('published_year',)                     # Sidebar filter
```

🛠️ **Features enabled:**

* **Table View**: Easily view book entries with essential fields.
* **Search Bar**: Quickly find books by title or author.
* **Year Filter**: Narrow down results using a published year filter.

---

### 📊 Step 4: Custom Admin Dashboard Widget

To personalize your admin homepage, a custom dashboard can be implemented using a template override (`templates/admin/index.html`). If configured, you'll see:

* **Total books** in the system
* **Number of unique authors**
* **Earliest published year**

Example block:

```html
{% extends "admin/index.html" %}
{% block content %}
  {{ block.super }}
  <div class="module">
    <h2>📊 Book Statistics</h2>
    <ul>
      <li>Total Books: {{ book_count }}</li>
      <li>Unique Authors: {{ unique_authors }}</li>
      <li>Earliest Year: {{ earliest }}</li>
    </ul>
  </div>
{% endblock %}
```

## 📸 Interface Preview

Here’s how **The Engineer’s Library Admin Panel Interface** looks in the browser:

![Light mode Preview](https://github.com/user-attachments/assets/c0801894-8ac0-409a-9676-8befbeaa7438)


Dark Mode Preview

![Dark mode Preview](https://github.com/user-attachments/assets/25ad2796-781d-4513-a150-09fc9c8cb6d4)


### 👥 Admin Access Summary

| Feature                | Description                                                  |
| ---------------------- | ------------------------------------------------------------ |
| **Login URL**          | [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) |
| **Username**           | `admin`                                                      |
| **Password**           | `admin` *(or whatever you set)*                              |
| **Admin Capabilities** | Add/edit/delete books, filter/search, view dashboard         |


---

## 💡 Bonus Functionality
* Alphabet-only input validation using JavaScript and HTML5 patterns.

* "Per Page" selector for adjustable pagination limits.

* Persistent filter state across paginated views.

* Developer-friendly branding and messaging tailored to a tech-savvy audience.
---

## 🚀 Getting Started (Local Setup)

To run the project locally:

1. **Clone the repository**

   ```bash
   git clone https://github.com/ALU-BSE/week-2-la-cool-devs-1.git
   cd week-2-la-cool-devs-1/pagination_project
   ```

2. **Set up a virtual environment and install dependencies**

   ```bash
   python -m venv env
   source env/bin/activate  # or env\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. **Run migrations and load sample data**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py loaddata books/fixtures/books.json
   ```

4. **Start the development server**

   ```bash
   python manage.py runserver
   ```

5. Visit the main app:
   📚 [http://127.0.0.1:8000/books/](http://127.0.0.1:8000/books/)


## 📦 Tech Stack
* Backend: Django (Python)

* Frontend: Bootstrap 5

* Data Source: AI-generated JSON via ChatGPT

* Database: SQLite (default Django setup)

## 📂 Folder Structure Overview
* pagination_project/ – Root Django project

* books/ – Django app with models, views, templates, and static files

* books/fixtures/books.json – Contains sample data to prepopulate the Book model

* templates/books/book_list.html – Main user-facing template

* static/books/script.js – JavaScript for form validation and interaction


## 📸 Interface Preview

Here’s how **The Engineer’s Library** looks in the browser:

![Light mode Preview](https://github.com/user-attachments/assets/aceaf3f7-f593-4ba0-9ea4-793cdce520f9)

DaRD Mode Preview

![Dark mode Preview](https://github.com/user-attachments/assets/75c7a71b-fdad-4433-ae81-9a49390caf49)




## 👥 Contributors

| Name           | GitHub Username                          |
| -------------- | ---------------------------------------- |
| Lydia Ojoawo   | [@lydia02](https://github.com/lydia02)   |
| Yvette Kwizera | [@ykwizera](https://github.com/ykwizera) |

---
🙌 Thank You
Happy coding and keep exploring clean software design practices!
Built with 💙 using Django & Bootstrap.
