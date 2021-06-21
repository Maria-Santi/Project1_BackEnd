from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement


class ManagerService(ABC):

    @abstractmethod
    def retrieve_all_managers(self):
        pass

    @abstractmethod
    def approve_deny_requests(self, manager_id: int, employee_id: int, request_id: int, status: str, message: str) -> Reimbursement:
        pass

    @abstractmethod
    def retrieve_all_requests(self, manager_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def retrieve_all_past_requests(self, manager_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def retrieve_all_pending_requests(self, manager_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def view_statistics_for_manager(self, manager_id: int):
        pass

    @abstractmethod
    def view_all_statistics(self):
        pass
