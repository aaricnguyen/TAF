
class RequestObject():

    def __init__(self, name=None, method=None, url=None, params=None,
                data=None, headers=None, cookies=None, files=None,
                auth=None, timeout=None, allow_redirects=True, proxies=None,
                hooks=None, stream=None, verify=None, cert=None, json=None):
        """
        :param name: (optional) request name
        :param method: (required) request "verbs", GET, PUT, POST, DELETE, PATCH, HEAD, etc.
        :param url: (required) URL
        :param params: (optional) Dictionary or bytes to be sent in the query
            string
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body
        :param json: (optional) json to send in the body
        :param headers: (optional) Dictionary of HTTP Headers to send
        :param cookies: (optional) Dict or CookieJar object to send
        :param files: (optional) Dictionary of 'filename': file-like-objects``
            for multipart encoding upload.
        :param auth: (optional) Auth tuple or callable to enable
            Basic/Digest/Custom HTTP Auth.
        :param timeout: (optional) How long to wait for the server to send
            data before giving up, as a float
        :type timeout: float
        :param allow_redirects: (optional) Set to True by default.
        :type allow_redirects: bool
        :param proxies: (optional) Dictionary mapping protocol or protocol and
            hostname to the URL of the proxy.
        :param stream: (optional) whether to immediately download the response
            content. Defaults to False.
        :param verify: (optional) Either a boolean, in which case it controls whether we verify
            the server's TLS certificate, or a string, in which case it must be a path
            to a CA bundle to use. Defaults to True.
        :param cert: (optional) if String, path to ssl client cert file (.pem).
            If Tuple, ('cert', 'key') pair.
        :rtype: requests.Response
        """

        self.name           = name
        self.method         = method
        self.url            = url
        self.headers        = headers
        self.files          = files
        self.data           = data or {}
        self.json           = json
        self.params         = params or {}
        self.auth           = auth
        self.cookies        = cookies
        self.hooks          = hooks
        self.timeout        = timeout
        self.allow_redirects= allow_redirects
        self.proxies        = proxies
        self.stream         = stream
        self.verify         = verify
        self.cert           = cert

    def set_name(self, name):
        self.name = name

    def set_method(self, method):
        self.method = method
  
    def set_url(self, url):
        self.url = url
    
    def set_headers(self, headers):
        self.headers = headers        

    def set_files(self, files):
        self.files = files   

    def set_data(self, data):
        self.data = data   
    
    def set_json(self, json):
        self.json = json
        
    def set_parameters(self, parameters):
        self.params = parameters
    
    def set_cookies(self, cookies):
        self.cookies = cookies

    def set_hooks(self, hooks):
        self.hooks = hooks

    def set_timeout(self, timeout):
        self.timeout = timeout

    def set_allow_redirects(self, allow_redirects):
        self.allow_redirects = allow_redirects
    
    def set_proxies(self, proxies):
        self.proxies = proxies
    
    def set_stream(self, stream):
        self.stream = stream
    
    def set_verify(self, verify):
        self.verify = verify
    
    def set_cert(self, cert):
        self.cert = cert