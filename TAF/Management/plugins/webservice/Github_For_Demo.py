# Example For Testing RESTFUL With TAF
# Import modules for REST API Testing
from RequestObject import RequestObject
from ResponseObject import ResponseObject
from WebService import WebService

# Github API Documment: https://developer.github.com/v3/users/#get-a-single-user
request_name = 'Get a single user'
request_method = 'GET'
request_base_url = 'https://api.github.com/users/francisnguyen12'

# Create a request object
request = RequestObject(request_name, request_method, request_base_url)

# Create a client web service named "Github-Client"
WS = WebService("Github-Client")

# Execute sending the request to Github Server
response = WS.send_request(request)

# Verify Status Code
WS.verify_response_status_code(response, 200)

# Verify Media Type
WS.verify_content_type(response, 'application/json; charset=utf-8')

# Verify JSON Payload
import json
with open('Github_Expected_Get_A_Single_User.json') as handle:
    expected_json_payload = json.loads(handle.read())

assert expected_json_payload == response.get_body_response_as_json
print ("PASSED")