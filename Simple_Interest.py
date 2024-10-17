
def simple_interest(p,t,r):
    print("The principal is", p)
    print("The time period is", t)
    print("The rate of interest is",r)
    
    SI = (p * t * r)/100
    
    print("The Simple Interest is", SI)
    return SI
    

simple_interest(10, 8, 10)