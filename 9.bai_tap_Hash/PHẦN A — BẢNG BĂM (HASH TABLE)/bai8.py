bang = [None] * 10

def chen(chi_so):
    i = 0
    
    while bang[(chi_so + i * i) % 10] is not None:
        i += 1
    
    bang[(chi_so + i * i) % 10] = "X"
    
chen(3)
chen(3)

print(bang)