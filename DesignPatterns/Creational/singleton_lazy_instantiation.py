class Singleton(object):
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called...")
        else:
            print("Instance already created:", self.getInstance())
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance=Singleton()
        return cls.__instance

# Lazy Instantioation
s = Singleton() ## class initialized, but object not created
print("______")
print("Object created", Singleton.getInstance()) # Object gets created here
s1 = Singleton() ## instance already created
