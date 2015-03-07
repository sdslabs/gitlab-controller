#!/usr/bin/python
import conf
import requests

def get( url, load = {}):
    load['private_token'] = conf.token
    r = requests.get(conf.base_url + url, params = load)
    return r.json()

def post( url, load = {}):
    load['private_token'] = conf.token
    r = requests.post(conf.base_url + url, params = load)
    return r.json()

def delete( url, load = {}):
    load['private_token'] = conf.token
    r = requests.delete(conf.base_url + url, params = load)
    return r.json()




class Controller:
    """A class to run our custom commands"""

    def __init__(self, url = conf.base_url, token = conf.token):
        self.url = url
        self.token = token


    def getuser(self):
        if hasattr(self, 'user'):
            return self.user
        self.user = get('/user')

        return self.user



    def selfusername(self):
        if hasattr(self, 'user'):
            return self.user['username']

        return self.getuser()['username']

    def getuserlist(self):
        if hasattr(self, 'userlist'):
            return self.userlist

        self.userlist = get('/users')
        return self.userlist

    def finduser(self, username):
        userlist = self.getuserlist()

        for user in userlist:
            if (user['username'] == username):
                return user
        return -1

    def addsshkey(self, username, sshkey):
        user = self.finduser(username)

        res = post('/users/' + str(user['id']) + '/keys',{'id': user['id'], 'title': 'username', 'key': sshkey})
        return res

    def listsshkeys(self, username):
        user = self.finduser(username)

        res = get('/users/' + str(user['id']) + '/keys',{'uid': user['id']})
        return res

    def deletekey(self, uid, keyid):
        res = delete('/users/' + str(uid) + '/keys/' + str(keyid), {'uid': uid, 'id':keyid})
        return res


    def deleteallkeys(self, username):
        keylist = self.listsshkeys(username)
        user = self.finduser(username)

        for key in keylist:
            self.deletekey(user['id'], key['id'])


    def modifykeys(self, username, key):
        self.deleteallkeys(username)
        self.addsshkey(username, key)

    def adduser(self, email, password, username, name):
        res = post('/users', {'email':email, 'password':password, 'username': username, 'name':name})

        return res

    def removeuser(self, username):
        user = self.finduser(username)
        res = delete('/users/' + str(user['id']), {'id':user['id']})

        return res





