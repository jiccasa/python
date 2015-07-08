# loop 1

print('What number do you want to start with:')
fnum=int(input())
print('What number do you want to end with:')
enum=int(input())
print('How much do you want your increment to be')
step=int(input())

f=fnum
e=enum
s=step
while f<=e:
    print(f)
    f=f+s
