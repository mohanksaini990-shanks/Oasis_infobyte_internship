import time
mt=3605
#mt=int(input('Enter time :'))
for i in range(mt,0,-1):
 s=i%60
 m=int(i/60)%60
 h=int(i/3600)
 print(f'{h:02}:{m:02}:{s:02}')
 time.sleep(1)
print(f'time up')