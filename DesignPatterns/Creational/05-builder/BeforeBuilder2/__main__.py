from computer import Computer

# exposing the attributes
# breaks encapsulate what varies
computer =  Computer()
computer.case = 'Coolermaster'
computer.mainboard = 'MSI'
computer.cpu = 'Intel Core i9'
computer.memory = '2 x 16GB'
computer.hard_drive = 'SSD 2TB'
computer.video_card = 'GeForce'
computer.display()
