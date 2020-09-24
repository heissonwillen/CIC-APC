# age = lambda d: f'{int(d)//360} {(int(d)%360)//30} {(int(d)%360)%30}'
#
# [print(age(i)) for i in input().split()]

[print(int(d)//360, (int(d)%360)//30, (int(d)%360)%30) for d in input().split()]
