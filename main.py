import qrcode

print("\033[32mEnter the URL to generate QR code: \033[0m", end="")
url = input().strip()

file_path = 'C:\\Users\\mathe\\Desktop\\qr.code.png'

qr = qrcode.QRCode()
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image()
img.save(file_path)

print(f"\033[32mQR code saved to {file_path}\033[0m")