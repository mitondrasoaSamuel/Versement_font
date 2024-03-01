import os
class API:
    API = "http://87.98.242.78:8081/api/"
    CLIENT_URL = API + "client"
    VERSEMENT_URL =  API + "versement"
    AUDIT_URL = API + "audit"
    USER_URL = API + "user"
    USER_LOGIN = API + "login"
    USER_REGISTER =  API + "register"
    AUDIT_URL_TOTAL = API + "audit/total"

    TOKEN = "1|Alquur2FPriNJ7mPrXxNSzswP4yDGGXRHBYKr4Jbc3d7af61"
    HEADER = {"Authorization" : f"Bearer {TOKEN}"}

    def set_token(self, data):
        os.environ['auth_token_abda'] = data['auth_token']
        self.HEADER = {"Authorization" : f"Bearer {self.get_token}"}
        
    def get_token(self):
        return os.environ.get('auth_token_abda')
    
    def get_header(self):
        return self.HEADER
     