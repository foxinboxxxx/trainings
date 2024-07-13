from MyABC import MyABC

class MyClass(MyABC):
    """Implementation of abstract base class"""

    def __init__(self, value=None):
        self._myprop = value

    def do_something(self, value):
        """Implementation of abstract method"""
        self._myprop *= value

    @property
    def some_property(self):
        """Implementation of abstract property"""
        return self._myprop
        