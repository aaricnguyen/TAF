
class ResponseObject():

    def __init__(self, response):
        self.response = response

    def get_status_code(self):
        return self.response.status_code

    def get_elapsed_time(self):
        return self.response.elapsed
    
    def get_ulr(self):
        return self.response.url

    def get_body_response_as_json(self):
        """Return a JSON Response Content"""
        return self.response.json()

    def get_body_response_as_text(self):
        """Return a Text Response Content"""
        return self.response.text

    def get_body_response_as_bytes(self):
        """Return a Binary Response Content"""
        return self.response.content
    
    def get_body_response_raw(self):
        """Return a Binary Response Content"""
        self.response.str   
        return self.response.raw
    
    def get_response_body_size(self):
        pass

    def get_headers(self):
        return self.response.headers

    def get_content_type(self):
        return self.response.headers['Content-Type']

    def get_response_header_size(self):
        pass
    
    def is_json_content_type(self):
        pass
    
    def is_text_content_type(self):
        pass
