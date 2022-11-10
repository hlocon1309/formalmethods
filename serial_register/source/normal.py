import sys
from serial_reg import serial_reg

if __name__ == "__main__":
    if len(sys.argv) == 4:
        res = serial_reg(sys.argv[1], sys.argv[2], sys.argv[3])
        print("Verification: ", res)
    else:
        print("Too few arguments")