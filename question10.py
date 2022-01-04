count = {}
word = "MISSISSIPPI"
for i in word:
    if i not in count:
        count[i]=1
    else:
        count[i]=count[i]+1
print(count)
