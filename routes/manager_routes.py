#import json
import simplejson as json

from flask import Flask, request, jsonify

from daos.employee_dao_postgres import EmployeeDAOPostgres
from daos.manager_dao_postgres import ManagerDAOPostgres
from exceptions.not_found_exception import ResourceNotFoundError
from services.manager_service_impl import ManagerServiceImpl

manager_dao = ManagerDAOPostgres()
employee_dao = EmployeeDAOPostgres()
manager_service = ManagerServiceImpl(manager_dao)


def create_routes(app: Flask):

    @app.route("/managers", methods=["GET"])
    def get_all_managers():
        managers = manager_service.retrieve_all_managers()
        json_managers = [m.as_json_dict() for m in managers]
        return jsonify(json_managers)

    @app.route("/managers/<manager_id>/employees/<employee_id>/requests/<request_id>", methods=["PATCH"])
    def approve_deny_requests(manager_id: str, employee_id: str, request_id: str):
        try:
            body = request.json
            if "status" in body:
                status = body["status"]
                message = body["requestMessage"]
                manager_service.approve_deny_requests(int(manager_id), int(employee_id), int(request_id), status, message)
                return f"Request status has changed to {status}", 200
        except ResourceNotFoundError as e:
            return e.as_json_dict(), 404

    @app.route("/managers/<manager_id>/requests", methods=["GET"])
    def get_all_requests_for_manager(manager_id: str):
        try:
            r_status = request.args.get("status")
            requests = []
            if r_status is not None:
                if r_status == "Past":
                    requests += manager_service.retrieve_all_past_requests(int(manager_id))
                if r_status == "Pending":
                    requests += manager_service.retrieve_all_pending_requests(int(manager_id))
            else:
                requests += manager_service.retrieve_all_requests(int(manager_id))
            json_requests = [r.as_json_dict() for r in requests]
            return jsonify(json_requests), 200
        except ResourceNotFoundError as e:
            return e.as_json_dict(), 404

    @app.route("/managers/<manager_id>/statistics", methods=["GET"])
    def view_statistics_manager(manager_id: int):
        try:
            stats = manager_service.view_statistics_for_manager(manager_id)
            json_stats = json.dumps(stats, indent=4)
            return json_stats
        except ResourceNotFoundError as e:
            return e.as_json_dict(), 404

    @app.route("/statistics")
    def view_all_statistics():
        stats = manager_service.view_all_statistics()
        json_stats = json.dumps(stats, indent=4)
        return json_stats


