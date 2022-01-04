def expanded_form(a):
    a=str(a)
    expanded_blank=[]
    print(a)
    for index,item in enumerate(reversed(a)):
        expanded_blank.append(item+('0'*index))
        final='+'.join(reversed(expanded_blank))
    print(final)
number=(input("enter the number "))
expanded_form(number)