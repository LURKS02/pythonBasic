
# function ===========================
def func():
    print("function")
    return
func()

x = 0
def func2(k):
    k = k + 1
func2(x)
print(x)


# class ==============================
class Classex:
    num = 0

    def fnc(self):
        self.num = 10

cls = Classex()
cls.num = 1
print(cls.num)
cls.fnc()
print(cls.num)



