from RequestObject import RequestObject
from ResponseObject import ResponseObject
from WebService import WebService

# HTTP has multiple request "verbs", such as GET, PUT, POST, DELETE, PATCH, HEAD, etc.
request_name = 'Get Method'
request_method = 'GET'
request_base_url = 'https://postman-echo.com/get?foo1=bar1&foo2=bar2'

# Create a request object
req_obj = RequestObject(request_name, request_method, request_base_url)

# Create a web service named "Demo Request Methods"
WS = WebService("Demo Request Methods")

# Execute the get request
res_obj = WS.send_request(req_obj)
print (res_obj.get_status_code)
print (str(res_obj.get_elapsed_time) + ' ms')
print (type(res_obj.get_headers))
WS.verify_response_status_code(res_obj, 200)
WS.verify_response_time_less_than(res_obj, 10000)
print (res_obj.get_body_response_as_text)
print (WS.verify_body_response_has_contains_string(res_obj, '{"foo1":"bar1","foo2":"bar2"}'))