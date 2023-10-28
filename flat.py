class Flat:
    def __init__(self, kod, maydoni):
        self._kod = kod
        self._maydoni = maydoni

    def get_cod(self):
        return self._kod
    
    def get_dimention(self):
        return self._maydoni
    
    def __str__(self):
        return f'{self.get_cod}, {self.get_dimention} metr kvadrat'