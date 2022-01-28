## PythonSWH - A python library for making calls and getting data from Software Heritage API

#### How to install it - pip install -i https://test.pypi.org/simple/ PythonSWH

#### Methods and their descriptions


|Name|Description|Parameters|
|----|------------|----------|
|getMetaData|function used to get metadata of an open source project|hash type and hash|
|getLicenseInfo|function used to get license info of an open source project|hash type and hash|
|checkAndGetOriginData|function used to check if orign exists in SWH archive and get its info if present|origin url|


#### How to use - from PythonSWH import myFunctions and then myFunctions.getMetaData(param1, param2)

#### for example: myFunctions.getMetaData('sha1','dc2830a9e72f23c1dfebef4413003221baa5fb62')
