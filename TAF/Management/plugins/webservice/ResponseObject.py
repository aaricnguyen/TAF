
class ResponseObject():

    def __init__(self, response):
        self.response = response

    @property
    def get_status_code(self):
        return self.response.status_code
    
    @property
    def get_elapsed_time(self):
        return self.response.elapsed
    
    @property
    def get_ulr(self):
        return self.response.url
    
    @property
    def get_body_response_as_json(self):
        """Return a JSON Response Content"""
        return self.response.json()
    
    @property
    def get_body_response_as_text(self):
        """Return a Text Response Content"""
        return self.response.text

    @property
    def get_body_response_as_bytes(self):
        """Return a Binary Response Content"""
        return self.response.content
    
    @property
    def get_body_response_raw(self):
        """Return a Binary Response Content"""
        self.response.str   
        return self.response.raw
    
    @property
    def get_response_body_size(self):
        pass

    @property
    def get_headers(self):
        return self.response.headers

    @property
    def get_content_type(self):
        return self.response.headers['Content-Type']

    @property
    def get_response_header_size(self):
        pass
    
    @property
    def is_json_content_type(self):
        pass
    
    @property
    def is_text_content_type(self):
        pass
