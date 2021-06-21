from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement


class EmployeeService(ABC):

    @abstractmethod
    def retrieve_all_past_requests(self, employee_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def retrieve_all_pending_requests(self, employee_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def retrieve_all_requests(self, employee_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def retrieve_all_employees(self):
        pass