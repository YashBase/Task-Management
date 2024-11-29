# Task Management App with Google Login

A simple web application built with **Django** and **Google OAuth** for user authentication. The app allows users to manage personal tasks after logging in using their Google accounts. Admin users can manage OAuth credentials and invite new users.

![Task Management App]   ![Login](https://github.com/user-attachments/assets/6766fc39-05c3-47a2-a2bb-021589a59329)


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
  ```

## Run the development server:
   ```bash
   python manage.py runserver
   ```
## Access the app:
- Open **http://localhost:8000** in your browser.

## Google OAuth Flow

- When users visit the app, they can log in using their Google account.
- After successful authentication, users will be redirected to their task dashboard.

## Admin Panel

1. **Create a superuser:**:
   ```bash
   python manage.py createsuperuser
   
2. **Admin features:**:

- Access the Django admin panel at **http://localhost:8000/admin/**.
- Admin can manage the Google OAuth keys, invite new users, and view all tasks.

  
# Task Management
  Users can:
  - **Create Tasks:** Title and description required.
  - **Edit Tasks:** Modify title or description.
  - **Delete Tasks:** Remove tasks from the list.

# Admin Features
  - **Manage OAuth Keys:** Admin can update Google OAuth credentials.
  - **Invite Users:** Admin can invite users by email, who will receive a registration link.

# Screenshots
1. **Login Screen:**
![Login](https://github.com/user-attachments/assets/6d877798-fe1a-41df-81dd-b752c481d87d)

2. **Task Dashboard:**
![dashboard](https://github.com/user-attachments/assets/bd08c521-62e2-419d-8270-6454987a12e7)

3. **Admin Panel:**
![Admin](https://github.com/user-attachments/assets/934ae279-6e42-46a5-858f-9fd921d57ace)

# Contributing
If you want to contribute to the development of this project, feel free to fork the repository and create pull requests. Please follow the steps below for contributing:

   1. Fork the repository.
   2. Create a feature branch ```bash git checkout -b feature-name ```.
   3. Commit your changes ```bash git commit -m 'Add new feature' ```.
   4. Push to the branch ```bash git push origin feature-name```.
   5. Open a pull request.
