# Office Portal - Document Comparison Tool

## Overview
This project implements a corporate **Office Portal**, which offers various tools and programs for internal company use. One of the primary tools available in this portal is a **PDF document comparison tool**, which compares uploaded PDF files against a **master DOCX file** and visually displays the differences on the web interface.

The comparison is highlighted with **green** for similarities and **red** for differences, allowing users to quickly identify changes between the two documents.

Additionally, the portal includes a **login system** that ensures secure access to the tools, utilizing hashed passwords for authentication.

## Features

### 1. Document Comparison
- **Functionality**: Compares a user-uploaded **PDF** document with a **master DOCX** file.
- **Visual Differences**:
   - **Green highlights** indicate matching content between the PDF and the DOCX.
   - **Red highlights** indicate differing content.
- **Supported Formats**:
   - Input: `.pdf` (user-uploaded document) and `.docx` (master document).

### 2. Login System
- **Secure Authentication**: Users must log in to access the tools within the portal.
- **Password Hashing**: Passwords are stored securely using **bcrypt hashing**, ensuring that user credentials are not stored in plain text.
- **User Sessions**: After login, the user's session is maintained, and they can access the comparison tool until they log out.

### 3. Cache Control and Session Handling
- **Session Management**: The session is cleared after logging out, and the cache is invalidated to prevent unauthorized access using browser navigation (e.g., back button).
- **No Caching**: Ensures that sensitive data is not stored or accessible after logout by disabling page caching.

### 4. Error Handling and File Validation
- **File Type Validation**: The system validates the file formats before processing, ensuring that only **PDF** and **DOCX** files are allowed. If the files are of an unsupported format, users receive an error message.
- **Error Feedback**: If an error occurs (e.g., missing file, incorrect format), the user is notified with a clear message via the Flask **flash** mechanism.

### 5. Visual and User-Friendly Interface
- **Intuitive Interface**: The user interface is designed for simplicity and ease of use, making it easy for employees to upload and compare documents.
- **Responsive Design**: The interface is responsive, making it accessible from different devices, including desktops and mobile devices.

## Major Python Libraries Used

1. **Flask**:
   - Web framework used to build the application, including routing, template rendering, and session management.
   
2. **bcrypt**:
   - Provides secure password hashing for the login system.

3. **docx (python-docx)**:
   - Library used to read and parse DOCX (Microsoft Word) files.

4. **PyPDF2**:
   - Library used to read and extract text from PDF files.

5. **difflib**:
   - Python standard library used for comparing sequences, such as lines of text.

6. **werkzeug**:
   - Utility library used for securely handling file uploads and generating secure filenames.

7. **magic (python-magic)**:
   - Library used for MIME type detection to ensure valid file formats before processing.

## Installation and Setup

### Prerequisites:
- Python 3.x
- Virtual environment (optional but recommended)

### Steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/office-portal.git
   cd office-portal

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   
4. **Create a .env file: Add necessary environment variables such as the SECRET_KEY and database connection string if needed.**
   Example .env file:
   ```bash
   SECRET_KEY=your_secret_key
   
5. **Run the application**:
   ```bash
   flask run


### Project Structure:
  ```markdown
  your-flask-project/
  ├── app/                   # Application modules
  │   ├── __init__.py        # Flask app initialization
  │   ├── models.py          # Database models
  │   └── compare.py         # Document comparison logic
  ├── static/                # Static files (CSS, JavaScript, images)
  │   └── assets/            # Assets like CSS files, images
  ├── templates/             # HTML templates
  │   ├── compare.html       # Comparison page
  │   ├── compare_result.html # Comparison result page
  │   └── login.html         # Login page
  ├── uploads/               # Directory for user-uploaded files (ignored by Git)
  ├── venv/                  # Virtual environment (ignored by Git)
  ├── config.py              # Configuration settings
  ├── server.py              # Main Flask app entry point
  ├── requirements.txt       # Project dependencies
  └── .gitignore             # List of files and directories ignored by Git
  ```

Usage
**Login:** 
Navigate to the login page and log in with your credentials.

**Upload Files:** After login, you can upload a PDF and a DOCX file.

**View Comparison:** Once files are uploaded, the system will compare the contents and display the results visually.

**Logout:** Securely log out of the system.

**Notes**:
Make sure the environment variables are set up correctly in the .env file.
The uploads/ directory is not included in the repository to protect user privacy and prevent unnecessary file bloat. Create it locally if needed.

