# Alexus Ear

# The encode function encodes the given 8-digit password by shifting each digit up by three.
def encode(password):
    encoded = ""
    for i in password:
        encoded = encoded + str((int(i) + 3))

    return encoded

# The decode function takes in an encoded password and returns the original password.
def decode(password):
	decoded = ''
	for i in password:
        	decoded = decoded + str((int(i)-3))

	return decoded

if __name__ == '__main__':
    password = ""
    while(True):
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        inputs = int(input("Please enter an option: "))

        if(inputs == 1):
            password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!\n")

        elif(inputs == 2):
            print("The encoded password is " + password + ", and the original password is " + decode(password) + ".\n")


        elif(inputs == 3):
            break


