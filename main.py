import random
results=[0,0,0,0,0,0]
for i in range(1000):
    roll=random.random()
    if roll<1/6:
        results[0]+=1
    elif roll<2/6:
        results[1]+=1
    elif roll<3/6:
        results[2]+=1
    elif roll<4/6:
        results[3]+=1
    elif roll<5/6:
        results[4]+=1
    else:
        results[5]+=1
for i,result in enumerate(results):
    print(f"Face {i+1}: {result} ({result/1000*100:.2f}%)")