import pytest

from daos.employee_dao import EmployeeDAO
from daos.employee_dao_postgres import EmployeeDAOPostgres
from exceptions.not_found_exception import ResourceNotFoundError

employee_dao: EmployeeDAO = EmployeeDAOPostgres()


def test_get_past_requests():
    past_requests = employee_dao.get_past_requests(1)
    assert len(past_requests) >= 1


def test_get_past_requests_exception():
    with pytest.raises(ResourceNotFoundError):
        employee_dao.get_past_requests(70)


def test_get_pending_requests():
    pending_requests = employee_dao.get_pending_requests(1)
    assert len(pending_requests) >= 1


def test_get_pending_requests_exception():
    with pytest.raises(ResourceNotFoundError):
        employee_dao.get_pending_requests(70)


def test_get_all_requests():
    requests = employee_dao.get_all_requests(1)
    assert len(requests) >= 1


def test_get_all_requests_exception():
    with pytest.raises(ResourceNotFoundError):
        employee_dao.get_all_requests(70)


def test_get_all_employees():
    emps = employee_dao.get_all_employees()
    assert len(emps) >= 1
