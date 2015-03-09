#!/usr/bin/python2

import sys
import base


if(len(sys.argv) < 2):
    print """Available commands are:
    addkey <username> <key>
    removekey <username>
    changekey <username> <key>
    adduser <email> <username> <password> <Full Name>
    removeuser <username>
    isadmin <username>
    isgroupmember <groupname> <username>
    Note: key and fullname may contain spaces so they have to be kept in quotes"""
    sys.exit()

first = sys.argv[1]
con = base.Controller()
if (first == 'addkey'):
    if(len(sys.argv) != 4):
        print "Incorrect number of parameters"
        sys.exit(1)
    user = sys.argv[2]
    key = sys.argv[3]
    print "Adding key for " + user

    r = con.addsshkey(user, key)
    if (r):
        print r
    else:
        print 'Failed to add key'
    sys.exit()

elif (first == 'removekey'):
    if(len(sys.argv) != 3):
        print "Incorrect number of parameters"
        sys.exit(1)

    user = sys.argv[2]
    print "Removing key for " + user

    r = con.deleteallkeys(user)
    if(r):
        print r
    else:
        print "Failed to remove keys"
    sys.exit()

elif (first == 'changekey'):
    if(len(sys.argv) != 4):
        print "Incorrect number of parameters"
        sys.exit(1)
    user = sys.argv[2]
    key = sys.argv[3]
    print "Changing key for " + user

    r = con.modifykeys(user, key)
    if(r):
        print r
    else:
        print "Failed to remove keys"

    sys.exit()

elif (first == 'isadmin'):
    if(len(sys.argv) != 3):
        print "Incorrect number of parameters"
        sys.exit(1)
    user = sys.argv[2]
    if(con.isadmin(user)):
        sys.stdout.write('yes')
    else:
        sys.stdout.write('no')
    sys.exit()

elif (first == 'isgroupmember'):
    if(len(sys.argv) != 4):
        print "Incorrect number of parameters"
        sys.exit(1)
    group = sys.argv[2]
    username = sys.argv[3]

    r = con.isgroupmember(group, username)
    if(r):
        sys.stdout.write('yes')
    else:
        sys.stdout.write('no')

elif (first == 'adduser'):
    if(len(sys.argv) != 6):
        print "Incorrect number of parameters"
        sys.exit(1)
    email = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]
    name = sys.argv[5]
    print "Creating user " + username

    r = con.adduser(email,password, username,name)
    if(r):
        print r
    else:
        print "Failed to add user"
    sys.exit()

elif (first == 'removeuser'):
    if(len(sys.argv) != 3):
        print "Incorrect number of parameters"
        sys.exit(1)
    username = sys.argv[2]
    print "Removing user " + username

    r = con.removeuser(username)
    if(r):
        print r
    else:
        print "Failed to remove user"
    sys.exit()
