h,e,m,g,a=90,90,30,90,50
total=h+e+m+g+a
print("total=",total)

per=total/5

print("Percentage=",per)

if per<33:
    print("fail")
elif per>=33 and per<45:
    print("third division")
elif per>=45 and per<60:
    print("Second division")
elif per>=60:
    print("first division")
