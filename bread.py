try:  
    fresh=int(input(" enter the fresh oves: "))
    old=int(input(" enter the day old oves: "))
    if((fresh>0) & (old>0)):
        regular_p=185
        print(regular_p)
        fresh=185*fresh
        print(" the fresh loves price is : ",fresh)
        o=185-(0.6*185)
        old=o*old
        print(" the day old loves price is : ",old)
        total=old+fresh
        print(total)
    else:
        print(" enter valid input")
except ValueError:
    print(" enter a valid input")
