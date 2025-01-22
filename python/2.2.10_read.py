from rc522 import RC522

rc = RC522()
rc.Pcd_start()
print("Reading...Please place the card...")


try:
    message = rc.read(2)
    print("Successfully retrieved data block:", message)
    input("Press enter to exit...")
except KeyboardInterrupt:
    print("Exiting...")