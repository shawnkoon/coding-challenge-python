class HelloWorld():
    """Basic Hello World class."""

    def __init__(self, name):
        self.name = name
        self.say_text = 'Hello World'

    def say(self):
        return self.say_text
