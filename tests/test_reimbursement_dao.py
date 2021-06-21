import pytest

from daos.reimbursement_dao import ReimbursementDAO
from daos.reimbursement_dao_postgres import ReimbursementDAOPostgres
from entities.reimbursement import Reimbursement
from exceptions.not_found_exception import ResourceNotFoundError

request_dao: ReimbursementDAO = ReimbursementDAOPostgres()
test_request = Reimbursement(0, 1, 1, 200, "Potion Poisoning", "", "")


def test_create_request():
    request_dao.create_request(1, 1, test_request)
    assert test_request.request_id != 0


def test_get_request_by_id():
    r_request = request_dao.get_request_by_id(test_request.request_id)
    assert test_request.request_id == r_request.request_id


def test_get_request_by_id_exception():
    with pytest.raises(ResourceNotFoundError):
        request_dao.get_request_by_id(70)
