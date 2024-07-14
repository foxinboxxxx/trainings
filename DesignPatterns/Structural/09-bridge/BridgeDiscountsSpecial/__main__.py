from monthly import Monthly
from annual import Annual
from datetime import datetime
from discount import NoDiscount, StudentDiscount, CorporateDiscount
from extend import Extend

def main():
    sub1 = Monthly('Ted', datetime.today(), StudentDiscount)
    sub2 = Annual('Alice', datetime.today(), CorporateDiscount)
    sub3 = Annual('Bob', datetime.today(), NoDiscount)
    sub4 = Annual('Bob-DOUBLE', datetime.today(), NoDiscount, )

    print(f'Subscription: {sub1.subscriber}, Cost: {sub1.price}, Expiration: {sub1.expiration}')
    print(f'Subscription: {sub2.subscriber}, Cost: {sub2.price}, Expiration: {sub2.expiration}')
    print(f'Subscription: {sub3.subscriber}, Cost: {sub3.price}, Expiration: {sub3.expiration}')
    print(f'Subscription: {sub4.subscriber}, Cost: {sub4.price}, Expiration: {sub4.expiration}')

if __name__ == "__main__":
    main()
