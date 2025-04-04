list = []
while True:
    print( '  *________________Database_______________*')
    print()
    print("The Indian Copyright Act, 1957, as amended, is the primary legislation governing copyright law in India, ")
    print("                     {Creator : khalid_saif}")
    print('''
    [1] about
    [2] list
    [3] functions
    [4] clear or remove
    [5] Dictionary 
    [6] Exit
    ''')
    i = int(input(">> Select Option: "))
    #coditional statement for display
    if i == 1:
        print('''
        this tool made for fun,
        this tool is free,
        this tool don't return any Error,
        this tool was made for testing,
        this tool is int 💀 harmful like 
        other tool, this tool not parform 
        any harmful operation... 
        
                    {Created by : Khalid}''')
        # while loop2
        while True:
            #cond st.
            print("[0] return ")
            #input2 
            i1 = input(">> Select Option: ")
            #cond st.
            if i1 == "0":
                print()
                break
            else:
                print("            invalid operation...")
                #end of while loop
    elif i == 2:
        print()
        i3 = input("continue for [y/n] ")
        print()
        #cond statement.
        if i3 == "y":
            print("🔵 let's start...")
            print()
            print('''you will be take at list three number...   and you can take number more than three...''')
            i4 = input(">> Enter number :")
            list.append(i4)
            i5 = input("continue for [y/n] ")
            #coditional statements 
            if i5 == "y":
                while True:
                    i6 = input(">> Enter number or quit [Q]:")
                    # loop append 
                    list.append(i6)
                    if i6 == "Q":
                        print("🔴 Output =>", list)
                        break
                    else:
                        pass
            elif i5 == "n":
                print("🔴 Output =>", list)
                print("     ∆___thanks for using this tool___∆")
            else:
                break
         #cond statement         
        elif i3 == "n":
            print()
            print("     ∆___thanks for using this tool___∆")
        else:
            print("                       invalid operation...") 
            print("Try again...!")
    elif i == 3:
        print('''
        [1] reverse 
        [2] sliceing
        [3] indexing 
        [4] Length
        [5] binary code
        [6] Loop
        [0] back
        ''')
        i7 = input(">> Select Option: ")
        if i7 == "1":
            i8 = input("continue for [y/n] ")
            if i8 == "y":
                list.reverse()
                print("🔴Output =>",list)
            elif i8 == "n":
                pass
            else:
                print("               <-----try again----->") 
                #best of luck
        elif i7 ==  "2":
            i9 = input("continue for [y/n] ")
            if i9 == "y":
                print('''if you want to slicing any number of list,  you will be give two value,                 1.starting... and 2.stopping...''')
                print()
                w = input(">> let str or int for slicing : ")
                s = int(input(">> starting value :"))
                sp = int(input(">> stopping value :"))
                
                print("🔴Output => ",w[s : sp])
            else:
                print()    
        elif i7 == "3":
            k = input("continue for [y/n] ")
            #conditional statement.           
            if k == "y":
                print('''if you want to know index of any number,for formula = (count+1)
                ''')
                p = input(">> let str or int for indexing : ")
                p2 = int(input(">> let count : "))
                #print indexing 
                print("🔴Output =>",p[p2])
            else:
                pass 
        elif i7 == "4":
            m = input("continue for [y/n] ")
            #conditional statement.           
            if m == "y":
                m2 = input(">> let str or int for lenth : ")
                print("🔴Output =>",len(m2))
            else:
                print("              <-----try again----->")
                pass
        elif i7 =="5":
            c = input("continue for [y/n] ")
            if c == "y":  
                c1 = int(input(">> let only int for binary code: "))
                print("🔴Output =>",bin(c1))      
            else:
                print("              <-----try again----->")
                pass           
        elif i7 =="6":
            u = input("continue for [y/n] ")
            if u == "y": 
                u2 = 1 
                u1 = input(">> let int or str for loop : ") 
                re = int(input(">> Enter range for loop : "))   
                while u2 <= re:
                    print(u2, u1)
                    u2 += 1
                    if u2 == re:
                        break
            else:
                print("              <-----try again----->")
                pass
    elif i == 4:
        print()
        print("Quit for [Q]")
        y = input(">> Select clear[c] or remove[r] : ")
        if y == "c":    
            print("this can delete all value of list")
            list.clear()
            print("🔴Output =>",list)  
        elif y == "r":
            h = input(">> Enter value : ")
            list.remove(h)
            print("🔴Output => ",list)
        elif y == "Q":
            print("<_____Quit_____>")        
    elif i ==5:
        v = input("continue for [y/n] ")
        if v == "y":
            n = input(">> Enter name : ")
            print("Hello,", n)
            f1 = input("continue for [y/n] ")
            if f1 == "y":
                f2 = input("enter age : ")
                f3 = input("enter country : ")
                f4 = input("enter state : ")
                f5 = input("are you student [y/n] ")
                if f5 == "y":
                    f6 = input("enter class : ")
                else:
                    pass 
                dic = {
                    "name" : n,
                    "age" : f2,
                    "country" : f3,
                    "state" : f4,
                    "Is student" : f5,
                    "class" : f6
                }    
                print("🔴Output =>",dic)       
            else :
                break
                print("________invalid_________") 
        elif v == "n":
            print("_______thanks for using________") 
            dic = {
                "name" : n,
                "age" : f2,
                "country" : f3,
                "state" : f4,
                "Is student" : f5,
                "class" : f6
            }
            print()
            pass
        else:
            pass  
            print()  
    elif i == 6:
        print("            <_______Exit_______>")   
        break     
    else:
        print("?______invalid Operation______?")
                 #completed project
                 

         