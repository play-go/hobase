from hobase import *

a = Database(autocommit=True)
a.set({"324234":"123123"}, UserID(123))
print(a.get(UserID(123)))
a.set({"1":"23123"}, UserID(123))
print(a.get(UserID(123)))
print(a)
a.close()
print(a)
