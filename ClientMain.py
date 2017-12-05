import io
import socket
import struct
import time
import picamera

soc = socket.socket()
soc.connect(("hostname", 42069))

connection = soc.makefile('wb')
try:
    with picamera.PiCamera() as camera:
        camera.resolution = (240, 368)
        camera.start_preview()
        time.sleep(1)

        stream = io.BytesIO()
        for frame in camera.capture_continuous(stream, 'jpeg'):
            connection.write(struct.pack('<L', stream.tell()))
            connection.flush()
            stream.seek(0)
            connection.write(stream.read())

            stream.seek(0)
            stream.truncate()
    connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    soc.close()