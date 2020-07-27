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
email = 'akashdeep.s@dell.com'
password = 'Ixia@12345'

# HTTP Headers
headers = {}

## Authenticate a user with the CloudCentral service
def authenticate():
    # Build login URL
    authenticationUrl = cloudcentralUrl + '/authentication/operations/login'

    # Create login body
    authenticationBody = json.dumps({
        'username': email,
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
        print ('Authentication response does not contain ixiaid_token')
        sys.exit()

    # Retrieve authentication token from response
    authenticationToken = response['ixiaid_token']

    # Add authentication token to headers
    global headers
    headers['Authorization'] = authenticationToken

## Get the current user's preferences
def getPreferences():
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build preferences URL
    preferencesUrl = cloudcentralUrl + '/preferences'
    r = requests.get(preferencesUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Preferences error: ' + response['errorMessage'])
        else:
            print ('Preferences error')
        sys.exit()

    return response

## Update current user's preferences
def updatePreferences(newPreferences):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build preferences URL
    preferencesUrl = cloudcentralUrl + '/preferences'

    r = requests.patch(preferencesUrl, headers = headers, data = json.dumps(newPreferences))

    # Convert response to JSON
    response = r.json()

    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Preferences error: ' + response['errorMessage'])
        else:
            print ('Preferences error')
        sys.exit()

## Create own account
def createOwnAccount():
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build create account URL
    createAccountUrl = cloudcentralUrl + '/preferences/operations/createAccount'

    # Make the login POST request
    r = requests.post(createAccountUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    if r.status_code != 200:
        print ('Create account error: ' + response)
        sys.exit()

## Change first and last name of current user
def changeUserDetails(firstName, lastName):
    # Get current preferences
    preferences = getPreferences()

    # Edit preferences
    preferences["user"]["firstName"] = firstName
    preferences["user"]["lastName"] = lastName

    # Save changes
    updatePreferences(preferences)

## Change default account to an available one
def changeDefaultAccount():
    # Get current preferences
    preferences = getPreferences()

    # Get current account
    if 'currentAccount' not in preferences.keys():
        print ('Preferences error: current account not present in response')
        sys.exit()
    currentAccount = preferences['currentAccount']
    print ('Current account is ' + currentAccount)

    # Get available accounts
    if 'accounts' not in preferences.keys():
        print ('Preferences error: accounts not present in response')
        sys.exit()

    accounts = preferences['accounts']
    if len(accounts) == 1:
        print ('Cannot change default account because there are no other ones available')
        sys.exit()

    # Choose an available account
    for account in accounts:
        # Example: choose the account with admin rights
        if account['id'] != currentAccount and account['type'] == 'administrator':
            print ('Changing default account to ' + account['id'])
            preferences['defaultAccount'] = account['id']

            # Save changes
            updatePreferences(preferences)
            break

## Change notification preferences (example: enable all granular preferences)
def changeNotificationPreferences():
    # Get current preferences
    preferences = getPreferences()

    # Get current notifications preferences
    if 'notifications' not in preferences.keys():
        print ('Preferences error: notifications not present in response')
        sys.exit()
    notificationsPreferences = preferences['notifications']

    # Get granular notifications preferences
    if 'granularPreferences' not in notificationsPreferences.keys():
        print ('Preferences error: granularPreferences not present in response')
        sys.exit()
    granularPreferences = notificationsPreferences['granularPreferences']

    # Example: Enable all granular preferences
    for granularPreference in granularPreferences:
        granularPreference['enabled'] = True

    # Update preferences with new notifications preferences
    preferences['notifications']['granularPreferences'] = granularPreferences

    # Save changes
    updatePreferences(preferences)
