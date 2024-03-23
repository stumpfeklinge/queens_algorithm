def try_fn(i, q):
    j = 0
    while j < 8 and not(q):
        j += 1
        q = False

        if a[j-1] and b[i+j-2] and c[i-j+7]:
            x[i-1] = j
            a[j-1] = False
            b[i+j-2] = False
            c[i-j+7] = False
            if i < 8:
                try_fn(i+1, q)
                if not(q):
                    a[j-1] = True
                    b[i+j-2] = True
                    c[i-j+7] = True
            else:
                q = True
        if q == True:
            print(x)
            break

q = False
a = [True] * 8
b = [True] * 15
c = [True] * 15
x = [0] * 8

try_fn(1, q)
