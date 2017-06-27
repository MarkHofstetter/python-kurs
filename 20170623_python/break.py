for i in range(10):
    for j in range(3):
        if j > 1:
            # break bezieht sich auf die innere Schleife, dh j 
            # continue
            break
        print(i,j)