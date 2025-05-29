t_list = sorted(list(map(float, input().split())))
t = float(input())
if sum(t_list[:-1]) - (3*t) > 1e-6:
    print('impossible')
elif sum(t_list[1:]) - (3*t) <= 1e-6:
    print('infinite')
else:
    print("%0.2f"%(t*3 - t_list[1] - t_list[2]))