from typing import List

from daos.reimbursement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from services.reimbursement_service import ReimbursementService


class ReimbursementServiceImpl(ReimbursementService):

    def __init__(self, request_dao: ReimbursementDAO):
        self.request_dao = request_dao

    def add_request(self, employee_id: int, manager_id: int, request: Reimbursement) -> Reimbursement:
        return self.request_dao.create_request(employee_id, manager_id, request)

    def retrieve_request_by_id(self, request_id: int) -> Reimbursement:
        return self.request_dao.get_request_by_id(request_id)
