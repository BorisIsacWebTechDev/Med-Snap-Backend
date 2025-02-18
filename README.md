📜 Documentation for Med-Snap
In the root directory (./), there is a file named CODEOWNERS, which defines the responsible reviewers for Python and JavaScript code.

1️⃣ Installation of GitHub
    1.1 Installing Git on Windows
    Download Git from the official website: Git for Windows.

    https://git-scm.com/downloads/win

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

Verify the installation

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

    python -m venv <my_venv>

exemple:

    python -m venv venv

In my case an environment will be named "venv".

Activate a Virtual Environment
Windows:

    <relative_path_to_venv>\venv\Scripts\activate

Linux/macOS:

    source <relative_path_to_venv>/venv/bin/activate

Now your virtual environment is active! On your bash should write name of your Environment before username
in my case my env is VENV and it shows me  
    
    (venv) <username> MINGW64 ~/<absolute_path_to_project> (<branch_name>)


Installation of dependencies:
Into Med-Snap-Backend, we have a requirements.txt
Run installation from requirements.txt with command 

    pip install -r requirements.txt

in terminal.
A position on terminal should be in Med-Snap-Backend. 
It will install all dependencies in your Virtual Environment

Postgres PSQL:

After installing PostgreSQL (psql), we need to create a superuser using the command:
    
    "CREATE ROLE spawnkid19xxsnap WITH SUPERUSER LOGIN PASSWORD 'your_password';

Into folder secret_folder in psql_Boris_data.py file insert in variable psql_password = 'your_password'
('your_password' is pass witch you indicate while created a superuser spawnkid19xxsnap)

After installing PostgreSQL (psql), we need to create a superuser using the following command:

    CREATE ROLE spawnkid19xxsnap WITH SUPERUSER LOGIN PASSWORD 'your_password';

Then, in the psql_Boris_data.py file inside the secret_folder, insert the password into the psql_password variable:

psql_password = 'your_password'
('your_password' is the password you set when creating the superuser spawnkid19xxsnap.) 
    
This superuser is created for testing and permissions. Additionally, this user is stored in the secret_files as the main user.

Now, let's grant permissions on the local machine using:
    
    ALTER USER spawnkid19xxsnap CREATEDB CREATEROLE;
    
To verify if the user exists, run:
    
    "\du"

After that, create a database named "snap".

    CREATE DATABASE <db_name>;

Now it is time to import the database file.
If you are still inside the psql terminal, exit by typing:

    \q

Then, in your terminal or command line, run:

    "psql -U spawnkid19xxsnap -d snap -W -f '<path_to_db>/mydb_backup.sql'"
    
👉 Replace <path_to_db> with the actual path to your .sql file.

Insert a password for the superuser spawnkid19xxsnap.

And finally run project.

Navigate to Your Django Project
    Open a terminal and move into your project directory: "cd /path/to/your/django_project"
    Your position should be in the same level with file "manage.py". then Run server with command "python manage.py runserver" or
    "python3 manage.py runserver" if you use linux.
    Open browser and insert a next link http://127.0.0.1:8000/ this link should redirect you to index page



# Single User  

A **Single User** is a doctor who works alone. They can register themselves but cannot add other users.  

## Registration for a Single User  

A **Single User** can register only if they are a doctor. They must fill in all the required fields:  

- **First Name** (`CharField`)  
- **Last Name** (`CharField`)  
- **Email** (`CharField`)  
- **Contact Number** (`Phone Number → CharField`)  
- **Gender** (`CharField` → Male, Female)  
- **Medical Order ID** (`CharField`)  
- **Specialty Type** (`CharField` → type1, type2, ...)  
- **Password**
- **Confirm Password**

---
📌 *This registration is intended for individual doctors who do not belong to a clinic.*  

## Login for Single User  

To log in, the user must enter a registered email and password.  

- If the email or password is incorrect, the user should receive an error message detailing the issue.  
- The system should not specify whether the email exists for security reasons.  

# Hospital User  

A **Hospital User** represents a hospital with at least two employees.  

- A **Superuser** (chief doctor or administrator) can add different types of employees, such as:  
  - **Receptionists**  
  - **Doctors**  
  - **Other staff members**  

## Registration for a Hospital User  

## Registration and Login  

- A **Hospital User** can register themselves.  
- After logging in, they can add other employees.  
- They must fill in all the required fields during registration.  

### Required Fields  

- **Name** (`CharField`)  
- **Tax ID** (`CharField`)  
- **Clinical Type** (`CharField`)  
- **Contact Number** (`CharField`)  
- **Head Physician** (`CharField`)  
- **Email** (`CharField`)  
- **Country** (`CharField`)  
- **City** (`CharField`)  
- **Address** (`CharField`)  
- **ZIP Code** (`CharField`)  
- **Website** (`CharField`)  
- **Number of Staff** (`IntegerField`)  
- **Number of Doctors** (`IntegerField`)  
- **Password** (`CharField`)  
- **Confirm Password** (`CharField`)  

---

📌 *This registration is intended for hospitals.*  




# DataBase employee MODEL
Database for employees has few classes.

# Employee Management System (Django)

A Django-based employee management system for medical record-keeping. This system supports both individual doctors and hospitals with multiple employees.
Features

✔️ User authentication and role-based access
✔️ Support for individual doctors and hospital organizations
✔️ Receptionists and doctors as separate user types
✔️ Medical specialization and registration system
✔️ Scalable hospital structure with a head physician



- **AbstractSingleCustomUser** - is represent all employee individuals. Contain next fields:
    - first_name --> models.CharField(max_length=50)
    - last_name --> models.CharField(max_length=50)
    - email --> models.EmailField(unique=True)
    - contact_number --> models.CharField(max_length=20)
    - gender --> models.CharField(["select", "male", "female"])  
    - role --> models.CharField(["select", "Receptionist", "Dr"])
    - is_active = models.BooleanField(default=True)
    - is_staff = models.BooleanField(default=False)

- **ReceptionsClinicalEmployee** - is represent receptionists. Is inherit from **AbstractSingleCustomUser** and do not contain any additional fields


- **DrClinicalEmployee** - is represent Doctors. Is inherit from **AbstractSingleCustomUser** and contain few additional fields:
    - medical_order_id = models.CharField(max_length=50, unique=True)
    - specialty_type = models.CharField(max_length=50)

- **CustomUser** - is represent Dr(singular or plural). Is inherit from **DrClinicalEmployee** and contain few additional fields:
    - user_type = models.CharField(['single',' Hospital'])  

- **HospitalUser** - is represent Dr(singular or plural). Is inherit from **CustomUser** and contain few additional fields:
    - head_physician = models.ForeignKey(
        "DrClinicalEmployee", 
        verbose_name=_(""), 
        on_delete=models.CASCADE, 
        related_name='hospital_head_physician'
        )
    - clinical_name = models.CharField(max_length=100)
    - tax_id = models.CharField(max_length=50, unique=True)
    - clinical_type = models.CharField(max_length=50)
    - country = models.CharField(max_length=50)
    - city = models.CharField(max_length=50)
    - address = models.TextField()
    - zip_code = models.CharField(max_length=10)
    - website = models.URLField(blank=True, null=True)
    - num_staff = models.CharField(
        beginner = '1-5', '1-5'
        medium = '6-10', '6-10'
        large = '11-20', '11-20'
        very_large = '21-50', '21-50'
        huge = '50+', '50+')

