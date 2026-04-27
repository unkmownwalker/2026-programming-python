if __name__ == '__main__':
    f=int(input())
    function={}
    for i in range(f):
        str=input().split()
        name=str[1]
        incon=[]
        j=2
        while j<len(str):
            if str[j]=='CALL':
                incon.append(str[j+1])
                j+=2
            else:
                incon.append(str[j])
                j+=1
        function[name]=incon

    n=int(input())
    commands=input().split()
    def move(cmd,x,y):
        if cmd == "U":
                    y += 1
        elif cmd == "D":
                    y -= 1
        elif cmd == "L":
                    x -= 1
        elif cmd == "R":
                    x += 1
        return x,y
    x,y=0,0
    stack=[]
    for command in commands:
        if command!='CALL':
            stack.append(command)
    while stack:
        command=stack.pop()
        if command in function.keys():
            for cmd in function[command]:
                stack.append(cmd)
        else:
              x,y=move(command,x,y)
    print(f"({x}, {y})")
