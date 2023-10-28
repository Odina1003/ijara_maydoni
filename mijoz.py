class Mijoz:
    def __init__(self, ismi, familiyasi, id):
        self._ism = ismi
        self._familiya = familiyasi
        self._id = id
        
    def get_name(self):
        return self._ism
    
    def get_surname(self):
        return self._familiya
    
    def get_id(self):
        return self._id

    def __str__(self):
        return f'{self._ism}, {self._familiya}, {self._id}'