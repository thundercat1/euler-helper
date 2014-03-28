import time
import sys
sys.path.append('/home/mch/Code/Python/euler-helper')
import sieve


def divisors(n, option=1):
    '''
    option 1 (default):
    (int) --> set([ints])
    Returns a set of integers that evenly divide n


    option 2:
    (int) --> {int: set([int])}
    Returns a dictionary with divisors of all numbers up to n 
    in format {int: set([divisor, divisor, divisor]), int: ([divisor, divisor])}
    '''
    
    if option == 1:
        d = set([1, n])
        for candidate in range(2, n/2 + 1):
            if n % candidate == 0:
                d.add(candidate)
                d.add(n / candidate)
        return d


    if option == 2:
        primes = sieve.erat(n,2)
        
        d = {1:set([1]), 2:set([1,2])}
        for i in range(3,n+1):
            d.setdefault(i, set([1,i]))
            if not primes[i]:
                for candidate in range(1,i/2+1):
                    if candidate not in d[i]:
                        #if it's not already identified as a divisor
                        if i % candidate == 0:
                            d[i].add(candidate)
                            d[i].add(i/candidate)
                            if candidate in d:
                                for knownDivisor in d[candidate]:
                                    d[i].add(knownDivisor)
        return d 


if __name__ == '__main__':

    n = 1000000
    print 'running test of option 1 with n = ' + str(n)
    startTime = time.time()
    a = divisors(n)
    endTime = time.time()
    print 'found divisors of ' + str(n) + 'in ' + str(endTime - startTime) + ' sec'

    n = 100000
    print 'running test option 2 with n = ' + str(n)
    startTime = time.time()
    a = divisors(n)
    endTime = time.time()
    print 'found divisors of integers to ' + str(n) + ' in ' + str(endTime-startTime) + 'sec'
