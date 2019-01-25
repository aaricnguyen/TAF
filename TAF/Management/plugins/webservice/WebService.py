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
        assert response_obj.get_ulr == expected_url, 'URL is mismatched as expected: {} instead of {}'.format(response_obj.get_ulr, expected_url)
        print ('URL is matched as expected: {}'.format(response_obj.get_ulr()))

    def verify_response_status_code(self, response_obj, expected_status_code):
        assert response_obj.get_status_code == expected_status_code, 'Status code is mismatched as expected: {} instead of {}'.format(expected_status_code, response_obj.get_status_code)
        print ('Status code is matched as expected: {}'.format(expected_status_code))
    
    def verify_response_status_code_in_range(self, response_obj, from_status_code, to_status_code):
        assert response_obj.get_status_code >= from_status_code and response_obj.get_status_code <= to_status_code
        print ('Status code is matched as expected in the range: [{},{}]'.format(from_status_code, to_status_code))
    
    def verify_content_type(self, response_obj, expected_content_type):
        assert response_obj.get_content_type == expected_content_type, 'Content-Type is mismatched as expected: {} instead of {}'.format(expected_content_type, response_obj.get_content_type)
        print ('Content-Type is matched as expected: {}'.format(expected_content_type))
  
    def verify_header_fields(self):
        pass
    
    def verify_body_response(self, response_obj, body_response):
        pass
    
    def verify_body_response_has_contains_string(self, response_obj, string):
        pass
    
    def verify_body_response_equal_to_a_string(self, response_obj, string):
        pass
    
    def verify_response_time_less_than(self, response_obj, expected_time_in_miliseconds):
        pass
    
    def verify_response_time_in_range(self, response_obj, from_time_in_miliseconds, to_time_in_miliseconds):
        pass