from fabric.api import *
'''
OPS435 Assignment 2S - Winter 2021
Program: a2r_khuang31.py
Author: Kaixi Huang
The python code in this file a2s_khuang31.py is original work written by
Kaixi Huang. No code in this file is copied from any other source 
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and violators 
will be reported and appropriate action will be taken.
'''

env.user = "student"

def addUser(name):
    '''add a user with given user name to remote system'''
    command = 'useradd ' + name
    status = sudo(command)
    print(status)
 
def listUser():
    '''return a list of shell user on a remote system'''
    cmd = 'awk -F: \'/bash$/{print $1}\' /etc/passwd'
    status = run(cmd)
    status_user = []
    for each_name in status:
        status_user.append(each_name)
    string_user = ''.join(status_user)
    list = string_user.split()
    print(list)


def listSysUser():
    '''return a list of system (non-shell) user'''
    cmd = 'awk -F: \'$7 !~ /bash$/{print $1}\' /etc/passwd'
    status = run(cmd)
    status_user = []
    for each_name in status:
        status_user.append(each_name)
    string_user = ''.join(status_user)
    list = string_user.split()
    print(list)

def findUser(name):
    '''find user with a given user name'''
    command = 'getent passwd ' + name +' | cut -d: -f1'
    status = run(command)
    if status == name:
        print('The given user name '+ name + ' found on the system.')
    else:
        print('The given user name ' + name + '  not found on the system.')
