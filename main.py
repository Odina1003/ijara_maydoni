from manager import Manager
from flat import Flat
from mijoz import Mijoz

manager = Manager()

flat1 = Flat(12, 9)
client1 = Mijoz("Said", "Azizov", 1)


manager.new_flat(flat1)
# print(manager.set_tariffs(4))
print(manager.new_client(client1))
print(manager.get_clienst(1))
print(manager.get_clients())