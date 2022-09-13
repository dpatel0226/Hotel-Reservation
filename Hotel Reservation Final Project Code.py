import json
def readjson():
    with open('booking.json') as f:
        data = json.load(f)
        f.close()
    return data

def get_data(data,name):
    for key in data['hotel']:
        room = data['hotel'][key]
        if room['name'] == name:
            return key
    return None

def set_data(data,name,email,num,type):
    for room in data:
        info = data[room]
        if info['type'] == type:
            if info['name'] == "":
                info['name'] = name
                info['email'] = email
                info['phone'] = num
                return data
    return None

print("Hello! Welcome to The Pier Hotel! Are you here for a reservation or for booking a reservation?")
while True:
    guest = input("> ")
    if guest == "reservation":
        name = input("Please provide your name so I can look up your reservation : ")
        data = readjson()
        
        info = get_data(data,name)
        
        if info == None:
            print("Sorry! You have no reservation.")
        else:
            print(f"You booked a {data['hotel'][info]['type']} room. Your room number is {info}. Here are you keys. Thankyou for choosing The Pier Hotel!")
        break
    elif guest == "booking":
        name = input("Please Enter your name : ")
        email = input("Please Enter your email : ")
        phone = input("Please Enter your phone : ")
        print("Which room would you like to book?\n1) Double Queen\n2) Presidential Suite\n3) King Suite")
        room = ""
        while True:
            type = input("> ")
            if type == "1":
                room = "double queen"
                break
            elif type == "2":
                room = "presidential suites"
                break
            elif type == "3":
                room = "king suites"
                break
            else: 
                print("Invalid option!")

        data = readjson()  
        print(data)
        info = set_data(data['hotel'],name,email,phone,room)
        
        if info == None:
            print("Sorry! On this type all rooms are booked.")
        else:
            my_dict = dict()
            my_dict["hotel"] = info

            json_object = json.dumps(my_dict, indent = 4)
            # Writing to sample.json
            with open("booking.json", "w") as outfile:
                outfile.write(json_object)
                outfile.close()
            print("Room Booked!")
        break
    else:
        print("Invalid Input!!!")