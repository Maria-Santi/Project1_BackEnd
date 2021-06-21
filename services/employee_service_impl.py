from typing import List

from daos.employee_dao import EmployeeDAO
from entities.reimbursement import Reimbursement
from services.employee_service import EmployeeService


class EmployeeServiceImpl(EmployeeService):

    def __init__(self, employee_dao: EmployeeDAO):
        self.employee_dao = employee_dao

    def retrieve_all_past_requests(self, employee_id: int) -> List[Reimbursement]:
        return self.employee_dao.get_past_requests(employee_id)

    def retrieve_all_pending_requests(self, employee_id: int) -> List[Reimbursement]:
        return self.employee_dao.get_pending_requests(employee_id)

    def retrieve_all_requests(self, employee_id: int) -> List[Reimbursement]:
        return self.employee_dao.get_all_requests(employee_id)

    def retrieve_all_employees(self):
        return self.employee_dao.get_all_employees()
