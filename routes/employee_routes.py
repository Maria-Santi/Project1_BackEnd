from flask import Flask, request, jsonify

from daos.employee_dao_postgres import EmployeeDAOPostgres
from entities.reimbursement import Reimbursement
from exceptions.not_found_exception import ResourceNotFoundError
from services.employee_service_impl import EmployeeServiceImpl

employee_dao = EmployeeDAOPostgres()
employee_service = EmployeeServiceImpl(employee_dao)


def create_routes(app: Flask):
    @app.route("/employees", methods=["GET"])
    def get_all_employees():
        employees = employee_service.retrieve_all_employees()
        json_emps = [e.as_json_dict() for e in employees]
        return jsonify(json_emps)

    @app.route("/employees/<employee_id>/requests", methods=["GET"])
    def get_all_employee_requests(employee_id: str):
        try:
            r_status = request.args.get("status")
            requests = []
            if r_status is not None:
                if r_status == "Past":
                    requests += employee_service.retrieve_all_past_requests(int(employee_id))
                if r_status == "Pending":
                    requests += employee_service.retrieve_all_pending_requests(int(employee_id))
            else:
                requests += employee_service.retrieve_all_requests(int(employee_id))
            json_requests = [r.as_json_dict() for r in requests]
            return jsonify(json_requests), 200
        except ResourceNotFoundError as e:
            return e.as_json_dict(), 404
