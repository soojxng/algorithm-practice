xa, ya, xb, yb, xc, yc = map(int, input().split())

if abs((xa-xb)*(ya-yc)) == abs((xa-xc)*(ya-yb)):
    print(-1.0)
else:
    lengths = [((xa-xb)**2+(ya-yb)**2)**(1/2), ((xa-xc)**2+(ya-yc)**2)**(1/2), ((xb-xc)**2+(yb-yc)**2)**(1/2)]
    perimeters = [(lengths[0]+lengths[1])*2, (lengths[0]+lengths[2])*2, (lengths[1]+lengths[2])*2]
    print(max(perimeters) - min(perimeters))