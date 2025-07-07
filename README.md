# Department Master CRUD API – FastAPI + MongoDB

This project provides a RESTful CRUD API for managing Department Master records, built using FastAPI and MongoDB.

---

## 🔧 Technologies Used

- Python
- FastAPI
- Pydantic
- MongoDB (via PyMongo)
- Swagger UI for API documentation

---

## ▶️ Setup Instructions

### 1. Clone or Download the Project

```bash
git clone https://github.com/Shashank135/department-crud-fastapi.git
cd department_api
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install fastapi uvicorn pymongo python-dotenv
```

### 3. MongoDB Setup

Start MongoDB with a custom data path:

```bash
mongod --dbpath ~/mongo-data
```

> Make sure to keep this terminal running.

---

### 4. Run FastAPI App

```bash
uvicorn main:app --reload
```

Swagger UI:  
[http://127.0.0.1:8000/docs]

---

## 📸 Screenshots

### 1. Create Department
(screenshots/post_department.png)

### 2. Get All Departments
(screenshots/get_all_departments.png)

### 3. Get Department by ID
(screenshots/get_by_id.png)

### 4. Update Department
(screenshots/update_department.png)

### 5. Delete Department
(screenshots/delete_department.png)


---

## 📁 File Structure

```
department_api/
├── main.py
├── models.py
├── database.py
├── .env
├── README.md
└── requirements.txt
```

---

## 📌 Notes

- Make sure MongoDB is running before launching the app.
- Tested on macOS with MongoDB 8.0 and FastAPI.
