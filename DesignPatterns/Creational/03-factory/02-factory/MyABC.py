import abc

class MyABC(abc.ABC):
    """Abstract Base Class definition"""

    @abc.abstractmethod
    def do_something(self, value):
        """Required method"""

    @abc.abstractproperty
    def some_property(self):
        """Required property"""
