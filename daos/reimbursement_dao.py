from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement


class ReimbursementDAO(ABC):

    @abstractmethod
    def create_request(self, employee_id: int, manager_id: int, request: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def get_request_by_id(self, request_id) -> Reimbursement:
        pass


