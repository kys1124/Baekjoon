text = input().split('-')

sm = sum(map(int,(text[0].split('+'))))
for x in text[1:]:
    sm -= sum((map(int,x.split('+'))))
print(sm)
