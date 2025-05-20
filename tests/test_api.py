import unittest
from app import create_app

class TodoAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_get_todos(self):
        response = self.app.get('/todos')
        self.assertEqual(response.status_code, 200)

    def test_add_todo(self):
        response = self.app.post('/todos', json={'task': 'Study DevOps'})
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
