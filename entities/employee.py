class Employee:

    def __init__(self, employee_id: int, manager_id: int, emp_name: str, emp_email: str, emp_password: str):
        self.employee_id = employee_id
        self.manager_id = manager_id
        self.emp_name = emp_name
        self.emp_email = emp_email
        self.emp_password = emp_password

    def as_json_dict(self):
        return {
            "employeeID": self.employee_id,
            "managerID": self.manager_id,
            "employeeName": self.emp_name,
            "employeeEmail": self.emp_email,
            "employeePassword": self.emp_password
        }
