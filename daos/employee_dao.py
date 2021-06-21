from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement


class EmployeeDAO(ABC):

    @abstractmethod
    def get_past_requests(self, employee_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def get_pending_requests(self, employee_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def get_all_requests(self, employee_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def get_all_employees(self):
        pass
