def create_phone_number(n):
    phone="("
    for i in range (0,3):
        phone+=str(n[i])
    phone+=(') ')
    for i in range (3,6):
        phone = phone+str(n[i])
    phone+=('-')
    for i in range (6,10):
        phone+=str(n[i])
    return(phone)
