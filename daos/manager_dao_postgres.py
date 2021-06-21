from typing import List

from daos.manager_dao import ManagerDAO
from daos.reimbursement_dao import ReimbursementDAO
from daos.reimbursement_dao_postgres import ReimbursementDAOPostgres
from entities.manager import Manager
from entities.reimbursement import Reimbursement
from exceptions.not_found_exception import ResourceNotFoundError
from utils.connection_util import connection

request_dao: ReimbursementDAO = ReimbursementDAOPostgres()


class ManagerDAOPostgres(ManagerDAO):

    def approve_deny_requests(self, manager_id: int, employee_id: int, request_id: int, status: str, message: str) \
            -> Reimbursement:
        r_request = request_dao.get_request_by_id(request_id)
        sql = """update request set status = %s, request_message = %s where employee_id = %s and manager_id = %s 
                and request_id = %s returning request_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (status, message, employee_id, manager_id, request_id))
        connection.commit()
        r_id = cursor.fetchone()
        if r_id is not None:
            return r_request
        else:
            raise ResourceNotFoundError(f"Request could not be found")

    def view_requests(self, manager_id: int) -> List[Reimbursement]:
        sql = """select * from request where manager_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        records = cursor.fetchall()
        if not records:
            raise ResourceNotFoundError(f"Manager {manager_id} has no requests from employees")
        else:
            requests = [Reimbursement(*record) for record in records]
            return requests

    def view_past_requests(self, manager_id: int) -> List[Reimbursement]:
        sql = """select * from request where manager_id = %s 
                and (status = 'Approved' or status = 'Denied')"""
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        records = cursor.fetchall()
        if not records:
            raise ResourceNotFoundError(f"Manager {manager_id} has no past requests")
        else:
            requests = [Reimbursement(*record) for record in records]
            return requests

    def view_pending_requests(self, manager_id: int) -> List[Reimbursement]:
        sql = """select * from request where manager_id = %s and status = 'Pending'"""
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        records = cursor.fetchall()
        if not records:
            raise ResourceNotFoundError(f"Manager {manager_id} has no pending requests")
        else:
            requests = [Reimbursement(*record) for record in records]
            return requests

    def get_all_managers(self):
        sql = """select * from manager"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        managers = [Manager(*record) for record in records]
        return managers

    def view_statistics_for_manager(self, manager_id: int):
        sql = """select employee_id as employeeID, employee.emp_name as employeeName, count(request_id), sum(amount),
            round(avg(amount)) as avg, max(amount), min(amount) from request inner join employee using(employee_id)
            where request.manager_id = %s group by employee.emp_name, employee_id order by sum desc; """
        cursor = connection.cursor()
        cursor.execute(sql, [manager_id])
        records = cursor.fetchall()
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in records]
        if data[0]["count"] == 0:
            raise ResourceNotFoundError(f"Manager has no requests")
        else:
            return data

    def view_all_statistics(self):
        sql = """select employee_id as employeeID, employee.emp_name as employeeName, count(request_id), sum(amount),
            round(avg(amount)) as avg, max(amount), min(amount) from request inner join employee using(employee_id)
            group by employee.emp_name, employee_id order by sum desc"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        desc = cursor.description
        column_names = [col[0] for col in desc]
        data = [dict(zip(column_names, row)) for row in records]
        return data
