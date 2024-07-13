import datetime
from singleton_meta import Singleton

class Logger(metaclass=Singleton):
    """
    The metaclass then is completely distinct and has but one responsibility, manage the instances of the classes it is responsible for. 
    A separation of concerns is complete. 
    """
    log_file = None

    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path,mode='w')

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = f'{now}: {log_record}\n'
        self.log_file.write(record)

    def close_log(self):
        self.log_file.close() 
        self.log_file = None       
