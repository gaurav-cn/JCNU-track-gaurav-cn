# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.assign_project import AssignProject  # noqa: E501
from swagger_server.models.name import Name  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_assign_mentor(self):
        """Test case for assign_mentor

        
        """
        response = self.client.open(
            '/myapp1/project/{project_id}/assignMentor/{user_id}/'.format(project_id=56, user_id=56),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_assign_project(self):
        """Test case for assign_project

        
        """
        Data = AssignProject()
        response = self.client.open(
            '/myapp1/user/assignProject/',
            method='POST',
            data=json.dumps(Data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mentees(self):
        """Test case for get_mentees

        
        """
        response = self.client.open(
            '/myapp1/user/{user_id}/mentees/'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_mentoring_projects(self):
        """Test case for get_mentoring_projects

        
        """
        response = self.client.open(
            '/myapp1/user/{user_id}/mentoring/'.format(user_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users_and_mentors(self):
        """Test case for get_users_and_mentors

        
        """
        response = self.client.open(
            '/myapp1/project/{project_id}/'.format(project_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_project_create(self):
        """Test case for project_create

        
        """
        name = Name()
        response = self.client.open(
            '/myapp1/project/create/',
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_create(self):
        """Test case for user_create

        
        """
        name = Name()
        response = self.client.open(
            '/myapp1/user/create/',
            method='POST',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
