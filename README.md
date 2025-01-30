📜 Documentation for Med-Snap
In the root directory (./), there is a file named CODEOWNERS, which defines the responsible reviewers for Python and JavaScript code.

1️⃣ Installation of GitHub
    1.1 Installing Git on Windows
    Download Git from the official website: Git for Windows.
    Install Git by following the setup instructions.
    Verify the installation by opening CMD (Command Prompt) or Git Bash and running:
    git --version

    ✅ Expected output:

    $ git --version
    git version 2.47.1.windows.2
    (The version number may be different depending on the latest Git release.)
    
    1.2 Installing Git on Linux
    Open a terminal and update your package list:
        sudo apt update
    Install Git:
        sudo apt install git
    Verify the installation:
        git --version

    ✅ Expected output:

    git --version
    git version 2.47.1
    (The version number may be different and possibly newer.)
2️⃣ Setting Up GitHub
    2.1 Initialize Git in Your Project
    First, create a new folder where you will store your project locally.
    Navigate to the folder and open a Bash terminal.
    2.2 Initialize Git
    Run the following command to initialize Git in your project:
    git init
    To confirm Git has been initialized, check for the .git directory:
    ls -al

    ✅ Expected output:
    drwxr-xr-x 1 boris 197611 0 Jan 30 14:50 .git/
    2.3 Add a Remote Repository
    Run the following command, replacing YOUR-TOKEN with your personal access token:
    git remote add origin https://YOUR-TOKEN@github.com/BorisIsacWebTechDev/Med-Snap-Backend.git
    2.4 Verify the Remote Repository
    Check if everything worked by running:
    git remote -v

    ✅ Expected output:
    origin  https://YOUR-TOKEN@github.com/BorisIsacWebTechDev/Med-Snap-Backend.git (fetch)
    origin  https://YOUR-TOKEN@github.com/BorisIsacWebTechDev/Med-Snap-Backend.git (push)
    2.5 Confirm Permissions
    Check with the administrator if you have the necessary permissions to contribute to the repository.
    2.6 Clone the Repository
To get a local copy of the repository, run:
git clone https://github.com/BorisIsacWebTechDev/Med-Snap-Backend.git

⚠️ IMPORTANT: Best Practices
✔ Always create a new branch based on the main branch before starting your work.
✔ Use meaningful commit messages to describe your changes clearly.
✔ Push your changes regularly to avoid losing progress.
✔ Follow the repository guidelines for code style and structure.


Install and Create a Virtual Environment
1️⃣ Install Virtual Environment
Open a terminal and type:
    pip install virtualenv
2️⃣ Create a Virtual Environment
    Run the following command in the terminal:
        python -m venv venv

Activate a Virtual Environment
    Windows:
        <relative_path_to_venv>\venv\Scripts\activate
    Linux/macOS:
        source <relative_path_to_venv>/venv/bin/activate
    Now your virtual environment is active! On your bash should write name of your Environment before username
    in my case my env is VENV and it show me  
    (VENV) <username> MINGW64 ~/<absolute_path_to_project> (<branch_name>)


Installation of dependecies:
    Into Med-Snap-Backend, we have a requirements.txt
    Run instalation from requirements.txt with command "pip install -r requirements.txt" in terminal.A position on terminal should be in Med-Snap-Backend. It will install all dependencies in your Virtual Environment

Postger PSQL:
    After installing PostgreSQL (psql), we need to create a superuser using the command:
    
    "ALTER USER spawnkid19xxsnap WITH SUPERUSER;" 
    
    This superuser is created for testing and permissions. Additionally, this user is stored in the secret_files as the main user.

    Now, let's grant permissions on the local machine using:
    "ALTER USER spawnkid19xxsnap CREATEDB CREATEROLE;"
    
    To verify if the user exists, run:
    
    "\du"

    After that, create a database named "snap".

    Now it is time to import the database file.
    If you are still inside the psql terminal, exit by typing:

    "\q"
    Then, in your terminal or command line, run:

    "psql -U spawnkid19xxsnap -d snap -W -f '<path_to_db>/mydb_backup.sql'"
    
    👉 Replace <path_to_db> with the actual path to your .sql file.


Navigate to Your Django Project
    Open a terminal and move into your project directory: "cd /path/to/your/django_project"
    Your path should be in the same level with file "manage.py". then Run server with comand "python manage.py runserver" or
    "python3 manage.py runserver" if you use linux.
    Open browser and insert a next link
