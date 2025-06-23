class User:
    
    def __init__(self, first_name, last_name):
        self.f_name = first_name
        self.l_name = last_name
        
    def imya(self):
        print("моё имя -", self.f_name)
        
    def familiya(self):
        print("моя фамилия -", self.l_name)
        
    def imya_familiya(self):
        print("собственно -", self.l_name, self.f_name)
        
