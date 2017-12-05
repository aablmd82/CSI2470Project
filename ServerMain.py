import io
import socket
import struct
import cv2
import numpy
import ImageProcessing
import emailer


def process_image(image):
    faces = ImageProcessing.detect_faces(image)
    print("Processed image.")
    if len(faces) > 0:
        print("Sending email.")
        encoded_img = cv2.imencode(".png", image)[1]
        stream = io.BytesIO()
        stream.write(encoded_img)
        stream.seek(0)
        emailer.sendMail(
            ["brian.semrau@gmail.com"],
            "Faces Detected on Camera",
            "",
            [(stream, "detected_faces.png")])


soc = socket.socket()
soc.bind(('0.0.0.0', 42069))
soc.listen(0)

connection = soc.accept()[0].makefile('rb')
try:
    while True:
        length = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not length:
            break

        stream = io.BytesIO()
        stream.write(connection.read(length))
        stream.seek(0)
        image = cv2.imdecode(numpy.frombuffer(stream.getvalue(), dtype=numpy.uint8), 1)

        process_image(image)
finally:
    connection.close()
    soc.close()
