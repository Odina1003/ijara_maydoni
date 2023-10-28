from flat import Flat
from mijoz import Mijoz

class Manager:
    def __init__(self):
        self._flat_list: list[Flat] = []
        self._mijozlar: list[Mijoz] = []

    def new_flat(self, flat: Flat):
        self._flat_list.append(flat)
        print("Kvartira kiritinldi")

    def set_tariffs(self, n):
        res = []
        for i in range(1, n+1):
            res.append(i)
        return res
    
    def get_tariffs(self):
        pass

    def new_client(self, client: Mijoz):
        self._mijozlar.append(client)
        print("Mijoz qo\'shildi")

    def get_clienst(self, clients_id):
        for mijoz in self._mijozlar:
            if mijoz._id == clients_id:
                return mijoz
        return None
    
    def get_clients(self):
        return self._mijozlar