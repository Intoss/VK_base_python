st = input()
a = 0
new_st = ""
st = st.lower()
for i in st:
    if i == "!" or i == "%" or i == "#" or i == "@":
        a += 1
    else:
        new_st += i
print(a)
print(new_st)