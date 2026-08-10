teks = "sigma sedang berjalan kesebuahdermaga hitam#ambatukam#"
teks1 = "A#"
teks2 = "ambatukam is king#"
a = ""

def read(teks):
    current = ""
    kata = 0
    for i in range(len(teks)):
        a = teks[i]
        if " " in a and current != " ":
            print("{a} mengandung spasi")
            kata += 1
        elif a == "#":
            if current != " " and current != "#":
                kata += 1
        current = a
    print(f"kata {kata}")
read(teks2)
