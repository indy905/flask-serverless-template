import json
import os
import unittest
from unittest.mock import patch

# These are fake credentials used only by Moto; no live AWS calls are made.
os.environ.update(AWS_ACCESS_KEY_ID='testing', AWS_SECRET_ACCESS_KEY='testing',
                  AWS_DEFAULT_REGION='ap-northeast-2', AWS_EC2_METADATA_DISABLED='true')

from moto import mock_aws

from application import create_app
from application.models.dao.users.user_model import UserModel
from application.models.types.role_type import RoleType


class CompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.aws = mock_aws()
        self.aws.start()
        self.addCleanup(self.aws.stop)
        UserModel._connection = None
        UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
        self.app = create_app('prod')
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_user_lifecycle(self):
        user = {'id': 'tester', 'name': '한글 사용자', 'role': 'READ'}
        created = self.client.post('/user', json=user)
        self.assertEqual(created.status_code, 200, created.get_data(as_text=True))
        self.assertEqual(json.loads(created.data)['name'], user['name'])
        fetched = self.client.get('/user/tester')
        self.assertEqual(fetched.status_code, 200)
        self.assertEqual(json.loads(fetched.data)['role'], 'READ')
        self.assertEqual(UserModel.get('tester').role, RoleType.READ)
        self.assertEqual(self.client.delete('/user/tester').status_code, 200)
        self.assertEqual(self.client.get('/user/tester').status_code, 404)

    def test_duplicate_and_missing_user(self):
        user = {'id': 'tester', 'name': '사용자', 'role': 'ADMIN'}
        self.assertEqual(self.client.post('/user', json=user).status_code, 200)
        self.assertEqual(self.client.post('/user', json=user).status_code, 403)
        self.assertEqual(self.client.delete('/user/missing').status_code, 404)

    def test_validation(self):
        for user in ({}, {'id': 'x', 'name': '사용자', 'role': 'READ'},
                     {'id': 'valid', 'name': '사용자', 'role': 'INVALID'}):
            with self.subTest(user=user):
                self.assertEqual(self.client.post('/user', json=user).status_code, 400)

    def test_cors_preflight_and_response(self):
        origin = 'https://example.com'
        response = self.client.options('/user', headers={
            'Origin': origin, 'Access-Control-Request-Method': 'POST',
            'Access-Control-Request-Headers': 'Content-Type'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Access-Control-Allow-Origin'], origin)
        self.assertIn('POST', response.headers['Access-Control-Allow-Methods'])
        self.assertIn('Content-Type', response.headers['Access-Control-Allow-Headers'])
        response = self.client.get('/user/missing', headers={'Origin': origin})
        self.assertEqual(response.headers['Access-Control-Allow-Origin'], origin)

    def test_json_unicode(self):
        with patch('application.controllers.user_controller.user_service.get_user',
                   side_effect=RuntimeError('한글 오류')):
            response = self.client.get('/user/tester')
        self.assertEqual(response.status_code, 500)
        self.assertIn('한글 오류', response.get_data(as_text=True))
        self.assertEqual(response.json['message'], '한글 오류')

    def test_model_iteration(self):
        model = UserModel(id='tester', name='사용자', role=RoleType.WRITE)
        self.assertEqual(dict(model)['role'], 'WRITE')


if __name__ == '__main__':
    unittest.main()
