
if __name__ == '__main__':

    # for i in range(3):
    #     print(i)
    # if (True):
    #     for i in range(3):
    #         print(i)
    mytuple = ["apple", "banana", "cherry"]
    myit = iter(mytuple)

    for i in myit:
        print(i)
        print(next(myit))

    # print(next(myit))
    # print(next(myit))
    # print(next(myit))