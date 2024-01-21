# Book Management System with Django and SQLite

This project is a simple Book Management System implemented using Django as the backend framework and SQLite as the database. The frontend is built using HTML, Bootstrap, and Axios for asynchronous HTTP requests.

## Project Structure

- **HTML Frontend:** The frontend is a simple HTML form for adding and updating books, and a list to display existing books. Bootstrap is used for styling.

- **Django Backend:** The backend is implemented with Django, a high-level Python web framework. It includes the necessary Django app, model, views, and URL configurations to handle book-related operations (CRUD - Create, Read, Update, Delete).

- **SQLite Database:** Django uses SQLite as the default database for simplicity in this project. However, the database engine can be changed in the Django settings if needed.

## Setup Instructions

1. **Install Dependencies:**
   - Make sure you have Python installed.
   - Install Django by running: `pip install Django`

2. **Migrate Database:**
   - Navigate to the project directory containing `manage.py`.
   - Run the following commands to apply migrations and create the database:
     ```
     python manage.py makemigrations
     python manage.py migrate
     ```

3. **Run the Development Server:**
   - Start the Django development server by running: `python manage.py runserver`
   - The server will be accessible at `http://127.0.0.1:8000/`.

4. **Access the Application:**
   - Open a web browser and go to `http://127.0.0.1:8000/` to interact with the Book Management System.

## Frontend Logic

- The HTML form allows users to add new books with details such as name, author, and publication year.
- Existing books are displayed in a list, each with options to delete or update.

## Backend Logic

- The Django backend handles CRUD operations for books through RESTful API endpoints.
- The `books` app includes a model for the book, views for handling HTTP requests, and URL configurations to map endpoints.

## Axios for Asynchronous Requests

- The frontend uses Axios to asynchronously send requests to the Django backend for adding, updating, and deleting books without refreshing the page.

## Future Improvements

- Enhance frontend with more user-friendly features and validation.
- Implement user authentication for secure operations.
- Explore using a more robust database engine for production.

Feel free to explore and modify the code to suit your needs. If you encounter any issues or have suggestions, please refer to the Django documentation or create an issue in this repository. Happy coding!
