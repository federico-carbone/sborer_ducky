s = "https://www.youtube.com/watch?v=dQw4w9WgXcQ\n"

m = "abcdefghijklmnopqrstuvwxyz1234567890\nù\b\t -ù[]\\#;'ù,.ùù"
M = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!\"£$%&/()=ùùùùù?*\{\}|~ù\":;ùù"

for c in s:
    if c in m:
        print("\t{", "0,0,{0},0,0,0,0,0".format(hex(m.index(c)+4)), "},", sep="")
    elif c in M:
        print("\t{", "0x2,0,{0},0,0,0,0,0".format(hex(M.index(c)+4)), "},", sep="")
    else:
        print("error on character {0}".format(c))