import unittest
import yaml
import re
from unittest.mock import mock_open, patch


class TestYamlParsing(unittest.TestCase):

    def test_yaml_parsing(self):
        with patch("builtins.open", mock_open(read_data="name: Project X\nteams:\n  - name: Team A\n    members:\n      - mail: test1@bmw.de\n        role: Developer\n      - mail: test2@bmw.com\n        role: Manager\n  - name: Team B\n    members:\n      - mail: test3@bmw.de\n        role: Tester\n        ")):
            
            try:
                with open("project.yaml", 'r') as f:
                    valuesYaml = yaml.load(f, Loader=yaml.FullLoader)
            except FileNotFoundError:
                self.fail("YAML file not found")
            
            self.assertEqual(valuesYaml['name'], 'Project X')
            self.assertEqual(len(valuesYaml['teams']), 2)

    def test_email_validation(self):
        email1 = "test1@bmw.de"
        email2 = "test2@bmw.com"
        email3 = "test3@bmw.de"
        email4 = "test4@gmail.com"
        
        self.assertTrue(re.search("@bm(w|w|w).de$", email1))
        self.assertFalse(re.search("@bm(w|w|w).de$", email2))
        self.assertTrue(re.search("@bm(w|w|w).de$", email3))
        self.assertFalse(re.search("@bm(w|w|w).de$", email4))

if __name__ == '__main__':
    unittest.main()

