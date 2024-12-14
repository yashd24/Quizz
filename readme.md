# Quizz 

## Overview
The goal of this project is to create a simple web application where a user can participate in a quiz session, answer multiple-choice questions, and track their performance (correct/incorrect answers).


- **Live Website:** **[Quizz](https://quizz-beta-one.vercel.app/)**
- **Live Backend REST APIs url**: https://quizz-6vtz.onrender.com.app/

## Features
- **Start New Quiz Session**: Users can start a new quiz session with random questions.
- **Answer Questions**: Users can view and answer multiple-choice     questions.

- **Track Results**: Displays the number of questions answered, with details on correct and incorrect submissions.

## Technologies Used:
- **Django**
- **Django REST Framework**
- **PostgreSQL**
- **HTML/CSS**
- **JavaScript**


## Installation

### Running the Backend Service as Localhost

1. Clone the repository:
    ```bash
    git clone https://github.com/yashd24/Quizz.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Quizz
    ```

3. Configure Environment Variables. 
Create an `.env` file in the ./Quiz_BE directory.


```bash
# Database Configuration

DB_USER=<your_db_user>
DB_HOST=<your_db_host_url>
DB_PASSWORD=<your_db_password>
DB_NAME=<your_db_name>
DB_PORT=<yout_db_port>

# Django Configuration
DJANGO_SECRET_KEY=<your_secret_key>

```

4. Install Requirements:
    ```bash
    pip install -r requirements.txt
    ```

5. Migrate the database:
    ```bash
    python manage.py migrate
    ```
6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
Server starts from index.html file.


## Contact
For any questions or feedback, please contact [yashd2024@gmail.com](mailto:yashd2024@gmail.com).
