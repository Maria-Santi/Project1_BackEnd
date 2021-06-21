class Manager:

    def __init__(self, manager_id: int, manager_name: str, manager_email: str, manager_password: str):
        self.manager_id = manager_id
        self.manager_name = manager_name
        self.manager_email = manager_email
        self.manager_password = manager_password

    def as_json_dict(self):
        return {
            "managerID": self.manager_id,
            "managerName": self.manager_name,
            "managerEmail": self.manager_email,
            "managerPassword": self.manager_password
        }
