def feb(n):
     n1, n2 = 0, 1
     for i in range(n):
         print(n1)
         n3 = n1+n2
         n1 = n2
         n2 = n3


def fac(n):
    fact = n
    for i in range(n):
        if i != 0:
            fact *= i
    print(fact)

def check():
    #app =  {"et":12, "tr":45,}
    app = [12,23,34]
    for i,v in enumerate(app):
        print(f"{i}-{v}")

def palind(n):
    print(a)
    tup = tuple(str(n))
    length = len(tup)
    rever_arr = []
    for ind, value in enumerate(tup):
        ind = (length-1)-ind
        if ind<length:
            rever_arr.append(tup[ind])
    rev_str = ""
    for i in rever_arr:
        rev_str += i
    if int(n) == int(rev_str):
        print("Palindrome")
    else:
        print("Not Palindrome")

def app(stri):
    st1=""
    te = st1.join(stri)
    print(te)

def findfibo(n):
    n1, n2 = 0, 1
    arr=[]
    for i in range(n):
        arr.append(n1)
        n3=n1+n2
        n1=n2
        n2=n3
    if n in arr:
        print("It's a fibo num")
    else:
        print("Not a fibo num")
    print(arr)

def checkprime(n):
    if n <= 1:
        return "Not prime"
    else:
        for i in range(2,n):
            if n % i == 0:
                return "Not Prime"

        return "Prime"


def split(word):
     res = []
     res[:] = str(word)
     print(res)


def tes(n):
    lis = list(str(n))
    new_str = ""
    for i,v in enumerate(lis, start=1):
        ind = lis[-i]
        new_str += ind
    print(type(new_str))
    if int(new_str) == n:
        print("pali")
    print("Nope")
    print(new_str )

#a,d,n
#a,a+d,a+2d, a+3d
def arith_series(a,d,n):
    sum = 0
    for i in range(n):
        sum += a+(i*d)
    print(sum)


#arith_series(a=2.5,d=1.5,n=20)

def calc(fun):
    def inner(*args, **kwargs):
        print(fun(*args))
    return inner

lis = [2,4,6,8]
list_2 = [2,3,4]
#print(list(map(calc, lis)))
te = map(lambda x,y:x+y, lis,list_2)
#print(list(te))
@calc
def fun(n):
    return n+n
fun(10)
