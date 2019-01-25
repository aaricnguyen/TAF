from WebService import WebService
from RequestObject import RequestObject
from ResponseObject import ResponseObject

def main():
    demo_http_method()

def demo_http_method():
    pass

def demo_http_authentication():
    pass

def demo_http_cookies():
    pass

# def demo_status_code():
#     # Create a Request Object
#     req = RequestObject()
#     req.set_url('https://httpbin.org/post')
#     req.set_method('Post')
#     req.set_data({'key1':'value1'})
#     # Create a Web Service allow sent request
#     ws = WebService("Demo")
#     res = ws.send_request(req)
#     print ('--- Get URL')
#     print (res.get_ulr)
#     print ('--- Get Status Code')
#     print (res.get_status_code)

# def demo_headers():
#     # Create a Request Object
#     req = RequestObject()
#     req.set_url('https://httpbin.org/post')
#     req.set_method('Post')
#     req.set_data({'key1':'value1'})
#     # Create a Web Service allow sent request
#     ws = WebService("Demo")
#     res = ws.send_request(req)
#     print ('--- Get Headers')
#     print (res.get_headers)

# def demo_body_response():
#     # Create a Request Object
#     req = RequestObject()
#     req.set_url('https://httpbin.org/post')
#     req.set_method('Post')
#     req.set_data({'key1':'value1'})
#     # Create a Web Service allow sent request
#     ws = WebService("Demo")
#     res = ws.send_request(req)
#     print ('--- Get Body Content As Json')
#     print (res.get_body_response_as_json)
#     print ('--- Get Body Content As Text')
#     print (res.get_body_response_as_text)
#     print ('--- Get Body Content As Bytes')
#     print (res.get_body_response_as_bytes)

# def demo_verify():
#     print('Start Demo 2')

#     WS = WebService('My Web Service')
    
#     request = RequestObject()
#     request.set_name('Get The GitHub\'s public timeline')
#     request.set_url('https://api.github.com/events')
#     request.set_method('GET')
    
#     response = WS.send_request(request)
#     WS.verify_response_status_code(response, 200)
#     WS.verify_content_type(response, "application/json; charset=utf-8")

if __name__ == "__main__":
    main()

#     print(response_object.text)
#     print(response_object.json())
#     print(response_object.content)
#     print(response_object.content.decode("utf-8"))
#     # Headers is a dictionary
#     print(response_object.headers)
#     
#     # Get the content-type from the dictionary.
#     print(response_object.headers["content-type"])