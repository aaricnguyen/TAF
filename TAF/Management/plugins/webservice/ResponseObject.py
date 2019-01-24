
class ResponseObject():

    def __init__(self, response):
        self.response = response
    
    def get_body_content(self):
        return self.response.content
    
    def get_content_type(self):
        return self.response.headers['Content-Type']
        
    def get_elapsed_time(self):
        return self.response.elapsed
    
    def get_headers(self):
        return self.response.headers
    
    def get_response_body_size(self):
        pass
    
    def get_response_header_size(self):
        pass
    
    def get_response_text(self):
        return self.response.text
    
    def get_status_code(self):
        return self.response.status_code
    
    def is_json_content_type(self):
        pass
    
    def is_text_content_type(self):
        pass