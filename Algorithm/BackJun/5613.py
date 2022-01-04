param1 = int(input())
while(1):
    sign = input()
    if sign == "+":
        param2 = int(input())
        param1 = param1 + param2
        
    elif sign == "-":
        param2 = int(input())
        param1 = param1 - param2
    
    elif sign == "*":
        param2 = int(input())
        param1 = param1 * param2
    
    elif sign == "/":
        param2 = int(input())
        param1 = param1 // param2
        
    elif sign == "=" :
        print(param1)
        break