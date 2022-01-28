#requests package for making HTTP calls to SWH api
import requests
baseSWHUrl = "https://archive.softwareheritage.org/api/1"

#method to get metadata based on hash 
def getMetaData(hashAlgo, hash):
    try:
        response = requests.get(baseSWHUrl+f'/content/{hashAlgo}:{hash}/')
        if response.status_code == 404:
            return "No data found"
        elif response.status_code == 400:
            return "Invalid hash or hash type"
        return response.json()
    except:
        return "an error occured"

#method to get license info based on hash 
def getLicenseInfo(hashAlgo, hash):
    try:
        response = requests.get(baseSWHUrl+f'/content/{hashAlgo}:{hash}/license')
        if response.status_code == 404:
            return "No data found"
        elif response.status_code == 400:
            return "Invalid hash or hash type"
        return response.json()
    except:
        return "an error occured"

#method to check and get origin data 
def checkAndGetOriginData(originUrl):
    try:
        response = requests.get(baseSWHUrl+f'/origin/{originUrl}/get/')
        if response.status_code == 404:
            return "No data found"
        elif response.status_code == 400:
            return "Invalid hash or hash type"
        return response.json()
    except:
        return "an error occured"

