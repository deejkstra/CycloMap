#!/usr/bin/python3

def func_string():
    return "some data"

def func_bool():
    return True

def example_one():
    if func_bool():
        return
    return func_string()

def example_two():
    i = 1
    j = 0
    while i > j:
        j += 1
        i += 1
    return func_string()

def example_three():
    data = example_one()
    return data + " woohoo"
