from mycomputer_builder import MyComputerBuilder

# enforce build order
builder = MyComputerBuilder()
builder.build_computer()
computer = builder.get_computer()
computer.display()
