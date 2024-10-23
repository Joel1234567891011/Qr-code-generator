import qrcode
qr=qrcode.QRCode(
                version=5,
                box_size=5,
                border=2)

name=input("enter your name:")

age=int(input("enter your age:"))

email=input("enter your email:")
mobile=int(input("enter your mobile:"))
data={"Name":name, "Age":age, "Email":email, "Mobile":mobile}

qr.add_data(data)

qr.make(fit=True)

img=qr.make_image()

img.save("mydetails_in_qr.png")

img.show()