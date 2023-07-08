import pyqrcode


# String which you want to convert into QR code
string = input("Enter string or link:")



# QR Code Generation
url = pyqrcode.create(string)

# Create and save the png file naming "qrcode.svg"
url.svg("qrcode.svg", scale=10)