import io
import socket
import struct
import cv2
import numpy
import ImageProcessing
import emailer
import time


email_timeout = 30
time_last_email_sent = 0


def process_image(image):
    global time_last_email_sent

    faces = ImageProcessing.detect_faces(image)
    print("Processed image.")
    if len(faces) > 0:
        current = time.time()
        if current - time_last_email_sent < email_timeout:
            print("Email timeout in effect %.1f." % (current - time_last_email_sent))
        else:
            print("Sending email.")
            send_email(image)
            time_last_email_sent = current


def send_email(image):
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
