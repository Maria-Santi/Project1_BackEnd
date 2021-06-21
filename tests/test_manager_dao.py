import pytest

from daos.manager_dao import ManagerDAO
from daos.manager_dao_postgres import ManagerDAOPostgres
from exceptions.not_found_exception import ResourceNotFoundError

manager_dao: ManagerDAO = ManagerDAOPostgres()


def test_approve_deny_requests():
    r_status = "Denied"
    r_message = "Needed a new Wand"
    request_update = manager_dao.approve_deny_requests(1, 1, 1, r_status, r_message)
    assert r_status == request_update.request_status


def test_approve_deny_requests_exception():
    with pytest.raises(ResourceNotFoundError):
        manager_dao.approve_deny_requests(1, 1, 100, "", "")


def test_view_requests():
    requests = manager_dao.view_requests(1)
    assert len(requests) >= 1


def test_view_requests_exception():
    with pytest.raises(ResourceNotFoundError):
        manager_dao.view_requests(70)


def test_view_past_requests():
    past_requests = manager_dao.view_past_requests(1)
    assert len(past_requests) >= 1


def test_view_past_requests_exception():
    with pytest.raises(ResourceNotFoundError):
        manager_dao.view_past_requests(70)


def test_view_pending_requests():
    pending_requests = manager_dao.view_pending_requests(1)
    assert len(pending_requests) >= 1


def test_view_pending_requests_exception():
    with pytest.raises(ResourceNotFoundError):
        manager_dao.view_pending_requests(70)


def test_view_statistics_for_manager():
    stats = manager_dao.view_statistics_for_manager(1)
    assert type(stats) is list


def test_view_all_statistics():
    stats = manager_dao.view_all_statistics()
    assert type(stats) is list