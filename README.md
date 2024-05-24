# Chatbot Project

This project is a simple web-based chatbot application that can respond to user questions based on data from a CSV file. Users can also upload a new CSV file to update the chatbot's responses.

## Features

- Interactive chat interface where users can ask questions.
- Ability to upload a new CSV file to update the chatbot's responses.
- Initial data loading from a default CSV file.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- A web browser

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/chatbot_project.git
    cd chatbot_project
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

  

3. **Create a new Django project and app if not already created:**

    ```bash
    django-admin startproject project
    cd project
    django-admin startapp chat
    ```

4. **Set up your Django settings:**

    - Add `'chat'` to `INSTALLED_APPS` in `project/settings.py`.
    - Set up your database (SQLite by default).

5. **Migrate the database:**

    ```bash
    python manage.py migrate
    ```
6.python manage.py runserver 8001
