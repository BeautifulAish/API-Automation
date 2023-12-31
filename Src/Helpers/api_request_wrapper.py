#To Make the  -  POST,PUT,PATCH,DELETE
import requests

#HTTP METHODS - Generic Functions

#data =get_request("https://restful-booker.com/booking/1", in_json= True)
 #data - In return in json, normal in json !True

 #xml data - json data
def get_request(url,auth, in_json):
    response = requests.get(url = url,auth=auth)
    if in_json is True:
        return response.json()
    return response

def post_requests(url,auth,headers, payload, in_json):
    post_response_data = requests.post(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return post_response.json()
    return response

def patch_requests(url,auth,headers, payload, in_json):
    patch_response_data = requests.patch(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return patch_response.json()
    return response

def put_requests(url,auth,headers,payload,in_json):
    post_response_data = requests.put(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return put_response.json()
    return response

def delete_requests(url,auth,headers,payload,in_json):
    post_response_data = requests.delete(url=url,headers=headers,auth=auth,data=json.dumps(payload))
    if in_json is True:
        return delete_response.json()
    return response
