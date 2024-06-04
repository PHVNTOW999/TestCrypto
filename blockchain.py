import datetime
import hashlib
from binascii import unhexlify, hexlify


class Block:
    def __init__(self, prev_hash, transaction, amount):
        self.next = None
        self.__data = {
            'prev_hash': prev_hash,
            'transaction': transaction,
            'amount': amount,
            'hash': '',
            'datatime': datetime.datetime.now().now()
        }

        self.__data['hash'] = self.make_hash()

    def get_data(self):
        return self.__data

    def make_hash(self):
        test_hash = hexlify(hashlib.sha256(unhexlify(self.get_data()['prev_hash'])).digest()).decode('utf-8')

        while test_hash[:2] != '00':
            test_hash = hexlify(hashlib.sha224(unhexlify(test_hash)).digest()).decode("utf-8")
            print(test_hash)
        return test_hash

    def append(self, transaction, amount):
        n = self
        while n.next:
            n = n.next
        prev_hash = n.get_data()['hash']
        end = Block(prev_hash, transaction, amount)
        n.next = end


def print_blocks(block):
    node = block
    print(node.get_data())
    while node.next:
        print(node.get_data())


test_block = Block('00c5a8953b0bbd55c0409b6fcbb3fccab785b819f029a0a82ee17a91', 'Evy2', 100)
test_block.append('Bob', 1090)
test_block.append('Maria', 10)
print_blocks(test_block)
# print(test_block.get_data())
