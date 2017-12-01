import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


def detect_faces(image):
    """
    Detects faces in an image using Haar cascading filters
    :param image: The image to detect faces in
    :return: Returns a list of rectangles outlining the detected faces
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(10, 10))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return faces


if __name__ == '__main__':
    # Run test
    cam = cv2.VideoCapture(1)
    ret, image = cam.read()
    print(image.shape)
    scaled = cv2.resize(image, (240, int(240. * image.shape[0] / image.shape[1])))
    detect_faces(scaled)
    cv2.imshow("Test", scaled)
    cam.release()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
