teks = "sigma sedang berjalan kesebuahdermaga hitam#ambatukam#"
teks1 = "A#"
teks2 = "ambatukam is king#"

a = [2, 3, 4]
b = [2, 5, 6] 

def remove(a, b):
    #check a
    for i in a:
        #check b
        if i in b:
            a.remove(i)
    return a, b
print(remove(a, b))



