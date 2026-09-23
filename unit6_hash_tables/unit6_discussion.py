"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")
    # Create an empty dictionary. This will be mapping reservation confirmation codes
    # to guest names in a restaurant. Python dictionaries act as builtin hash tables which
    # automatically pass the key through a builtin hash function to convert it into a bucket index.
    reservation_table = {}

    # Add at least 5 key-value pairs for the restaurant reservation system.
    reservation_table["RES101"] = "Elton John"
    reservation_table["RES102"] = "Bob Dylan"
    reservation_table["RES103"] = "David Bowie"
    reservation_table["RES104"] = "Freddie Mercury"
    reservation_table["RES105"] = "Joan Jett"

    # Display the contents of the dictionary
    print(f"Initial Reservation Hash Table: {reservation_table}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # Retrieve and display at least two existing keys.
    guest_101 = reservation_table.get("RES101")
    guest_104 = reservation_table["RES104"]

    # Instead of going through the collection line by line (which is an O(N) search),
    # the hash table uses the keys hash code to go straight to the slot that contains the data.
    # This ends up as a O(1) direct memory reference lookup.
    print(f"Lookup for 'RES101': {guest_101}")
    print(f"Lookup for 'RES104': {guest_104}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print(f"Before Update Operations: {reservation_table}")

    # Update the value associated with an existing key.
    # Since keys need to stay unique, assigning a value to an existing key makes the hash function
    # route over to the exact same bucket. Instead of making a duplicate, it replaces the old
    # memory reference with the newer value.
    reservation_table["RES102"] = "Bob Ross (Table Upgraded)"

    print(f"After Update Operations:  {reservation_table}")

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print(f"Before Delete Operations: {reservation_table}")

    # Delete at least one key-value pair.
    # During deletion, the dictionary finds the keys hash bucket and safely clears the binding entry.
    # This frees up the bucket array slot to accept any new keys or marks it for collision avoidance.
    removed_guest = reservation_table.pop("RES103")
    print(f"Successfully checked out/removed: {removed_guest}")
    print(f"After Delete Operations:  {reservation_table}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Lookup a missing key.
    # Using the bracket notation (reservation_table["RES999"]) would instantly throw a KeyError.
    # Using the .get() method safely returns 'None' if the key isn't found which would prevent
    # a system crash.
    missing_lookup = reservation_table.get("RES999")
    print(f"Edge Case 1: Lookup missing key 'RES999': {missing_lookup}")

    # Edge Case 2: Safely deleting a missing key
    # Trying to delete a missing key using standard methods would crash. Passing a default value
    # fallback like False or None to the .pop() method helps to avoid an error.
    safe_delete = reservation_table.pop("RES999", "Reservation Not Found")
    print(f"Edge Case 2: Delete missing key 'RES999' safely: {safe_delete}")

    print(f"Final Hash Table: {reservation_table}")


if __name__ == "__main__":
    main()