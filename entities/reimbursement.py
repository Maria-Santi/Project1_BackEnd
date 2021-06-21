class Reimbursement:

    def __init__(self, request_id: int, employee_id: int, manager_id: int, amount: int, reason: str,
                 request_status: str, request_message: str):
        self.request_id = request_id
        self.employee_id = employee_id
        self.manager_id = manager_id
        self.amount = amount
        self.reason = reason
        self.request_status = request_status
        self.request_message = request_message

    def as_json_dict(self):
        return {
            "requestID": self.request_id,
            "employeeID": self.employee_id,
            "managerID": self.manager_id,
            "amount": self.amount,
            "reason": self.reason,
            "requestStatus": self.request_status,
            "requestMessage": self.request_message
        }
