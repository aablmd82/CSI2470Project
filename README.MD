# Raspberry Pi facial scanner and notifier

This was created for my Intro to Computer Networks class in the Fall 2017 semester. This purpose of this small project was to detect and capture faces with a Raspberry Pi camera, then email a picture containing the detected face to the owner of the Pi. Because we were using an older Raspberry Pi, we needed the image processing to be done through a server application on a stronger machine. For our demonstration we assumed the Pi and the server machine would be on the same network.
- I wrote <b>ServerLookup.py</b>, which uses Scapy to perform an ARP scan, then attempts to connect to the returned addresses. If a connection is successfully established, the server machine's local IP is returned
