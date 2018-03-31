# coding=utf-8
import re


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = raw_input('Enter text:')
something = something.lower()
somethings = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：]+".decode("utf8"),
       "".decode("utf8"), something.decode("utf8"))
if is_palindrome(somethings):
    print('Yes, it is a palindrome')
else:
    print('No, it is not a palindrome')
