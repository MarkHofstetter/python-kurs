class WifiMessage:

    @property
    def body(self):
        return self.__body
        


class SMS(WifiMessage):
    
    @property
    def phonenumber(self):
        return self.__phonenumber
        
class WifiEmail(WifiMessage):
    
    @property
    def address(self):
        return self.__address
        
    @address.setter
    def address(self, address):
        print('aus setter', address)
        self.__address = address
    
    def send(self):
        print(body)