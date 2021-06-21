from typing import List

from daos.manager_dao import ManagerDAO
from entities.reimbursement import Reimbursement
from services.manager_service import ManagerService


class ManagerServiceImpl(ManagerService):

    def __init__(self, manager_dao: ManagerDAO):
        self.manager_dao = manager_dao

    def retrieve_all_managers(self):
        return self.manager_dao.get_all_managers()

    def approve_deny_requests(self, manager_id: int, employee_id: int, request_id: int, status: str, message: str) \
            -> Reimbursement:
        return self.manager_dao.approve_deny_requests(manager_id, employee_id, request_id, status, message)

    def retrieve_all_requests(self, manager_id: int) -> List[Reimbursement]:
        return self.manager_dao.view_requests(manager_id)

    def retrieve_all_past_requests(self, manager_id: int) -> List[Reimbursement]:
        return self.manager_dao.view_past_requests(manager_id)

    def retrieve_all_pending_requests(self, manager_id: int) -> List[Reimbursement]:
        return self.manager_dao.view_pending_requests(manager_id)

    def view_statistics_for_manager(self, manager_id: int):
        return self.manager_dao.view_statistics_for_manager(manager_id)

    def view_all_statistics(self):
        return self.manager_dao.view_all_statistics()
