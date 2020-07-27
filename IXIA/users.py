################################################################################
#                                                                              #
#    Copyright 2017 - 2018 by IXIA Keysight                                    #
#    All Rights Reserved.                                                      #
#                                                                              #
################################################################################

################################################################################
#                                                                              #
#                                LEGAL  NOTICE:                                #
#                                ==============                                #
# The following code and documentation (hereinafter "the script") is an        #
# example script for demonstration purposes only.                              #
# The script is not a standard commercial product offered by Ixia and have     #
# been developed and is being provided for use only as indicated herein. The   #
# script [and all modifications, enhancements and updates thereto (whether     #
# made by Ixia and/or by the user and/or by a third party)] shall at all times #
# remain the property of Ixia.                                                 #
#                                                                              #
# Ixia does not warrant (i) that the functions contained in the script will    #
# meet the user's requirements or (ii) that the script will be without         #
# omissions or error-free.                                                     #
# THE SCRIPT IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, AND IXIA        #
# DISCLAIMS ALL WARRANTIES, EXPRESS, IMPLIED, STATUTORY OR OTHERWISE,          #
# INCLUDING BUT NOT LIMITED TO ANY WARRANTY OF MERCHANTABILITY AND FITNESS FOR #
# A PARTICULAR PURPOSE OR OF NON-INFRINGEMENT.                                 #
# THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE SCRIPT  IS WITH THE #
# USER.                                                                        #
# IN NO EVENT SHALL IXIA BE LIABLE FOR ANY DAMAGES RESULTING FROM OR ARISING   #
# OUT OF THE USE OF, OR THE INABILITY TO USE THE SCRIPT OR ANY PART THEREOF,   #
# INCLUDING BUT NOT LIMITED TO ANY LOST PROFITS, LOST BUSINESS, LOST OR        #
# DAMAGED DATA OR SOFTWARE OR ANY INDIRECT, INCIDENTAL, PUNITIVE OR            #
# CONSEQUENTIAL DAMAGES, EVEN IF IXIA HAS BEEN ADVISED OF THE POSSIBILITY OF   #
# SUCH DAMAGES IN ADVANCE.                                                     #
# Ixia will not be required to provide any software maintenance or support     #
# services of any kind (e.g., any error corrections) in connection with the    #
# script or any part thereof. The user acknowledges that although Ixia may     #
# from time to time and in its sole discretion provide maintenance or support  #
# services for the script, any such services are subject to the warranty and   #
# damages limitations set forth herein and will not obligate Ixia to provide   #
# any additional maintenance or support services.                              #
#                                                                              #
################################################################################

import requests
import json
import sys

### Configuration
# REST API URL
cloudcentralUrl = 'https://cloudcentral.saas.ixiacom.com/api/v2'
# IXIA account credentials
email = ''
password = ''

# HTTP Headers
headers = {}

## Authenticate a user with the CloudCentral service
def authenticate():
    # Build login URL
    authenticationUrl = cloudcentralUrl + '/authentication/operations/login'

    # Create login body
    authenticationBody = json.dumps({
        'username': username,
        'password': password
    })

    # Make the login POST request
    r = requests.post(authenticationUrl, data = authenticationBody)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Authentication error: ' + response['errorMessage'])
        else:
            print ('Authentication error')
        sys.exit()

    # Check if response contains "ixiaid_token"
    if 'ixiaid_token' not in response.keys():
        print ('Authentication response does not containt ixiaid_token')
        sys.exit()

    # Retrieve authentication token from response
    authenticationToken = response['ixiaid_token']

    # Add authentication token to headers
    global headers
    headers['Authorization'] = authenticationToken

## Get detailed user information
def getUsers():
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build users URL
    usersUrl = cloudcentralUrl + '/users'
    r = requests.get(usersUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Users error: ' + response['errorMessage'])
        else:
            print ('Users error')
        sys.exit()

    return response

## Get a single user's detail
def getSingleUserInfo(username):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build users summary URL
    singleUserUrl = cloudcentralUrl + '/users/' + username
    r = requests.get(singleUserUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Single user error: ' + response['errorMessage'])
        else:
            print ('Single user error')
        sys.exit()

    return response

## Get aggregated user information
def getUsersSummary():
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build users summary URL
    usersUrl = cloudcentralUrl + '/users/summary'
    r = requests.get(usersUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Users summary error: ' + response['errorMessage'])
        else:
            print ('Users summary error')
        sys.exit()

    return response

## Update a single user's details
def updateSingleUserInfo(username, userData):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build users summary URL
    singleUserUrl = cloudcentralUrl + '/users/' + username
    r = requests.patch(singleUserUrl, headers = headers, data = json.dumps(userData))

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Update single user error: ' + response['errorMessage'])
        else:
            print ('Update single user error')
        sys.exit()

## Add a single user to the account
def addSingleUser(userData):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build users summary URL
    usersUrl = cloudcentralUrl + '/users'
    r = requests.post(singleUserUrl, headers = headers, data = json.dumps(userData))

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Add single user error: ' + response['errorMessage'])
        else:
            print ('Add single user error')
        sys.exit()

## Change user's role to administrator
def makeUserAdmin(username):
    # Get user's info
    userInfo = getSingleUserInfo(username)

    # Change role to 'administrator'
    userInfo['type'] = 'administrator'

    # Update user
    updateSingleUserInfo(username, userInfo)

## Change user's role to readonly
def makeUserReadonly(username):
    # Get user's info
    userInfo = getSingleUserInfo(username)

    # Change role to 'readonly'
    userInfo['type'] = 'readonly'

    # Update user
    updateSingleUserInfo(username, userInfo)

## Get last seen for a specific user
def getLastSeenForUser(username):
    # Get user's info
    userInfo = getSingleUserInfo(username)

    # Get last seen info from user
    lastSeen = userInfo['lastSeen']

    return lastSeen

## Get active users
def getActiveUsers():
    # Get users
    users = getUsers()

    # Filter only the active ones
    activeUsers = [user for user in users if user['active'] == True]

    return activeUsers
