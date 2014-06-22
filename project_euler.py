## Project Euler Solutions
## MIT License, 2014 Gurjot S. Sidhu

def factors(n):
    import functools as func
    return set(func.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def largest_prime_factor(x):
    allf = list(factors(x))
    for i in allf:
        pass

def palindrome_number(m,n):
    '''
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    '''
    import math
    ans = []
    num = []
    for j in range(m,n):
        num.append(str(j))
    products = []
    for j in num:
        for k in num:
            product = str(int(j) * int(k))
            lisp = list(product)
            if lisp[0] == lisp[-1]:
                if lisp[1] == lisp[-2]:
                    if lisp[2] == lisp[-3]:
                        if lisp[3] == lisp[-4]:
                            products.append(product)
            if product == '998001':
                num.clear()
    return max(products)

def fibo(x):
    w = []
    f = 'o'*(x-2)
    w = list(f)
    l = [0,1]
    l.extend(w)
    for j in range(2,x):
        l[j] = int(l[j-1]) + int(l[j-2])
    return l

def nth_fibo(n):
    import time
    t1 = time.time()
    f = fibo((5000 * ((n//1045)+1)))
    for i in range(0,len(f)):
        if len(str(f[i])) == n:
            t2 = time.time()
            print(t2-t1)
            return f[i], i
    
def isfibo(x):
    squares = []
    for i in range(0,1000):
        squares.append(i**2)
    if (5*(x**2) + 4) == i*i or (5*(x**2) - 4) == i*i:
        return True
    else:
        return False

def even_fibo_sum(x):
    '''
    Sum of even fibonacci numbers under x.
    '''
    l = fibo(x)
    sums = 0
    for i in l:
        if i%2 == 0:
            sums += i
    return sums

def sum_square_diff(x):
    '''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

    '''
    square = 0
    sums = 0
    sum_square = 0
    nums = []
    for i in range(1,x+1):
        nums.append(i)
    
    for i in nums:
        square += i**2
        sums += i
        sum_square = sums**2
    
    return sum_square - square

def primes(m,x):
    '''
    Primes till x
    '''
    import time
    t1 = time.time()
    primes = []
    for i in range(m,x+1):
        if isprime(i) == True:
            primes.append(i)
    t2 = time.time()
    print(t2 - t1)
    return primes

def x_prime(x):
    '''
    Xth prime
    '''
    import time
    t1 = time.time()
    prime = primes(x*100)
    a = prime[x-1]
    t2 = time.time()
    print (t2 - t1)
    return a
        
def isprime(x):
    nums = []
    l = []

    for i in range(2,int(x**0.5)+1):
##        nums.append(i)
##    for i in nums:
        if x%i == 0:        
            return False
    return True

def n_prime(x):
    prime = []
    prime = primes(10000)
    return prime[x-1]

def sum_prime(m,n):
    '''
Sum of all primes below x
    '''
    import time
    t1 = time.time()
    sums = 0
    for i in range(m,n+1):
        if isprime(i) == True:
            sums += i
    t2 = time.time()
    print(t2 - t1)
    return sums

def shit():
    import time
    t1 = time.time()
    a = sum_prime(2,100000) + sum_prime(100000,200000) + sum_prime(200000,300000) + sum_prime(300000,400000) + sum_prime(400000,500000) + sum_prime(500000,600000) + sum_prime(600000,700000)+ sum_prime(700000,800000) + sum_prime(800000,900000) + sum_prime(900000,1000000) + sum_prime(1000000,1100000) + sum_prime(1100000,1200000) + sum_prime(1200000,1300000) + sum_prime(1300000,1400000) + sum_prime(1400000,1500000) + sum_prime(1500000,1600000) + sum_prime(1600000,1700000)+ sum_prime(1700000,1800000) + sum_prime(1800000,1900000) + sum_prime(1900000,2000000)
    t2 = time.time()
    print(t2 - t1)
    return a

def largest_product():
    number = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    l = []
    product = 0
    for i in range(0, len(number)-5):
        product = int(number[i])*int(number[i+1])*int(number[i+2])*int(number[i+3])*int(number[i+4])
        l.append(product)
    return max(l)

def chunks(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def pythagorean():
    nums = []
    trips = []
    ans = []
    sums = 0
    for i in range(1,1000):
        nums.append(str(i))
    for a in nums:
        for b in nums:
            for c in nums:
                if int(a)**2 + int(b)**2 == int(c)**2:
                    if int(a) + int(b) + int(c) == 1000:
                        return a,b,c

def triang(x,d):
    '''
Returns the first number in range (1,x) which has greater than d divisors.

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

What is the value of the first triangle number to have x divisors?

    '''
    import time
    t1 = time.time()
    nums = []
    for i in range(1,x+1):
        nums.append(i)
    g = 'o'*(x-1)
    w = list(g)
    l = [1]
    l.extend(w)
    alist = []
    f = []
    for j in range(1, len(l)):
            l[j] = sum(nums[0:j+1])
##            f.append(factors(l[j]))
            if len(factors(l[j])) > d:
                t2 = time.time()
                print (t2-t1)
                return (l[j])
    

def collatz(x):
    '''
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1

    '''
    l = [x]

    for i in l:
        if i != 1:
            if i % 2 == 0:
                l.append(i//2)
            else:
                l.append(3*i + 1)
##        k.append(len(l)) 
    return l
##max(k), (k.index(max(k)) + 2)

def max_collatz(x):
    '''
Which starting number, under x, produces the longest chain?

    '''
    l = []
    k = []
    for j in range(2,x+1):
        l.append(j)
    for i in l:
        k.append(len(collatz(i)))
    return max(k), k.index(max(k))+2

def power_digit_sum(x, y):
    a = str(x**y)
    b = list(a)
    c = 0
    for i in b:
        c += int(i)

    return a, c

def factorial(x):
    '''
    Return factorial and sum of digits of the factorial
    '''
    factory = 1
    nums = []
    for i in range(1,x+1):
        nums.append(i)
    for i in nums:
        factory *= i
    s = 0
    a = list(str(factory))
    for i in a:
        s += int(i)
    return factory

def amicable(m,n):
    nums = []
    ans = []
    s = 0
    for i in range(m,n+1):
        nums.append(i)
    for x in nums:
        one = list(factors(x))
        one_a = sum(one) - x
        two = list(factors(one_a))
        two_a = sum(two) - one_a
        if two_a == x:
            if two_a+1 != one_a+1:
                ans.append(x)
                ans.append(one_a)
    for i in ans:
        if ans.count(i) == 2:
            ans.remove(i)
    for i in ans:
        s += i
    return ans

def names():
    import fileinput
    import re
    dic = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "\"": 0}
    n = []
    a = []
    names = []
    p1 = re.compile("\"[A-Z][A-Z]\"")
    p2 = re.compile("\"[A-Z][A-Z][A-Z]\"")
    p3 = re.compile("\"[A-Z][A-Z][A-Z][A-Z]\"")
    p4 = re.compile("\"[A-Z][A-Z][A-Z][A-Z][A-Z]\"")
    p5 = re.compile("\"[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]\"")
    p6 = re.compile("\"[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]\"")
    p7 = re.compile("\"[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]\"")
    p8 = re.compile("\"[A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z][A-Z]\"")

    for word in fileinput.input("names.txt"):
        n = word

    n.replace("\"", "1")
    
    a.append(re.findall(p1,n))
    a.append(re.findall(p2,n))
    a.append(re.findall(p3,n))
    a.append(re.findall(p4,n))
    a.append(re.findall(p5,n))
    a.append(re.findall(p6,n))
    a.append(re.findall(p7,n))
    a.append(re.findall(p8,n))
    for i in a:
        for j in i:
            names.append(j)
    return names

def names_in_order():
    n = []
    import fileinput
    dic = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "\"": 0}
    for word in fileinput.input("names.txt"):
        for i in range(0,len(word)):
            while word[i].isalpha() == True:
                n.append(word[i])
                if word[i].isalpha() == False:
                    break
                continue
    return n
    
def names_sum():
    import time
    t1 = time.time()
    dic = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "\"": 0}
    a = ["\"", "!", "?"]
    name = names()
    n_sum = 0
    n_sum_value = 0
    n_list = []
    for i in name:
        for j in i:
            for k in j:
                if k not in a:
                    n_sum += int(dic.get(k))
                n_list.append(n_sum)
                n_sum = 0
    for i in n_list:
        n_sum_value += (i * (n_list.index(i)+1))
    t2 = time.time()
    print(t2-t1)
    return n_sum_value

def abundant():
    import time
    t1 = time.time()
    abundance = []
    abun_sums = []
    for i in range(1, 100):
        if sum(factors(i) - {i}) > i:
            abundance.append(i)
    for i in range(1, 100):
        for j in abundance:
            for k in abundance:
                if i != j + k:
                    abun_sums.append(i)
    for i in abun_sums:
        while abun_sums.count(i) > 1:
            abun_sums.remove(i)
    t2 = time.time()
    print (t2-t1)
    return abun_sums

def perfect(d):
    import time
    t1 = time.time()
    perfect = []    
    for i in range(1,d):
        if sum(factors(i) - {i}) == i:
            perfect.append(i)
    t2 = time.time()
    print(t2-t1)
    return perfect
    
def abund(d):
    import time
    t1 = time.time()
    abun = []    
    for i in range(1,d):
        if sum(factors(i) - {i}) > i:
            abun.append(i)
    t2 = time.time()
    print(t2-t1)
    return abun

def nonabun_sum(d):
    import time
    t1 = time.time()
    abun = abund(d)
    non_abun = []
    ab = []
    shit = list(set(range(1,d)) - set(abun))
    for i in shit:
        for j in abun:
            for k in abun:
                if j < i and k <= j:
                    if i == j + k:
                        ab.append(i)
    non_abun = list(set(range(1,d)) - set(ab))
    t2 = time.time()
    print(t2-t1)
    return set(ab)

def distinct_powers():
    l = []
    for i in range(2,101):
        for j in range(2,101):
            l.append(i**j)
            l.append(j**i)
    return len(set(l))

def fifth_power_digit():
##    powers = [i**5 (for i in range(1,10))]
    l = []
    sums = 0
    count = 0
    s = 0
    for i in range(4000,200000):
        l = list(str(i))
        for j in l:
            sums += int(j)**5
        if sums == i:
            sums = 0
            l.clear()
            count += 1
            s += i
            print (i)
        else:
            sums = 0
            l.clear()
    return count, s

def coin_sums():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    a, b, c, d, e, f, g, h = 1, 1, 1, 1, 1, 1, 1, 1
    while a < 201 and  b < 201 and c < 201 and d < 201 and e < 201 and f < 201 and  g < 201 and h < 201:
        if a * 1 + b * 2 + c * 5 + d * 10 + e * 20 + f * 50 + g * 100 + h * 200 == 200:
            count += 1
            print (a, b, c, d, e, f, g, h)
            print (count)
        
def pandigital(m,n):
    import time
    t1 = time.time()
    k = 0
    a = {}
    l = []
    b = []
    c = 0
    for i in range(0,100):
        for j in range(m,n):
            if i != j and i < j:
                k = i * j
                string = str(i) + str(j) + str(k)
                a = set(string)
                if len(string) == 9 and len(a) == 9:
                    l.append(k)
                    c += k
    t2 = time.time()
    print (t2-t1)
    return len(l), c, l

def kuchhni():
    return 11140 + circular_primes(120000,130000) + circular_primes(130000,140000) + circular_primes(140000,150000) + circular_primes(150000,160000) + circular_primes(160000,170000) + circular_primes(170000,180000) + circular_primes(180000,190000) + circular_primes(190000,200000)

def digit_factorials():
    l = []
    sums = 0
    count = []
    s = 0
    for i in range(0,100000):
        l = list(str(i))
        for j in l:
            sums += factorial(int(j))
        if i != sums:
            sums = 0                
        else:
            count.append(sums)
            s += sums
    return s, count


def circular_primes(m,n):
    import time
    import itertools as it
    t1 = time.time()
    l = primes(m,n)
    a = []
    b = ''
    c = []
    d = {}
    string = []
    for i in l:
        if isprime(i) == True:
            string = list(str(i))
            a = list(it.permutations(string))
            for j in a:
                b = ''.join(j)
                if isprime(int(b)) == True and int(b) != i:
                    c.append(i)
            if len(str(i)) == 1 or len(set(str(i))) == 1:
                c.append(i)           
    d = set(c)
    t2 = time.time()
    print(t2-t1)
    return len(d)

def is_palindrome(x):
    dec = str(x)
    pal = list(dec)
    l = []
    r = []
    m = []

    for j in range(0,len(pal)//2):
        l.append(pal[j])
    for k in range(len(pal)//2, len(pal)):
        r.append(pal[k])
    if len(pal)%2 != 0:
        r.remove(r[0])
    l.reverse()
    if l == r:
        return True
    else:
        return False

def palindrome_numbers():
    import time
    t1 = time.time()
    s = 0
    binary = ''
    for i in range(0,1000000):
        if is_palindrome(i) == True:
            binary = str(bin(i))
            baba = binary[2:]
            if baba[0] == '0':
                baba = baba[1:]
            if is_palindrome(baba) == True:
                s += i
    t2 = time.time()
    print(t2-t1)
    return s

def pytha_triplets():
    s = 0
    ans = []
    triples = []
    bum = []
    for i in range(1,400):
        for j in range(200,500):
            for k in range(300,600):
                if i < j < k and i**2 + j**2 == k**2:
                    s = i + j + k
                    triples.append(s)
    for i in triples:
        bum.append([triples.count(i),i])
    return max(bum)

def truncatable_primes():
    l = []
    shit = ''
    string = ''
    a = []
    b = {}
    for i in range(1,1000):
        if isprime(i) == True:
            string = str(i)
            l = list(string)
            l.reverse()
            shit = ''.join(l)
            for j in range(1,len(string)):
                if isprime(int(shit[0:j])) :
                    a.append(i)
    b = set(a)
    return b

def champernowne(x):
    l = []
    champ = ''
    for i in range(1, 400000,1):
        l.append(str(i))
        champ = ''.join(l)
    return champ[x], len(champ)

def coins():
##    200 = 1, 100 = 2, 
    count = 0
    for a in range(0,201):
        for b in range(0,101):
            for c in range(0,41):
                for d in range(0,21):
                    for e in range(0,11):
                        for f in range(0,5):
                            if a + 2*b + 5*c + 10*d + 20*e + 50*f == 100:
                                        count += 1

    return count

def pan_prime():
    
    for i in range(100000000, 999999999):
        numba = str(i)
        a = set(numba)
        if a and {'1','2','3','4','5','6','7','8','9'} == a and isprime(i) == True:
            return i

def prime_digit_replacements():
    for x in range(56000, 57000):
##        if isprime(x):
            num = str(x)
            array = []
            for i in range(0, len(str(x))-1):
##                for j in range(1, len(str(x))):
                    for k in range(1, 10):
    ##                    if i == 0 and k == 0:
    ##                        break
                        new = num.replace(num[i],str(k))
                        new = num.replace(num[i+1],str(k))
                        if isprime(int(new)):
                            array.append(new)
                            
            if len(array) == 7:
                return num, array
