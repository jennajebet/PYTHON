medical_cause=input("Did you have a medical cause? (Y/N):").strip().upper()
if medical_cause=="Y":
    print("You are allowed")
else:
    presence=int(input("Enter the attendence of the studen:"))
    
    if presence >=75 :
        print("Allowed")
    else:
        print("Not allowed")
    