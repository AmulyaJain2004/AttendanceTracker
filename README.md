# AttendanceTracker 📚

A Django-based web application to track and manage class attendance for university students. Tired of maintaining records of missed classes for minimum percentage criteria? This attendance tracker is here to help!

## 🚀 Features

- **Course Management**: Create and manage multiple courses
- **Attendance Recording**: Record attendance for multiple classes per day
- **Attendance Tracking**: Track attendance status (Present, Absent, Cancelled)
- **Progress Monitoring**: View attendance percentage for each course
- **Class Details**: Track time duration and date for each class
- **User-Friendly Interface**: Clean and intuitive web interface

## 🛠️ Tech Stack

- **Backend**: Django 5.0.7
- **Database**: SQLite3 (default)
- **Frontend**: HTML, CSS, Bootstrap (via Django templates)
- **Package Management**: Pipenv
- **Python Version**: 3.12

## 📋 Prerequisites

- Python 3.12 or higher
- pip (Python package installer)
- pipenv (recommended) or virtualenv

## 🔧 Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd AttendanceTracker
   ```

2. **Set up virtual environment using Pipenv (Recommended)**

   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```

   **OR using venv**

   ```bash
   python -m venv attendance_env
   attendance_env\Scripts\activate  # On Windows
   # source attendance_env/bin/activate  # On macOS/Linux
   pip install django
   ```

3. **Navigate to the Django project directory**

   ```bash
   cd attendance_tracker
   ```

4. **Run database migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Start the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the application**

   Open your web browser and go to: `http://127.0.0.1:8000/`

## 📱 Usage

### Creating Courses

1. Navigate to the home page
2. Click on "Create Course"
3. Enter the course name
4. Submit to create the course

### Recording Attendance

1. From the home page, click "Submit Attendance"
2. Select the number of classes attended (1-6)
3. For each class, fill in:
   - Course name
   - Time duration (format: HH:MM-HH:MM, e.g., 14:45-15:45)
   - Attendance status (YES/NO/CANCELLED)
4. Submit the attendance records

### Viewing Course Details

1. Click on any course from the home page
2. View detailed attendance records
3. See attendance percentage and statistics

## 📁 Project Structure

```text
AttendanceTracker/
├── Pipfile                     # Pipenv dependencies
├── Pipfile.lock               # Locked dependencies
├── README.md                  # Project documentation
└── attendance_tracker/        # Django project root
    ├── manage.py              # Django management script
    ├── db.sqlite3             # SQLite database
    ├── attendance/            # Main Django app
    │   ├── __init__.py
    │   ├── admin.py           # Admin interface configuration
    │   ├── apps.py            # App configuration
    │   ├── forms.py           # Django forms
    │   ├── models.py          # Database models
    │   ├── tests.py           # Unit tests
    │   ├── urls.py            # URL routing
    │   ├── views.py           # View functions
    │   └── migrations/        # Database migrations
    ├── attendance_tracker/    # Project settings
    │   ├── __init__.py
    │   ├── asgi.py            # ASGI configuration
    │   ├── settings.py        # Django settings
    │   ├── urls.py            # Main URL configuration
    │   └── wsgi.py            # WSGI configuration
    ├── static/                # Static files (CSS, images)
    │   └── css/
    └── templates/             # HTML templates
        ├── base.html
        ├── course_detail.html
        ├── create_course.html
        ├── fill_attendance.html
        ├── index.html
        └── submit_attendance.html
```

## 🎯 Models

### Course Model

- `name`: Course name (CharField)
- Methods:
  - `total_classes()`: Returns total number of classes
  - `attended_classes()`: Returns number of attended classes
  - `attendance_percentage()`: Calculates attendance percentage

### AttendanceRecord Model

- `course`: Foreign key to Course
- `date`: Auto-generated date field
- `time_duration`: Time duration of the class
- `attended`: Choice field (YES/NO/CANCELLED)

## 🌐 URL Patterns

- `/` - Home page (course list)
- `/create_course/` - Create new course
- `/submit/` - Submit attendance form
- `/fill_attendance/<num_classes>/` - Fill attendance details
- `/course/<course_id>/` - Course detail view

## 🔮 Future Enhancements

- [ ] User authentication and authorization
- [ ] Export attendance data to CSV/PDF
- [ ] Email notifications for low attendance
- [ ] Mobile-responsive design improvements
- [ ] Attendance analytics and charts
- [ ] Bulk import/export functionality
- [ ] Calendar integration
- [ ] Attendance reminders

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📞 Support

If you encounter any issues or have questions, please:

1. Check the existing issues in the repository
2. Create a new issue with detailed information
3. Provide steps to reproduce any bugs

## 👥 Authors

- Amulya Jain - Initial work

---

Happy Tracking! 📈
