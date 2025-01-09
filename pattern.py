def decorator1(func):
    def starPatterns():
        print("* * * * *")
        func()
        print("* * * * *")
    return starPatterns()
    
def decorator2(func):
    def modulusPattern():
        print("% % % % %")
        func()
        print("% % % % %")  
    return modulusPattern()
    
 
@decorator1
@decorator2
def main():
    print("Hello Reviewers!")
    
main()
