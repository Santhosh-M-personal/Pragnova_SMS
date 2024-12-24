
---

# Student Management System (SMS)  

Welcome to the **Student Management System (SMS)** project repository. This application provides a robust backend for managing student data, course enrollment, mentorship features, and administrative operations.  

## Tech Stack  

- **Backend Language**: Python  
- **Framework**: FastAPI  
- **Database**: PostgreSQL (for transactional data) and MongoDB (for mentor and feedback data)  

## Features  

- Add, edit, and delete student records.  
- Search for students by name or ID.  
- View all student details in a list format (admin functionality).  
- Scalable and secure backend architecture.  

## Getting Started  

Follow the steps below to set up the project on your local machine.  

### 1. Clone the Repository  

Clone this repository to your local system using:  

```bash  
git clone https://github.com/YourUsername/Student-Management-System.git  
```  

Navigate into the project directory:  

```bash  
cd Student-Management-System  
```  

### 2. Create and Activate a Virtual Environment  

It's recommended to use a virtual environment to manage dependencies:  

- **For Windows**:  
  ```bash  
  python -m venv venv  
  venv\Scripts\activate  
  ```  

- **For macOS/Linux**:  
  ```bash  
  python3 -m venv venv  
  source venv/bin/activate  
  ```  

### 3. Install Dependencies  

With the virtual environment activated, install the required dependencies:  

```bash  
pip install -r requirements.txt  
```  

### 4. Set Up the Databases  

1. **PostgreSQL**:  
   - Create a PostgreSQL database for transactional data.  
   - Update the database connection details in the `.env` file (e.g., database name, username, password).  


### 5. Initialize the Database Schema  

Run the following script to create the required PostgreSQL tables:  

```bash  
python create_tables.py  
```  

### 6. Run the Application  

Start the FastAPI application by executing:  

```bash  
uvicorn main:app --reload  
```  

The application will be hosted locally at `http://127.0.0.1:8000`.  

### 7. Access the API Documentation  

FastAPI provides interactive API documentation via Swagger UI. Access it at:  

```text  
http://127.0.0.1:8000/docs  
```  

Explore and test the API endpoints directly from this interface.  

## Contribution  

Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.  

## License  

This project is licensed under the MIT License.  

---  
