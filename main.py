from fastapi import FastAPI, HTTPException # type: ignore
from models import Department
from database import department_collection

app = FastAPI()

# Helper function to convert MongoDB doc to Python dict
def serialize_department(doc):
    return {
        "department_id": doc["department_id"],
        "name": doc["name"],
        "code": doc["code"],
        "facility_id": doc["facility_id"],
        "active_status": doc["active_status"]
    }

@app.post("/department")
def create_department(dept: Department):
    if department_collection.find_one({"department_id": dept.department_id}):
        raise HTTPException(status_code=400, detail="Department ID already exists.")
    department_collection.insert_one(dept.dict())
    return {"message": "Department created successfully."}

@app.get("/department")
def get_all_departments():
    depts = department_collection.find()
    return [serialize_department(d) for d in depts]

@app.get("/department/{department_id}")
def get_department(department_id: str):
    dept = department_collection.find_one({"department_id": department_id})
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found.")
    return serialize_department(dept)

@app.put("/department/{department_id}")
def update_department(department_id: str, updated: Department):
    result = department_collection.update_one(
        {"department_id": department_id},
        {"$set": updated.dict()}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Department not found.")
    return {"message": "Department updated successfully."}

@app.delete("/department/{department_id}")
def delete_department(department_id: str):
    result = department_collection.delete_one({"department_id": department_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Department not found.")
    return {"message": "Department deleted successfully."}
