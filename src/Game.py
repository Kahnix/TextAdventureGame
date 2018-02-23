def Play():
    pass

def Menu():
    print("\033[H\033[J")
        
    print("""
                                                                    
                             88 88                              
            ,d               88 88                              
            88               88 88                              
,adPPYba, MM88MMM ,adPPYYba, 88 88   ,d8  ,adPPYba, 8b,dPPYba,  
I8[    ""   88    ""     `Y8 88 88 ,a8"  a8P_____88 88P'   "Y8  
 `"Y8ba,    88    ,adPPPPP88 88 8888[    8PP""""""" 88          
aa    ]8I   88,   88,    ,88 88 88`"Yba, "8b,   ,aa 88          
`"YbbdP"'   "Y888 `"8bbdP"Y8 88 88   `Y8a `"Ybbd8"' 88          
                                                (The badly made text game)
                                                                
                1) Start
                2) Quit""")
    
    options = [Play,exit]

    Choice = int(input(""))
    while Choice < len(options)-1 and Choice>0:
           Choice=int(input(""))
           options[Choice-1]()
Menu()




