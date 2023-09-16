import unittest

from story_request.context_mappings import get_basic_context_for_monster


class TestGetBasicContext(unittest.TestCase):

    def test_unknown_monster(self):
        context = get_basic_context_for_monster(monster_id="notvalid")
        expected = "Write a story of about a generic female hero that saves animals. " \
                   "It is very important to use maximum 50 words!"
        self.assertEqual(expected, context)
