
def hi(name):
    print("Hello,{n}! Welcome to Hwindy's test aplication.".format(n = name))

def main():
    name = input("Please input your name")
    hi(name)

if __name__ == '__main__':
    main()
