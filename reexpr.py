import re

def main():
    f = open('raven.txt')
    print("========Menu========")
    a=input("Pls press S for search R for replace")
    if a=='s':
        for n in f:                                                #n is variable for iteration and fh is for file
            ma= re.search('Big Data', n)
            if ma:
                print(ma.group())
    elif a=='r':
        for n in f:
            ma= re.search('Big Data', n)
            if ma:
                print(n.replace(ma.group(),'BD'),end=' ')
    else:
        print("Sorry! illegal input")

if __name__ == "__main__": main()
