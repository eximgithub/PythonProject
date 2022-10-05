from threading import Lock, Thread


class DatabaseConfiguration:
    def __init__(self, host, user, passwd, dbname):
        self._host = host
        self._user = user
        self._passwd = passwd
        self._dbname = dbname

    def get_host(self):
        return self._host

    def set_host(self, host):
        self._host = host

    def get_user(self):
        return self._user

    def set_user(self, user):
        self._user = user

    def get_passwd(self):
        return self._passwd

    def set_passwd(self, passwd):
        self._passwd = passwd

    def get_dbname(self):
        return self._dbname

    def set_dbname(self, dbname):
        self._dbname = dbname


# classic implementation of Singleton Design pattern
class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print("init")
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance


def test_singleton() -> None:
    instance = Singleton()
    if instance != Singleton():
        print(Singleton())
    # print(Singleton.getInstance())


# main method
if __name__ == "__main__":
    print("Begin")
    for number in range(0, 100000):
        Thread(target=test_singleton).start()
    print("End")
# </editor-fold>
