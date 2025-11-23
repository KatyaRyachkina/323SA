def create_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
      
    return counter

if __name__ == "__main__":
    counter = create_counter()
    print(counter())
    print(counter())
    print(counter())
