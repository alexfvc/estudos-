import qrcode

img = qrcode.make('https://www.instagram.com/lilalingeriestore/')
print(type(img))
print(img.size)
# <class 'qrcode.image.pil.PilImage'>
# (330,330)

img.save('qrcode_instalilastore.png')