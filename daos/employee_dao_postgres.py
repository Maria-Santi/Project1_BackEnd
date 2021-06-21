from typing import List

from daos.employee_dao import EmployeeDAO
from entities.employee import Employee
from entities.reimbursement import Reimbursement
from exceptions.not_found_exception import ResourceNotFoundError
from utils.connection_util import connection


class EmployeeDAOPostgres(EmployeeDAO):
    def get_all_employees(self):
        sql = """select * from employee"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        employees = [Employee(*record) for record in records]
        return employees

    def get_past_requests(self, employee_id: int) -> List[Reimbursement]:
        sql = """select * from request where employee_id = %s and (status = 'Approved' or status = 'Denied')"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        records = cursor.fetchall()
        if not records:
            raise ResourceNotFoundError(f"Employee {employee_id} has no past requests")
        else:
            requests = [Reimbursement(*record) for record in records]
            return requests

    def get_pending_requests(self, employee_id: int) -> List[Reimbursement]:
        sql = """select * from request where employee_id = %s 
                and status = 'Pending'"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        records = cursor.fetchall()
        if not records:
            raise ResourceNotFoundError(f"Employee {employee_id} has no pending requests")
        else:
            requests = [Reimbursement(*record) for record in records]
            return requests

    def get_all_requests(self, employee_id: int) -> List[Reimbursement]:
        sql = """select * from request where employee_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        records = cursor.fetchall()
        if not records:
            raise ResourceNotFoundError(f"Employee {employee_id} has no requests")
        else:
            requests = [Reimbursement(*record) for record in records]
            return requests
