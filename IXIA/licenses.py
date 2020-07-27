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
import datetime

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
        print ('Authentication response does not containt ixiaid_token')
        sys.exit()

    # Retrieve authentication token from response
    authenticationToken = response['ixiaid_token']

    # Add authentication token to headers
    global headers
    headers['Authorization'] = authenticationToken

## Get all licenses which are registered on all license servers
def getLicenses():
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build licenses URL
    licensesUrl = cloudcentralUrl + '/licenses'
    r = requests.get(licensesUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Licenses error: ' + response['errorMessage'])
        else:
            print ('Licenses error')
        sys.exit()

    return response

## Get a summary of all licenses
def getLicensesSummary():
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build licenses summary URL
    licensesSummaryUrl = cloudcentralUrl + '/licenses/summary'
    r = requests.get(licensesSummaryUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Licenses summary error: ' + response['errorMessage'])
        else:
            print ('Licenses summary error')
        sys.exit()

    return response

## Get detailed information about a specific part number
def getPartNumberInfo(partNumber):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build part number URL
    partNumberUrl = cloudcentralUrl + '/licenses/' + partNumber
    r = requests.get(partNumberUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Part number error: ' + response['errorMessage'])
        else:
            print ('Part number error')
        sys.exit()

    return response

## Get a summary of the licenses usage over the specified period
def getLicensesUsageSummary(period = '1day'):
    # Define accepted period
    acceptedPeriods = ['1day', '7days', '15days', '30days']

    # Check if period is acceptable
    if period not in acceptedPeriods:
        print ('Usage period is not accepted. Please use a period from the following: ' + str(acceptedPeriods))
        sys.exit()

    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build licenses usage summary URL
    licensesUsageSummaryUrl = cloudcentralUrl + '/licenses/summary/usage?period=' + period
    r = requests.get(licensesUsageSummaryUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('License usage summary error: ' + response['errorMessage'])
        else:
            print ('License usage summary error')
        sys.exit()

    return response

## Get the licenses usage over the specified period
def getLicensesUsage(period = '1day'):
    # Define accepted period
    acceptedPeriods = ['1day', '7days', '15days', '30days']

    # Check if period is acceptable
    if period not in acceptedPeriods:
        print ('Usage period is not accepted. Please use a period from the following: ' + str(acceptedPeriods))
        sys.exit()

    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build licenses usage summary URL
    licensesUsageUrl = cloudcentralUrl + '/licenses/usage?period=' + period
    r = requests.get(licensesUsageUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('License usage error: ' + response['errorMessage'])
        else:
            print ('License usage error')
        sys.exit()

    return response

## Get usage for a specific part number for a particular period
def getPartNumberUsageForPeriod(partNumber, period = '1day'):
    # Define accepted period
    acceptedPeriods = ['1day', '7days', '15days', '30days']

    # Check if period is acceptable
    if period not in acceptedPeriods:
        print ('Usage period is not accepted. Please use a period from the following: ' + str(acceptedPeriods))
        sys.exit()

    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build part number usage summary URL
    partNumberUsageUrl = cloudcentralUrl + '/licenses/' + partNumber + '/usage?period=' + period
    r = requests.get(partNumberUsageUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Part number usage error: ' + response['errorMessage'])
        else:
            print ('Part number usage error')
        sys.exit()

    return response


## Show licenses expiring in less than 30 days
def showLicensesExpiringIn30Days():
    # Get all licenses
    licenses = getLicenses()

    for license in licenses:
        expirationDate = license['expirationDate']
        splittedDate = expirationDate.split('/')
        day = int(splittedDate[0])
        month = int(splittedDate[1])
        year = int(splittedDate[2])
        expirationDate = datetime.datetime(year, month, day)
        presentDatePlus30Days = datetime.datetime.now() + datetime.timedelta(30)
        if expirationDate <= presentDatePlus30Days:
            print('License with part number: ' + license['partNumber'] + ' will expire on ' + license['expirationDate'])