weather= (1, 0, 0, 0, 1, 1, 0)
rainy= 0
sunny= 0
for i in range(0,7):
    if weather[i]==0:
        rainy+=1
    else:
        sunny+=1
if sunny>rainy:
    print("It's good weather")
else:
    print("It's bad weather")