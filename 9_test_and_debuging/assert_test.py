from unittest import TestCase


class AssertTestCase(TestCase):
    def test_assert_helper(self):
        expected = 12
        found = 2* 5
        self.assertEqual(expected, found)

    def test_assert_statement(self):
        expected = 12
        found = 2* 5
        assert expected == found
