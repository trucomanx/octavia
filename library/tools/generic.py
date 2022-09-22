#!/usr/bin/python

import os

def command_open_program(program):
    os.system( program)

def text_exist_in_double_list(texto,list_of_list):
    for n in range(len(list_of_list)):
        if texto in list_of_list[n]:
            return n;
    return -1;
