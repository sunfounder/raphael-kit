from rc522 import RC522

rc = RC522()
rc.Pcd_start()
x = input("Please enter the data to be written:")
print("Reading...Please place the card...")
data = [ord(x[i]) for i in range(len(x))]

try:
    rc.write(2,data)
    message = rc.read(2)
    print("Successfully retrieved data block:", message)
    input("Press enter to exit...")
except:
    print("Error")
