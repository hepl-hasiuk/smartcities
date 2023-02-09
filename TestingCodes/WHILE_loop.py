# File : WHILE_loop
# Simple blink program
# https://docs.micropython.org/en/latest/library/machine.Pin.html
#ilya.hasiuk@student.hepl.be
# 9/2/2022

a=0
print('loop start')
while a < 5:
    print(a)
    a=a+1
print("loop end")
    