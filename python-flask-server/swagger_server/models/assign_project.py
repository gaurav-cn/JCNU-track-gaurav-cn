# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AssignProject(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, project_id: int=None, users: List[int]=None):  # noqa: E501
        """AssignProject - a model defined in Swagger

        :param project_id: The project_id of this AssignProject.  # noqa: E501
        :type project_id: int
        :param users: The users of this AssignProject.  # noqa: E501
        :type users: List[int]
        """
        self.swagger_types = {
            'project_id': int,
            'users': List[int]
        }

        self.attribute_map = {
            'project_id': 'project_id',
            'users': 'users'
        }

        self._project_id = project_id
        self._users = users

    @classmethod
    def from_dict(cls, dikt) -> 'AssignProject':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The assignProject of this AssignProject.  # noqa: E501
        :rtype: AssignProject
        """
        return util.deserialize_model(dikt, cls)

    @property
    def project_id(self) -> int:
        """Gets the project_id of this AssignProject.

        ID  # noqa: E501

        :return: The project_id of this AssignProject.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id: int):
        """Sets the project_id of this AssignProject.

        ID  # noqa: E501

        :param project_id: The project_id of this AssignProject.
        :type project_id: int
        """

        self._project_id = project_id

    @property
    def users(self) -> List[int]:
        """Gets the users of this AssignProject.


        :return: The users of this AssignProject.
        :rtype: List[int]
        """
        return self._users

    @users.setter
    def users(self, users: List[int]):
        """Sets the users of this AssignProject.


        :param users: The users of this AssignProject.
        :type users: List[int]
        """

        self._users = users
