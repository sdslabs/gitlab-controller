#!/usr/bin/python

import sys
import base


if(len(sys.argv) < 2):
    print """Available commands are:
    addkey <username> <key>
    removekey <username>
    changekey <username> <key>
    adduser <email> <username> <password> <Full Name>
    removeuser <username>
    Note: key and fullname may contain spaces so they have to be kept in quotes"""
    sys.exit()

first = sys.argv[1]
con = base.Controller()
print first
if (first == 'addkey'):
    if(len(sys.argv) != 4):
        print "Incorrect number of parameters"
        sys.exit(1)
    user = sys.argv[2]
    key = sys.argv[3]
    print "Adding key for " + user

    print con.addsshkey(user, key)
    sys.exit()

elif (first == 'removekey'):
    if(len(sys.argv) != 3):
        print "Incorrect number of parameters"
        sys.exit(1)

    user = sys.argv[2]
    print "Removing key for " + user

    print con.deleteallkeys(user)
    sys.exit()

elif (first == 'changekey'):
    if(len(sys.argv) != 4):
        print "Incorrect number of parameters"
        sys.exit(1)
    user = sys.argv[2]
    key = sys.argv[3]
    print "Changing key for " + user

    print con.modifykeys(user, key)
    sys.exit()
elif (first == 'adduser'):
    if(len(sys.argv) != 6):
        print "Incorrect number of parameters"
        sys.exit(1)
    email = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
    name = sys.argv[5]
    print "Creating user " + username

    print con.adduser(email,password, username,name)
    sys.exit()

elif (first == 'removeuser'):
    if(len(sys.argv) != 3):
        print "Incorrect number of parameters"
        sys.exit(1)
    username = sys.argv[2]
    print "Removing user " + username

    print con.removeuser(username)
    sys.exit()
