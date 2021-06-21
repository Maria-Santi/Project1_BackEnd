from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement


class ReimbursementService(ABC):

    @abstractmethod
    def add_request(self, employee_id: int, manager_id: int, request: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def retrieve_request_by_id(self, request_id: int) -> Reimbursement:
        pass

