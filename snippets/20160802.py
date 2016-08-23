import re

def parse_with_regex(text, pattern):
    m = re.findall(pattern, text)
    print m
    print m.groups()

parse_with_regex("hello banana bye hello pineapple bye", r"hello (.*?) bye")
parse_with_regex("hello banana bye", r"nomatch")
