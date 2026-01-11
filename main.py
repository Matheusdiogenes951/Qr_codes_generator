import qrcode

url = input("Enter the URL to generate QR code: ").strip()

file_path = 'C:\\Users\\mathe\\Desktop\\qr.code.png'

qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image()
img.save(file_path)

print(f"QR code saved to {file_path}")