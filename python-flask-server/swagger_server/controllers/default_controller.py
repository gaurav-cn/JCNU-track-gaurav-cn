import connexion
import six

from swagger_server.models.assign_project import AssignProject  # noqa: E501
from swagger_server.models.name import Name  # noqa: E501
from swagger_server import util


def assign_mentor(project_id, user_id):  # noqa: E501
    """assign_mentor

     # noqa: E501

    :param project_id: ID of project
    :type project_id: int
    :param user_id: ID of mentor
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def assign_project(Data=None):  # noqa: E501
    """assign_project

    Assign project to a user # noqa: E501

    :param Data: Project Id
    :type Data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Data = AssignProject.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_mentees(user_id):  # noqa: E501
    """get_mentees

    Get the list of IDs of the users being mentored by the queried user. # noqa: E501

    :param user_id: ID of the user
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_mentoring_projects(user_id):  # noqa: E501
    """get_mentoring_projects

    Get the list of IDs of the projects being mentored by the queried user. # noqa: E501

    :param user_id: ID of the user
    :type user_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_users_and_mentors(project_id):  # noqa: E501
    """get_users_and_mentors

    Get the list of IDs of the mentors and users of the project # noqa: E501

    :param project_id: ID of the project
    :type project_id: int

    :rtype: None
    """
    return 'do some magic!'


def project_create(name=None):  # noqa: E501
    """project_create

    Create a project # noqa: E501

    :param name: Name of project
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = Name.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def user_create(name=None):  # noqa: E501
    """user_create

    Create a new user # noqa: E501

    :param name: The name of the person
    :type name: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        name = Name.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
