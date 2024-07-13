from computer import Computer
from mycomputer import MyComputer

# encapsulate the attributes in MyComputer class
builder = MyComputer()
builder.build_computer()
computer = builder.get_computer()
computer.display()
