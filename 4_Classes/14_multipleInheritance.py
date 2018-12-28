# Now we will see the order in which the classes are accessed in case of multiple inheritance
# Python uses DEPTH FIRST SEARCH (DFS) algorithm for lookups


class A(object):
    def doThis(self):
        print('Doing this in A')


class B(A):
    pass


class C(object):
    def doThis(self):
        print('Doing this in C')

# If class C was also being derived from A then the lookup order would be D,B,C,A


class D(B, A):
    pass


if __name__ == '__main__':
    dObj = D()
    dObj.doThis()  # A method gets called because order for lookup is D,B,A,C this is shown by function mro

    print(D.mro())  # mro is Method Resolution Order and it is the set of rules that construct the linearization
