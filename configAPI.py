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

    TOKEN = "6|F9z6xWmgb8va3zMp2MMwvpz5bi9BKAtm6qIHY1zY3baa7466"
    HEADER = {"Authorization" : f"Bearer {TOKEN}"}

    def set_token(self, data):
        os.environ['auth_token_abda'] = data['auth_token']
        self.HEADER = {"Authorization" : f"Bearer {self.get_token}"}
        
    def get_token(self):
        return os.environ.get('auth_token_abda')
    
    def get_header(self):
        return self.HEADER
     