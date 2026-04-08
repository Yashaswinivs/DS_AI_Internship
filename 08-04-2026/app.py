print("App is starting...") 
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask is working!"

employees = [
    {'id': 1, 'name': 'Ashley'},
    {'id': 2, 'name': 'Kate'},
    {'id': 3, 'name': 'Joe'}
]

nextEmployeeId = 4

# GET all employees
@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employees)

# GET employee by ID
@app.route('/employees/<int:id>', methods=['GET'])
def get_employee(id):
    for emp in employees:
        if emp['id'] == id:
            return jsonify(emp)
    return jsonify({'error': 'Employee not found'}), 404

# POST (create new employee)
@app.route('/employees', methods=['POST'])
def create_employee():
    global nextEmployeeId
    employee = json.loads(request.data)
    employee['id'] = nextEmployeeId
    nextEmployeeId += 1
    employees.append(employee)
    return jsonify(employee), 201

# PUT (update employee)
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    updated = json.loads(request.data)
    for emp in employees:
        if emp['id'] == id:
            emp.update(updated)
            return jsonify(emp)
    return jsonify({'error': 'Employee not found'}), 404

# DELETE employee
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    global employees
    employees = [e for e in employees if e['id'] != id]
    return jsonify({'message': 'Deleted'}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)