from requests import sessions
from RequestObject import RequestObject
from ResponseObject import ResponseObject


class WebService(object):
    
    def __init__(self, name=None):
        self.name = name

    def send_request(self, request_obj):
        with sessions.Session() as session:
            response = session.request(
                method          = request_obj.method,
                url             = request_obj.url,
                params          = request_obj.params,
                data            = request_obj.data,
                headers         = request_obj.headers,
                cookies         = request_obj.cookies,
                files           = request_obj.files,
                auth            = request_obj.auth,
                timeout         = request_obj.timeout,
                allow_redirects = request_obj.allow_redirects,
                proxies         = request_obj.proxies,
                hooks           = request_obj.hooks,
                stream          = request_obj.stream,
                verify          = request_obj.verify,
                cert            = request_obj.cert,
                json            = request_obj.json       
                )
            return ResponseObject(response)

    def verify_url(self, response_obj, expected_url):
        assert response_obj.get_ulr() == expected_url, 'URL is mismatched as expected: {} instead of {}'.format(response_obj.get_ulr(), expected_url)
        print ('URL is matched as expected: {}'.format(response_obj.get_ulr()))

    def verify_response_status_code(self, response_obj, expected_status_code):
        assert response_obj.get_status_code() == expected_status_code, 'Status code is mismatched as expected: {} instead of {}'.format(expected_status_code, response_obj.get_status_code())
        print ('Status code is matched as expected: {}'.format(expected_status_code))
    
    def verify_response_status_code_in_range(self, response_obj, from_status_code, to_status_code):
        assert response_obj.get_status_code() >= from_status_code and response_obj.get_status_code() <= to_status_code
        print ('Status code is matched as expected in the range: [{},{}]'.format(from_status_code, to_status_code))
    
    def verify_content_type(self, response_obj, expected_content_type):
        assert response_obj.get_content_type() == expected_content_type, 'Content-Type is mismatched as expected: {} instead of {}'.format(expected_content_type, response_obj.get_content_type())
        print ('Content-Type is matched as expected: {}'.format(expected_content_type))
  
    def verify_header_field(self):
        pass
    
    def verify_body_response(self, response_obj, body_response):
        pass
    
    def contains_string(self, response_obj, string):
        pass
    
    def verify_something_more(self):
        pass

def main():
    demo_status_code()
    demo_headers()
    demo_body_response()

def demo_status_code():
    # Create a Request Object
    req = RequestObject()
    req.set_url('https://httpbin.org/post')
    req.set_method('Post')
    req.set_data({'key1':'value1'})
    # Create a Web Service allow sent request
    ws = WebService("Demo")
    res = ws.send_request(req)
    print ('--- Get URL')
    print (res.get_ulr())
    print ('--- Get Status Code')
    print (res.get_status_code())

def demo_headers():
    # Create a Request Object
    req = RequestObject()
    req.set_url('https://httpbin.org/post')
    req.set_method('Post')
    req.set_data({'key1':'value1'})
    # Create a Web Service allow sent request
    ws = WebService("Demo")
    res = ws.send_request(req)
    print ('--- Get Headers')
    print (res.get_headers())

def demo_body_response():
    # Create a Request Object
    req = RequestObject()
    req.set_url('https://httpbin.org/post')
    req.set_method('Post')
    req.set_data({'key1':'value1'})
    # Create a Web Service allow sent request
    ws = WebService("Demo")
    res = ws.send_request(req)
    print ('--- Get Body Content As Json')
    print (res.get_body_response_as_json())
    print ('--- Get Body Content As Text')
    print (res.get_body_response_as_text())
    print ('--- Get Body Content As Bytes')
    print (res.get_body_response_as_bytes())

def demo_verify():
    print('Start Demo 2')

    WS = WebService('My Web Service')
    
    request = RequestObject()
    request.set_name('Get The GitHub\'s public timeline')
    request.set_url('https://api.github.com/events')
    request.set_method('GET')
    
    response = WS.send_request(request)
    WS.verify_response_status_code(response, 200)
    WS.verify_content_type(response, "application/json; charset=utf-8")

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
    
