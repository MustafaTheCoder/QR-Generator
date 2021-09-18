# Encoding QR Code
import qrcode
import cv2

img = qrcode.make("https://www.youtube.com/")
img.save("youtubeQR.jpg")

# Decoding QR Code
d = cv2.QRCodeDetector()
val, _, _ = d.detectAndDecode(cv2.imread("youtubeQR.jpg"))
print("Decoded Text: ", val)
