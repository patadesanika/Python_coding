import time
def DisplayEven(no):
    for i in range(1,no):
        if(i%2==0):
            print("Even number:",i)
def DisplayOdd(no):
    for i in range(1,no):
        if(i%2!=0):
            print("odd number:",i)

def main():
    print("demonstration of serial programming")
    DisplayEven(2000)
    DisplayOdd(2000)
if __name__=="__main__":
    start_time=time.time()
    main()
    end_time=time.time()
    print("excution time is",end_time-start_time)