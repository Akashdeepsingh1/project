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
        print ('Authentication response does not containt ixiaid_token')
        sys.exit()

    # Retrieve authentication token from response
    authenticationToken = response['ixiaid_token']

    # Add authentication token to headers
    global headers
    headers['Authorization'] = authenticationToken

## Get all licenses servers from the current account
def getLicenseServers():
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build license servers URL
    licenseServersUrl = cloudcentralUrl + '/licenseServers'
    r = requests.get(licenseServersUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('License servers error: ' + response['errorMessage'])
        else:
            print ('License servers error')
        sys.exit()

    return response

## Get a summary of all license servers
def getLicenseServersSummary():
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build license servers summary URL
    licenseServersSummaryUrl = cloudcentralUrl + '/licenseServers/summary'
    r = requests.get(licenseServersSummaryUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('License servers summary error: ' + response['errorMessage'])
        else:
            print ('License servers summary error')
        sys.exit()

    return response

## Get detailed information about a specific license server
def getSingleLicenseServer(licenseServerId):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build license servers summary URL
    singleLicenseServerUrl = cloudcentralUrl + '/licenseServers/' + licenseServerId
    r = requests.get(singleLicenseServerUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Single license server error: ' + response['errorMessage'])
        else:
            print ('Single license server error')
        sys.exit()

    return response

## Lookup a license server by its activation code
def searchLicenseServer(activationCode):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build search license server URL
    searchLicenseServerUrl = cloudcentralUrl + '/licenseServers/operations/lookup'
    body = {
        'activationCode': activationCode
    }
    r = requests.post(searchLicenseServerUrl, headers = headers, data = json.dumps(body))

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('License server search error: ' + response['errorMessage'])
        else:
            print ('License server search error')
        sys.exit()

    return response

## Add a list of license servers to the current account
def addLicenseServers(licenseServersIds):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build license servers add summary URL
    addLicenseServerUrl = cloudcentralUrl + '/licenseServers/operations/add'
    body = {
        'assetIds': licenseServersIds
    }
    r = requests.post(addLicenseServerUrl, headers = headers, data = json.dumps(body))

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('License servers add error: ' + response['errorMessage'])
        else:
            print ('License servers add error')
        sys.exit()


## Delete a list of license servers from the current account
def removeLicenseServers(licenseServersIds):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build users summary URL
    removeLicenseServersUrl = cloudcentralUrl + '/licenseServers/operations/remove'
    body = {
        'assetIds': licenseServersIds
    }
    r = requests.post(removeLicenseServersUrl, headers = headers, data = json.dumps(body))

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('License servers remove error: ' + response['errorMessage'])
        else:
            print ('License servers remove error')
        sys.exit()

## Generate report for a list of license servers from the current account
def generateLicenseServersReport(licenseServersIds):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build users summary URL
    generateLicenseServersReportUrl = cloudcentralUrl + '/licenseServers/operations/generateReport'
    body = {
        'assetIds': licenseServersIds
    }
    r = requests.post(generateLicenseServersReportUrl, headers = headers, data = json.dumps(body))

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('License servers report error: ' + response['errorMessage'])
        else:
            print ('License servers report error')
        sys.exit()

## Lookup a license server and add it to the account
def searchLicenseServerAndAddToAccount(activationCode):
    # Search license server with given serial number
    lookupResults = searchLicenseServer(activationCode)

    # Check that the search has any results
    if len(lookupResults) == 0:
        print('No license server found using the activation code provided')
        sys.exit()

    # Example: add first lookup result to the account (for all roles available: license server, chassis, ...)
    lookupResult = lookupResults[0]
    assetIds = []

    for role in lookupResult['roles']:
        assetIds.append(role['id'])

    # Add the lookup result to the acount
    addLicenseServers(assetIds)


## Remove a license server from the account
def removeALicenseServerFromTheAccount():
    # Get all license servers assigned to the account
    licenseServers = getLicenseServers()

    # Check if there are any license servers in the account
    if len(licenseServers) == 0:
        print('There are no license servers assigned to the account')
        sys.exit()

    # Example: get the first license server
    firstLicenseServer = licenseServers[0];
    assetId = firstLicenseServer['id']

    # Remove license server from account
    removeLicenseServers([assetId])


## Get licenses for a specific feature (eg: OSPF)
def findLicensesWithFeature(featureName = 'OSPF'):
    # Get all license servers
    licenseServers = getLicenseServers()

    # Check if there are any license servers in the account
    if len(licenseServers) == 0:
        print('There are no license servers assigned to the account')
        sys.exit()

    #
    for licenseServer in licenseServers:
        licenses = licenseServer['licenses']
        for license in licenses:
            features = license['features']
            for feature in features:
                if featureName in feature:
                    print ('Feature ' + featureName + ' is contained by part number ' + license['partNumber'] +
                    ' and activation code ' + license['activationCode'] + ' on license server ' + licenseServer['address'])