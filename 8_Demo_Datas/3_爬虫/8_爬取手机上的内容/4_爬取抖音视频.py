from urllib import request
url = 'https://aweme-hl.snssdk.com/aweme/v1/aweme/detail/?version_code=6.5.0&pass-region=1&pass-route=1&js_sdk_version=1.16.2.7&app_name=aweme&vid=9D5F078E-A1A9-4F64-81C7-F89CA6A3B1DC&app_version=6.5.0&device_id=34712926793&channel=App Store&mcc_mnc=46011&aid=1128&screen_width=750&openudid=263bd93f02801d126ca004edccbff8f6e1b19f51&os_api=18∾=WIFI&os_version=12.3.1&device_platform=iphone&build_number=65014&device_type=iPhone9,1&iid=74239983401&idfa=F39B285A-4B4F-4874-9D7E-C728A892BF6D'

headers = {
    'User-Agent': 'Aweme 6.5.0 rv:65014 (iPhone; iOS 12.3.1; en_CN) Cronet',
}

req=request.Request(url=url,headers=headers)
response=request.urlopen(req)
res=response.read()
print(res)