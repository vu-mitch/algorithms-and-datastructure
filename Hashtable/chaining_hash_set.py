from chaining_hash_node import Chaining_Hash_Node

class Chaining_Hash_Set():

    def __init__(self, capacity = 0):
        self.hash_table = [None] * capacity
        self.table_size = 0

    def get_hash_code(self, key, hash_table_length):
        """Hash function that calculates a hash code for a given key using the modulo division.
        @param key:
        		Key for which a hash code shall be calculated according to the length of the hash table.
        @param hash_table_length:
        		Length of the hash table.
        @return:
        		The calculated hash code for the given key.
        """
        return key % hash_table_length

    def get_hash_table(self):
        """(Required for testing only)
        @return the hash table.
        """
        return self.hash_table

    def set_hash_table(self, table, size):
        """(Required for testing only) Set a given hash table which shall be used.
        @param table:
        		Given hash table which shall be used.
        @param size:
        		Number of already stored keys in the given table.
        """
        self.hash_table = table
        self.table_size = size

    def get_table_size(self):
        """returns the number of stored keys (keys must be unique!).
    	 """
        counter = 0
        for x in self.hash_table:
            if x:
                while x:
                    counter += 1
                    x = x.next

        return counter

    def insert(self, key, data):
        """Inserts a key and returns true if it was successful. If there is already an entry with the
          same key or the hash table is full, the new key will not be inserted and false is returned.

         @param key:
         		The key which shall be stored in the hash table.
         @param data:
         		Any data object that shall be stored together with a key in the hash table.
         @return:
         		true if key could be inserted, or false if the key is already in the hash table.
         @throws:
         		a ValueError exception if any of the input parameters is None.
         """
        if key is None or data is None:
            raise ValueError("You Donkey, Donkey, donkey!")

        index = self.get_hash_code(key, len(self.hash_table))
        inserted = True

        if self.contains(key) is True:
            inserted = False
        else:
            if self.hash_table[index] is None:
                self.hash_table[index] = Chaining_Hash_Node(key, data)
                self.table_size += 1
            else: # chaining
                current = self.hash_table[index]
                while current:
                    if current.next is None:
                        current.next = Chaining_Hash_Node(key, data)
                        self.table_size += 1
                        break
                    current = current.next

        return inserted

    def contains(self, key):
        """Searches for a given key in the hash table.
         @param key:
         	    The key to be searched in the hash table.
         @return:
         	    true if the key is already stored, otherwise false.
         @throws:
         	    a ValueError exception if the key is None.
         """
        found = False
        if key is None:
            raise ValueError("You Donkey, Donkey, Donkey!")
        for x in self.hash_table:
            if x: # case: None-element in list
                while x:
                    if x.key is key:
                        found = True
                    x = x.next

        return found

    def remove(self, key):
        """Removes the key from the hash table and returns true on success, false otherwise.
        @param key:
        		The key to be removed from the hash table.
        @return:
        		true if the key was found and removed, false otherwise.
        @throws:
         	a ValueError exception if the key is None.
        """
        if key is None:
            raise ValueError("You Donkey, Donkey, Donkey!")

        found = False
        i = 0

        for parent in self.hash_table:
            if parent: # case: None in table
                if parent.key is key: # case: first node
                    self.hash_table[i] = None
                    self.table_size -= 1
                    found = True
                else: # case: search in chain
                    node = parent.next
                    while node:
                        if node.key == key:
                            parent.next = None
                            found = True
                            self.table_size -= 1
                            if node.next: # case: connect parent.next
                                parent.next = node.next
                            break
                        parent = parent.next # obtain parent
                        node = node.next
            i += 1

        return found

    def clear(self):
        """Removes all stored elements from the hash table by setting all nodes to None.
        """
        i = 0
        for x in self.hash_table:
            if x:
                self.hash_table[i] = None
            i += 1
        self.table_size = 0

if __name__ == "__main__":
    tbl = Chaining_Hash_Set(5)
    tbl.insert(5,".")
    tbl.insert(10,".")
    tbl.insert(15,".")
    print(tbl.hash_table[0].key)
    print(tbl.hash_table[0].next.key)
    print(tbl.hash_table[0].next.next.key)
    tbl.remove(10)
    print()
    print(tbl.hash_table[0].key)
    print(tbl.hash_table[0].next.key)
    print(tbl.hash_table[0].next.next)
    tbl.remove(5)
    print(tbl.hash_table)
    tbl.insert(8,".")
    print(tbl.hash_table)
    tbl.remove(8)
    print(tbl.hash_table)
