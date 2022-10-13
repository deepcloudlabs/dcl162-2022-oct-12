with open("accounts.txt", mode="wt") as accounts:
    accounts.write("iban,balance,status\n")
    accounts.write("TR1,1000,ACTIVE\n")
    accounts.write("TR2,2000,CLOSED\n")
    accounts.write("TR3,3000,BLOCKED\n")
    accounts.write("TR4,4000,ACTIVE")
