# skillswap

**1. Set Up Virtual Environment:**
   - Navigate into the project directory:

     ```bash
     cd <project_directory>
     ```

   - Create a virtual environment:

     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment:

     - On Windows:

       ```bash
       venv\Scripts\activate
       ```

     - On Unix or MacOS:

       ```bash
       source venv/bin/activate
       ```

**2. Install Dependencies:**
   - Install the project dependencies using `requirements.txt`:

     ```bash
     pip install -r requirements.txt
     ```

**3. Configure Database:**
   - Update the database settings in the project's `settings.py` file.
   - Run migrations to apply the database schema:

     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

**4. Create Superuser:**
   - Create a superuser for accessing the Django admin interface:

     ```bash
     python manage.py createsuperuser
     ```

   - Follow the prompts to set up a username, email, and password.

**5. Run the Development Server:**
   - Start the Django development server:

     ```bash
     python manage.py runserver
     ```

   - Open a web browser and navigate to `http://localhost:8000` to see your project.

**6. Access Admin Interface:**
   - Log in to the Django admin interface using the superuser credentials:

     ```
     http://localhost:8000/admin/
     ```