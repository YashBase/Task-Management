# Task Management App with Google Login

A simple web application built with **Django** and **Google OAuth** for user authentication. The app allows users to manage personal tasks after logging in using their Google accounts. Admin users can manage OAuth credentials and invite new users.

![Task Management App](https://via.placeholder.com/800x400?text=Task+Management+App)  

## Features

- **Google Authentication**: Users can sign in using their Google account.
- **Task Management**:
  - Create, view, edit, and delete tasks.
  - Each task contains a title and description.
- **Admin Panel**:
  - Store and manage Google OAuth keys.
  - Admin can invite users via email with a registration link.

## Technologies Used

- **Django**: Backend framework to build the web application.
- **Google OAuth**: Used for user authentication with Google accounts.
- **SMTP**: For sending emails, including registration invitations for new users.
- **HTML/CSS/JS**: For creating the front-end interface.

## Setup

Follow the steps below to set up and run the project locally.

### Prerequisites

- Python 3.x
- Django 3.x or higher
- A Google Developer account for OAuth setup
- SMTP server details for email functionality (e.g., Gmail or other services)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/task-management-app.git
   cd task-management-app

2. **Create a virtual environment:**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
   
3. **Install dependencies:**:
   ```bash
   pip install -r requirements.txt

## Google OAuth Setup:

- Go to the Google Developer Console.
- Create a new project and enable the Google OAuth API.
- Create OAuth credentials and obtain the Client ID and Client Secret.
- Set up your redirect URI as **http://localhost:8000/accounts/google/login/callback/**.

## Update settings:

- In **settings.py**, add your Google OAuth credentials:
   ```python
   SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '<your-client-id>'.
   SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '<your-client-secret>'.

## Run migrations:
   ```bash
   python manage.py migrate

## Run the development server:
   ```bash
   python manage.py runserver

## Google OAuth Setup:


