# write your code here
import re
import sys

sys.setrecursionlimit(10000)


def check_one_char(regex, char, literal=False):
    if not literal:
        return (regex == char) or (regex == '.') or (regex == '')
    return regex == char


def check_one_by_one(regex, text):
    # base case 1: regex is consumed
    if len(regex) == 0:
        return True
    elif regex == '$' and len(text) == 0:
        return True
    # base case 2: remains regex while no text
    elif len(text) == 0:
        return False

    # reductive step
    if regex.startswith('\\'):
        if regex[1] in '.?+*\\':
            return check_one_char(regex[1], text[:1], literal=True) and check_one_by_one(regex[2:], text[1:])
    else:
        return check_one_char(regex[:1], text[:1]) and check_one_by_one(regex[1:], text[1:])


def check_regex_plain(regex, text):
    if regex.startswith('^'):
        return check_one_by_one(regex[1:], text)

    if len(regex.replace('$', '').replace('\\', '')) > len(text):
        # base case: regex is longer than text
        return False
    else:
        return check_one_by_one(regex, text) or check_regex_plain(regex, text[1:])


def check_regex_with_question_mark(regex, text):
    # 2 possible scenarios
    regex1, regex2 = regex.split('?')
    # 1) exclude preceding character
    regex_exclude = regex1[:-1] + regex2
    # 2) include preceding character
    regex_include = regex1 + regex2

    return check_regex_plain(regex_exclude, text) or check_regex_plain(regex_include, text)


def check_regex_with_star_sign(regex, text):
    # base case: not long enough text
    if len(regex) > len(text) + 3:    # possible 3 extra characters => $,^,(*,+?)
        return False
    regex1, regex2 = regex.split('*')
    regex_question_mark = regex1 + '?' + regex2
    regex_check_more = regex1 + regex1[-1] + '*' + regex2
    return check_regex_with_star_sign(regex_check_more, text) or check_regex_with_question_mark(regex_question_mark, text)


def check_regex_with_plus_sign(regex, text):
    regex1, regex2 = regex.split('+')
    regex_star = regex1 + regex1[-1] + '*' + regex2
    return check_regex_with_star_sign(regex_star, text)


def match(regex, text):
    if '?' in regex and ('\\?' not in regex):
        return check_regex_with_question_mark(regex, text)
    elif '+' in regex and ('\\+' not in regex):
        return check_regex_with_plus_sign(regex, text)
    elif '*' in regex and ('\\*' not in regex):
        return check_regex_with_star_sign(regex, text)
    return check_regex_plain(regex, text)


def main():
    text_input = input()
    regex, text = text_input.split("|")
    print(match(regex, text))


if __name__ == '__main__':
    main()
