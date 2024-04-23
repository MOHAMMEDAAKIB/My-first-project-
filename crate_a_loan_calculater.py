L = int(input("how much loan you get ")) #lone amount 
i = float (0.05) #interast rate
n = int (input("what is the number of pyment")) #number of pyment
# M = monthly payments 
M = L*(i *(1+i)*n)/((1+i)*n -1)
M = round (M,2)
print (f"your monthly payment is {M}")






