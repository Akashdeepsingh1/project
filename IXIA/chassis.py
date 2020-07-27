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
        print ('Authentication response does not containt ixiaid_token')
        sys.exit()

    # Retrieve authentication token from response
    authenticationToken = response['ixiaid_token']

    # Add authentication token to headers
    global headers
    headers['Authorization'] = authenticationToken

## Get summary topologies for all chassis in the account
def getChassis():
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build chassis URL
    chassisUrl = cloudcentralUrl + '/chassis'
    r = requests.get(chassisUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Chassis error: ' + response['errorMessage'])
        else:
            print ('Chassis error')
        sys.exit()

    return response

## Get detailed topology information for single chassis
def getSingleChassisInfo(chassisId):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build single chassis URL
    singleChassisUrl = cloudcentralUrl + '/chassis/' + chassisId
    r = requests.get(singleChassisUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Single chassis error: ' + response['errorMessage'])
        else:
            print ('Single chassis error')
        sys.exit()

    return response

### Get summary information for all chassis aggregated in the account
def getChassisSummary():
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build chassis summary URL
    chassisSummaryUrl = cloudcentralUrl + '/chassis/summary'
    r = requests.get(chassisSummaryUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Chassis summary error: ' + response['errorMessage'])
        else:
            print ('Chassis summary error')
        sys.exit()

    return response

## Get maxUsage for all chassis in the account for the specified period
def getMaxUsageAllChassisForPeriod(period = '1day'):
    # Define accepted periods
    acceptedPeriods = ['1day', '7days', '15days', '30days']

    # Check if period is acceptable
    if period not in acceptedPeriods:
        print ('Max usage period is not accepted. Please use a period from the following: ' + str(acceptedPeriods))
        sys.exit()

    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build chassis max usage URL
    chassisMaxUsageUrl = cloudcentralUrl + '/chassis/usage?period=' + period
    r = requests.get(chassisMaxUsageUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Chassis max usage error: ' + response['errorMessage'])
        else:
            print ('Chassis max usage error')
        sys.exit()

    return response

## Lookup a chassis by its serial number
def searchChassis(serialNumber):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build search chassis URL
    searchChassisUrl = cloudcentralUrl + '/chassis/operations/lookup'
    body = {
        'serialNo': serialNumber
    }
    r = requests.post(searchChassisUrl, headers = headers, data = json.dumps(body))

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Chassis search error: ' + response['errorMessage'])
        else:
            print ('Chassis search error')
        sys.exit()

    return response

## Add a list of chassis to the current account
def addChassis(chassisArray):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build add chassis URL
    addChassisUrl = cloudcentralUrl + '/chassis/operations/add'
    body = {
        'assetIds': chassisArray
    }
    r = requests.post(addChassisUrl, headers = headers, data = json.dumps(body))

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Chassis add error: ' + response['errorMessage'])
        else:
            print ('Chassis add error')
        sys.exit()

## Remove a list of chassis from the current account
def removeChassis(chassisArray):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build remove chassis URL
    removeChassisUrl = cloudcentralUrl + '/chassis/operations/remove'
    body = {
        'assetIds': chassisArray
    }
    r = requests.post(removeChassisUrl, headers = headers, data = json.dumps(body))

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Chassis remove error: ' + response['errorMessage'])
        else:
            print ('Chassis remove error')
        sys.exit()

    return response

## Generate report for list of chassis
def generateChassisReport(chassisArray):
    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build generate chassis report URL
    generateChassisReportUrl = cloudcentralUrl + '/chassis/operations/generateReport'
    body = {
        'assetIds': chassisArray
    }
    r = requests.post(generateChassisReportUrl, headers = headers, data = json.dumps(body))

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        if 'errorMessage' in response.keys():
            print ('Generate chassis report error: ' + response['errorMessage'])
        else:
            print ('Generate chassis report error')
        sys.exit()

    return response

## Get detailed topology information and detailed usage history
def getDetailedUsageForSingleChassisAndPeriod(chassisId, period = '1day'):
    # Define accepted perios
    acceptedPeriods = ['1day', '7days', '15days', '30days']

    # Check if period is acceptable
    if period not in acceptedPeriods:
        print ('Max usage period is not accepted. Please use a period from the following: ' + str(acceptedPeriods))
        sys.exit()

    # Check if authenticated
    if 'Authorization' not in headers.keys():
        authenticate()

    # Build single chassis usage URL
    singleChassisUsageUrl = cloudcentralUrl + '/chassis/' + chassisId + '/usage?period=' + period
    r = requests.get(singleChassisUsageUrl, headers = headers)

    # Convert response to JSON
    response = r.json()

    # Check if request returned with error
    if r.status_code != 200:
        print ('Detailed usage for single chassis error: '+ response)
        sys.exit()

    return response

## Lookup a chassis and add it to the account
def searchChassisAndAddToAccount(serialNumber):
    # Search chassis with given serial number
    lookupResults = searchChassis(serialNumber)

    # Check that the search has any results
    if len(lookupResults) == 0:
        print('No chassis found using the serial number provided')
        sys.exit()

    # Example: add first lookup result to the account (for all roles available: chassis, license server, ...)
    lookupResult = lookupResults[0]
    assetIds = []

    for role in lookupResult['roles']:
        assetIds.append(role['id'])

    # Add the lookup result to the acount
    addChassis(assetIds)

## Remove a chassis from the account
def removeAChassisFromTheAccount():
    # Get all chassis assigned to the account
    chassis = getChassis()

    # Check if there are any chassis in the account
    if len(chassis) == 0:
        print('There are no chassis assigned to the account')
        sys.exit()

    # Example: get the first chassis
    firstChassis = chassis[0];
    assetId = firstChassis['id']

    # Remove chassis from account
    removeChassis([assetId])

## Get chassis with utilization over a specific threshold percentage
def showChassisWithUtilizationOverThreshold(threshold, period = '1day'):
    # Get chassis data
    chassis = getChassis()

    # Get chassis max usage data for specified period
    maxUsageData = getMaxUsageAllChassisForPeriod(period)

    if 'maxUsage' not in maxUsageData.keys():
        print ('Max usage data not present in the response')
        sys.exit()

    # Get usage dictionary from response
    maxUsageDict = maxUsageData['maxUsage']

    # Iterate through all chassis and get max usage from dictionary using
    # the chassis id as key
    for singleChassis in chassis:
        chassisId = singleChassis['id']
        if chassisId in maxUsageDict.keys() and maxUsageDict[chassisId] >= threshold:
            print('Chassis with serial number: ' + singleChassis['serialNumber']
            + ' and name: ' + singleChassis['name'] + ' has max usage: ' +
            str(maxUsageDict[chassisId]) + '%' + ' for the last ' + period)
