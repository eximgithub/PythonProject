from src.Base.Configuration.IConfiguration import IConfiguration


class Configuration(IConfiguration):
    def __init__(self):
        IConfiguration.__init__(self)

    def show(self):
        print('Hello World!')
