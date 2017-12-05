import ImageProcessing
import emailer
import cv2
import socket
from server import Server


def process_image(image):
    faces = ImageProcessing.detect_faces(image)
    print("Processed image.")
    if len(faces) > 0:
        print("Sending email.")
        _, encoded_img = cv2.imencode(".png", image)
        emailer.sendMail(["brian.semrau@gmail.com"], "Test Server Msg", "This is the content", [encoded_img])


if __name__ == '__main__':
    server = Server()
    server.listen(socket.gethostbyname(socket.gethostname()), 42069)
    print("Server listening.")
    server.retrieve_data(process_image)
