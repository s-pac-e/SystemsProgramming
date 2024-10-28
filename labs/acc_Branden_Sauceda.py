import threading

glist = list(range(500))

alist = [0] * 5
def accumulate(i):
    start_index = i * 100
    end_index = start_index + 100
    
    acc = sum(glist[start_index:end_index])
    
    alist[i] = acc
    
    # Get the thread ID
    tid = threading.get_native_id()
    
    # Print monitoring info
    print(f"Accumulated value in thread [{tid} -> {i}] is {acc}")

def main():
    threads = []
    
    for i in range(5):
        thread = threading.Thread(target=accumulate, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    # Calculate the total accumulated value
    total = sum(alist)
    print(f"Total is: {total}")

if __name__ == "__main__":
    main()
