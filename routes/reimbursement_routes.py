from flask import Flask, request

from daos.reimbursement_dao_postgres import ReimbursementDAOPostgres
from entities.reimbursement import Reimbursement
from exceptions.not_found_exception import ResourceNotFoundError
from services.reimbursement_service_impl import ReimbursementServiceImpl

request_dao = ReimbursementDAOPostgres()
request_service = ReimbursementServiceImpl(request_dao)


def create_routes(app: Flask):
    @app.route("/managers/<manager_id>/employees/<employee_id>/requests", methods=["POST"])
    def create_request(manager_id: str, employee_id: str):
        try:
            body = request.json
            r_request = Reimbursement(body["requestID"], int(employee_id), int(manager_id), body["amount"],
                                      body["reason"], body["requestStatus"], body["requestMessage"])
            request_service.add_request(int(employee_id), r_request.manager_id, r_request)
            return f"Created request for employee {employee_id}", 201
        except ResourceNotFoundError as e:
            return e.as_json_dict(), 404

