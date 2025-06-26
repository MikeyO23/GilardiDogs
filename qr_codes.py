import qrcode

# URL to embed
url = "https://gilardi-hotdogs-chicago.netlify.app/"

# Create QR code instance
qr = qrcode.QRCode(
    version=1,  # size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add the URL
qr.add_data(url)
qr.make(fit=True)

# Create the image
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("gilardi_hotdogs_qr.png")
print("✅ QR code saved as 'gilardi_hotdogs_qr.png'")
# Display the QR code
img.show()
print("📱 Scan the QR code to visit Gilardi Hot Dogs!")