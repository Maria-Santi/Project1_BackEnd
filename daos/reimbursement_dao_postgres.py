from typing import List

from daos.reimbursement_dao import ReimbursementDAO
from entities.reimbursement import Reimbursement
from exceptions.not_found_exception import ResourceNotFoundError
from utils.connection_util import connection


class ReimbursementDAOPostgres(ReimbursementDAO):
    def create_request(self, employee_id: int, manager_id: int, request: Reimbursement) -> Reimbursement:
        request.status = "Pending"
        sql = """insert into request values (default, %s, %s, %s, %s, %s, %s) returning request_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (employee_id, manager_id, request.amount, request.reason, request.status,
                             request.request_message))
        connection.commit()
        r_id = cursor.fetchone()[0]
        request.request_id = r_id
        return request

    def get_request_by_id(self, request_id) -> Reimbursement:
        sql = """select * from request where request_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [request_id])
        record = cursor.fetchone()
        if record is not None:
            request = Reimbursement(*record)
            return request
        else:
            raise ResourceNotFoundError(f"Request {request_id} could not be found")


