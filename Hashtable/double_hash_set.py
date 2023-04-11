from open_hash_node import Open_Hash_Node

class Double_Hash_Set():

    def __init__(self, capacity = 0):
        self.hash_table = [None] * capacity
        self.table_size = 0

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
        return self.table_size

    def get_hash_code_2(self, key, hash_table_length):
        """Hash function 2 for double hashing, that calculates a key specific offset.
        @param key:
        		Key for which a hash code shall be calculated according to the length of the hash table.
        @param hash_table_length:
        		Length of the hash table.
        @return:
        		The calculated hash code for the given key.
        """
        h1 = key % hash_table_length
        h2 = 1 + key % (hash_table_length - 1)
        return h1, h2

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
            raise ValueError("You Donkey!")
        h1, h2 = self.get_hash_code_2(key, len(self.hash_table))

        inserted = False
        if self.contains(key) is True:
            return inserted
        if self.table_size == len(self.hash_table):
            return inserted
        else:
            if self.hash_table[h1] is None:
                self.hash_table[h1] = Open_Hash_Node(key, data)
                self.table_size += 1
                inserted = True
            else:
                while not inserted:
                    new_hash = (h1 + h2) % len(self.hash_table)
                    if self.hash_table[new_hash] is None:
                        self.hash_table[new_hash] = Open_Hash_Node(key, data)
                        self.table_size += 1
                        inserted = True
                    else:
                        h1 = new_hash

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
            raise ValueError("You are a disgrace!")
        for x in self.hash_table:
            if x: # case: None-element in list
                if x.key is key:
                    found = True
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

        h1, h2 = self.get_hash_code_2(key, len(self.hash_table))

        if self.hash_table[h1].key == key:
            self.hash_table[h1].removed = True
            self.hash_table[h1] = None
            self.table_size -= 1
            found = True
        else:
            for x in range(self.table_size):
                new_hash = (h1 + h2) % len(self.hash_table)
                if self.hash_table[new_hash]: # case: does node exist?
                    if self.hash_table[new_hash].key == key:
                        self.hash_table[new_hash].removed = True
                        self.hash_table[new_hash] = None
                        self.table_size -= 1
                        found = True
                    else:
                        h1 = new_hash

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

    def print_tablekeys(self):
        i = 0
        for x in self.hash_table:
            if x:
              self.hash_table[i] = x.key
            i += 1

        return self.hash_table

if __name__ == "__main__":
    dbl = Double_Hash_Set(5)
    print(dbl.insert(0, "."))
    print(dbl.insert(5, "."))
    print(dbl.insert(2, "."))
    # test index 1 is used
    print(dbl.insert(1, "."))

    # test index 4 also taken
    print(dbl.insert(4, "."))

    print(dbl.remove(2))
    print(dbl.print_tablekeys())

    print(dbl.table_size)