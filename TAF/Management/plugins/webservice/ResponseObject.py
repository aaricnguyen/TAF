
class ResponseObject():

    def __init__(self, response):
        self.response = response

    @property
    def get_status_code(self):
        """Return The Status Code"""
        return self.response.status_code
    
    @property
    def get_elapsed_time(self):
        """Return The Time Response In Milliseconds"""
        return self.response.elapsed.microseconds / 1000
    
    @property
    def get_ulr(self):
        """Return The URL Response In String"""
        return self.response.url
    
    @property
    def get_body_response_as_json(self):
        """Return The Body Response As JSON"""
        return self.response.json()
    
    @property
    def get_body_response_as_text(self):
        """Return The Body Response As Text"""
        return self.response.text

    @property
    def get_body_response_as_bytes(self):
        """Return The Body Response As Bytes"""
        return self.response.content
    
    @property
    def get_body_response_raw(self):
        """Return The Body Response Raw""" 
        return self.response.raw

    @property
    def get_headers(self):
        return self.response.headers

    @property
    def get_content_type(self):
        return self.response.headers['Content-Type']