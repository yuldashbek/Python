import threading

def is_prime(n):
    if n < 2 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False 
    return True 
def find_primes(start, end, primes):
    for number in range(start, end):
        if is_prime(number):
            primes.append(number)
if __name__ == "__main__":
    start_range = 1
    end_range = 50
    mid = (start_range + end_range) // 2
primes1 ==[]
primes2 = []
t1 = threading.Thread(target=find_primes, args=(start_range, mid, primes1))
t2 = threading.Thread(target=find_primes, args=(mid, end_range, primes2))
t1.start()
t2.start()
t1.join()
t2.join()

all_primes = sorted(primes1 + primes2)
print("Prime numbers:", all_primes)
