
import json
import os
# connect to the server
import requests
from requests import Request, Session, RequestException

# get the cookie from ~/.lapis/auth.cookie
with open(os.path.expanduser('~/.lapis/auth.cookie'), 'r') as f:
    cookie = f.read()

import lapiscli.config as config
url = config.get('host')
# make a post request with file in form-data
def login(username, password):
    # make a GET request to url with user and password in form-data
    response = requests.post(url + 'login', data={'username': username, 'password': password})
    # if the response is 200, save the cookie to ~/.lapis/auth.cookie
    if response.status_code == 200:
        with open(os.path.expanduser('~/.lapis/auth.cookie'), 'w') as f:
            f.write(response.cookies['token'])
            return response
    else:
        return response

def signup(username, password,email):
    # POST a request to /signup
    response = requests.post(url + 'signup', data={'username': username, 'password': password, 'email': email})
    return response

def logout():
    response = requests.get(url + 'logout')
    # print the response
    return response

def list_builds():
    # make a GET request to url with user and password in form-data
    response = requests.get(url + 'builds')
    # response text is an array of json objects
    # format it so it looks pretty
    return json.dumps(json.loads(response.text), indent=4)
    #print(response.text)

def build(buildroot, path):
    # POST a request to /build
    # check if the path is a link or a path to a file
    if os.path.exists(path):
        # if it's a path, send it as a file as form-data
        files = {'file': open(path, 'rb')}
    elif path.startswith('http') or path.startswith('https'):
        # if its a link send the link as form called 'link'
        files = {'link': path}
    # finally make a post request with the cookie and the file
    response = requests.post(url + 'builds/submit', cookies={'token': cookie} , data={'buildroot': buildroot}, files=files)
    return response

##### Buildroots #####
def list_buildroots():
    # make a GET request to url with user and password in form-data
    response = requests.get(url + 'buildroot/', cookies={'token': cookie})
    # response text is an array of json objects
    # format it so it looks pretty
    return json.dumps(json.loads(response.text), indent=4)

def init_buildroot(file, comps=None):
    # get the file path
    # upload the file with form-data
    # if the comps are not None, send them as form-data
    if comps:
        files = {'mock': open(file, 'rb'), 'comps': open(comps, 'rb')}
    else:
        response = requests.post(url + 'buildroot/submit',cookies={'token': cookie}, files={'mock': open(file, 'rb')})
    return response

#login('cappy', 'password')
#logout()
#list_builds()