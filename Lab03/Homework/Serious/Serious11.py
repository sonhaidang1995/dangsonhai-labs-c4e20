from random import randint
def is_inside(point, shape):
    if shape[0]<point[0]<shape[0]+shape[2] and shape[1]<point[1]<shape[1]+shape[3]:
        return True
    else:
        return False
result = print(is_inside([30,20],[0,0,20,20]))