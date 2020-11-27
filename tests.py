import unittest
import regex


class RegexEngineTest(unittest.TestCase):

    def test_check_one_char(self):

        self.assertEqual(regex.check_one_char('a', 'a'), True)
        self.assertEqual(regex.check_one_char('.', 'a'), True)
        self.assertEqual(regex.check_one_char('', 'a'), True)
        self.assertEqual(regex.check_one_char('', ''), True)
        self.assertEqual(regex.check_one_char('a', ''), False)
        self.assertEqual(regex.check_one_char('a', 'b'), False)
        self.assertEqual(regex.check_one_char('7', '7'), True)
        self.assertEqual(regex.check_one_char('6', '7'), False)
        self.assertEqual(regex.check_one_char('a', '.'), False)

    def test_check_one_by_one(self):
        # test 1-character input
        self.assertEqual(regex.check_one_by_one('a', 'a'), True)
        self.assertEqual(regex.check_one_by_one('.', 'a'), True)
        self.assertEqual(regex.check_one_by_one('', 'a'), True)
        self.assertEqual(regex.check_one_by_one('', ''), True)
        self.assertEqual(regex.check_one_by_one('a', ''), False)
        self.assertEqual(regex.check_one_by_one('a', 'b'), False)
        self.assertEqual(regex.check_one_by_one('7', '7'), True)
        self.assertEqual(regex.check_one_by_one('6', '7'), False)
        self.assertEqual(regex.check_one_by_one('a', '.'), False)

        # test >1-character input
        self.assertEqual(regex.check_one_by_one('apple', 'apple'), True)
        self.assertEqual(regex.check_one_by_one('.pple', 'apple'), True)
        self.assertEqual(regex.check_one_by_one('appl.', 'apple'), True)
        self.assertEqual(regex.check_one_by_one('.....', 'apple'), True)
        self.assertEqual(regex.check_one_by_one('', 'apple'), True)
        self.assertEqual(regex.check_one_by_one('apple', ''), False)
        self.assertEqual(regex.check_one_by_one('apple', 'peach'), False)

    def test_check_full_string(self):
        # test 1-character input
        self.assertEqual(regex.check_regex_plain('a', 'a'), True)
        self.assertEqual(regex.check_regex_plain('.', 'a'), True)
        self.assertEqual(regex.check_regex_plain('', 'a'), True)
        self.assertEqual(regex.check_regex_plain('', ''), True)
        self.assertEqual(regex.check_regex_plain('a', ''), False)
        self.assertEqual(regex.check_regex_plain('a', 'b'), False)
        self.assertEqual(regex.check_regex_plain('7', '7'), True)
        self.assertEqual(regex.check_regex_plain('6', '7'), False)
        self.assertEqual(regex.check_regex_plain('a', '.'), False)

        # test >1-character input
        self.assertEqual(regex.check_regex_plain('apple', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('.pple', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('appl.', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('.....', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('apple', ''), False)
        self.assertEqual(regex.check_regex_plain('apple', 'peach'), False)

        # stage-3
        self.assertEqual(regex.check_regex_plain('le', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('app', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('a', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('.', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('apwle', 'apple'), False)
        self.assertEqual(regex.check_regex_plain('peach', 'apple'), False)

    def test_check_full_string_start_end_match(self):
        self.assertEqual(regex.check_regex_plain('^app', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('le$', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('^a', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('.$', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('apple$', 'tasty apple'), True)
        self.assertEqual(regex.check_regex_plain('^apple', 'apple pie'), True)
        self.assertEqual(regex.check_regex_plain('^apple$', 'apple'), True)
        self.assertEqual(regex.check_regex_plain('^apple$', 'tasty apple'), False)
        self.assertEqual(regex.check_regex_plain('^apple$', 'apple pie'), False)
        self.assertEqual(regex.check_regex_plain('app$', 'apple'), False)
        self.assertEqual(regex.check_regex_plain('^le', 'apple'), False)
        self.assertEqual(regex.check_regex_plain('^no', 'noooooooope'), True)
        self.assertEqual(regex.check_regex_plain('^noo', 'noooooooope'), True)

    def test_check_str_with_question_mark(self):
        self.assertEqual(regex.check_regex_with_question_mark('colou?r', 'color'), True)
        self.assertEqual(regex.check_regex_with_question_mark('colou?r', 'colour'), True)
        self.assertEqual(regex.check_regex_with_question_mark('colur?r', 'colouur'), False)
        self.assertEqual(regex.check_regex_with_question_mark('.?', 'aaa'), True)

    def test_check_regex_with_star_sign(self):
        self.assertEqual(regex.check_regex_with_star_sign('colou*r', 'color'), True)
        self.assertEqual(regex.check_regex_with_star_sign('colou*r', 'colour'), True)
        self.assertEqual(regex.check_regex_with_star_sign('colou*r', 'colouur'), True)
        self.assertEqual(regex.check_regex_with_star_sign('.*', 'aaa'), True)
        self.assertEqual(regex.check_regex_with_star_sign('^noo*', 'nooooope'), True)

    def test_check_regex_with_plus_sign(self):
        self.assertEqual(regex.check_regex_with_plus_sign('colou+r', 'colour'), True)
        self.assertEqual(regex.check_regex_with_plus_sign('colou+r', 'color'), False)
        self.assertEqual(regex.check_regex_with_plus_sign('.+', 'aaa'), True)
        self.assertEqual(regex.check_regex_with_plus_sign('no+$', 'nooooooope'), False)
        self.assertEqual(regex.check_regex_with_plus_sign("^no+", 'noooooooope'), True)
        self.assertEqual(regex.check_regex_with_plus_sign("^no+pe$", "noooooooope"), True)
        self.assertEqual(regex.check_regex_with_plus_sign("^n.+pe$", 'noooooooope'), True)
        self.assertEqual(regex.check_regex_with_plus_sign("^n.+p$", 'noooooooope'), False)


if __name__ == '__main__':
    unittest.main()
