def persistent_counter():
    if not hasattr(persistent_counter, "count"):
        persistent_counter.count = 0
    persistent_counter.count += 1
    print(persistent_counter.count)
    
persistent_counter()
persistent_counter()
persistent_counter()
persistent_counter()