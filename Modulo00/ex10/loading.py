import time

def ft_progress(lst):
    total = len(lst)
    processed = 0
    start_time = time.time()
    for i, item in enumerate(lst):
        yield item
        processed += 1
        percent = (processed / total) * 100
        elapsed_time = time.time() - start_time
        remaining_time = elapsed_time / processed * (total - processed)
        progress_bar = "=" * int(percent / 5)
        arrow = ">" if i < total - 1 else ""        
        progress_string = "ETA: {:.2f}s [{:>3}%] [{:<20}] {}/{} | elapsed time {:.2f}s".format(
            remaining_time, int(percent), progress_bar + arrow, processed, total, elapsed_time)        
        print("\r{}".format(progress_string), end="")        
    print("\n...")

# Ejemplos del subject:

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem+3) % 5
    time.sleep(0.01)
print(ret)

listy = range(3333)
ret = 0
for elem in ft_progress(listy):    
    ret += elem    
    time.sleep(0.0005)
print()
print(ret) 