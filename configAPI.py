import requests as req

class API:
    API = "http://87.98.242.78:8081/api/"
    CLIENT_URL = API + "client"
    VERSEMENT_URL =  API + "versement"
    USER_LOGIN = API + "login"
    USER_REGISTER =  API + "register"
     ### Gerer utilisateur connecte 
    TOKEN = "1|Alquur2FPriNJ7mPrXxNSzswP4yDGGXRHBYKr4Jbc3d7af61"
    HEADER = {"Authorization" : f"Bearer {TOKEN}"}

    def get_clients():
        return req.get(API.CLIENT_URL, headers=API.HEADER).json()