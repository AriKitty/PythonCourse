def spam1():

    def spam2():

        def spam3():
            z = " even" + y
            print(f"In spam3, locals are {locals()}")
            return z

        y = " more " + x  # Y must exist before spam3() is called.
        y += spam3()  # Do not combine.
        print(f"In spam2, locals are {locals()}")
        return y

    x = "spam"  # X must exist before spam2() is called.
    x += spam2()  # Do not combine.
    print(f"In spam1, locals are {locals()}")
    return x


print(spam1())
print(locals())
print(globals())
