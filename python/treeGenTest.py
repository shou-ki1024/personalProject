name = input("input your ahh name...")
size_name = len(name)
print("your name is", size_name, "chars long")
print("your initial name is", name[0])
print(f"niggas{name}")


print(f"""█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝
                                                                              
                                                                              
                                                                              
                    ████████╗██████╗ ███████╗███████╗                         
                    ╚══██╔══╝██╔══██╗██╔════╝██╔════╝                         
                       ██║   ██████╔╝█████╗  █████╗                           
                       ██║   ██╔══██╗██╔══╝  ██╔══╝                           
                       ██║   ██║  ██║███████╗███████╗                         
                       ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝                         
                                                                              
 ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗  
██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗ 
██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝ 
██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗ 
╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║ 
 ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝ 
                                                                              
                                                                              
                                                                              
█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗█████╗
╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝╚════╝""")


#start of tree gen
length = int(input("write the initial length: "))

#var
#drawVar
star = "*"
candle = r"/\ "
log_round = "||"
thin_log = "|"

#elseVar
decrease = int(length/2 - 1)
much_loop_round = int(length/2)
loop = much_loop_round
space = " "

#function
def batang_per(grow):
    for batang in range(grow):
        print(f"{space * (much_loop_round - 2)}{thin_log}{space}{thin_log}")
def tumbuhkan_batang():
    if length <= 10:
        print(f"{space * (much_loop_round - 1)}{thin_log}")
    elif length <= 30:
        batang_per(2)
    elif length > 30:
        grow = round((length) / 30)
        batang_per(grow + 2)

if (length/2) % 1 == 0:
    print(f"{space * (much_loop_round - 1)}{candle}")
    for leaves in range (much_loop_round):
        print(f"{space * (loop - 1)}{star * (length - decrease * 2)}")
        loop -= 1
        decrease -= 1
    print(f"{space * (much_loop_round - 2)} {log_round}")

elif (length/2) % 1 != 0:
    for leaves in range (much_loop_round):
        print(f"{space * (loop - 1)}{star * (length - loop * 2)}")
        loop -= 1
    tumbuhkan_batang()

