class myclass:
    __privateVar=27
    def __privmath(self):
        print("I'm inside class myclass")
    def hello(self):
        print("Private variable values:",myclass.__privateVar)
foo=myclass
foo.hello()
foo.__privateVar            