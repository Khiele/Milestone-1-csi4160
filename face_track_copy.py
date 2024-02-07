import cv2
import subprocess
import csv
from datetime import datetime

#detects faces
def detect_faces(image):
    #Load a pre-trained face detector using cv2
    face_cascade_path ="/home/kyle/haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    #Grayscaling the image so that face detection can work
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #Detect faces in the images
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
    return faces
         
#Draws the rectangles around the detected faces
def draw_faces(image, faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

#captures the frame using fswebcam
def capture_frame():
    #Uses fswebcam to capture an image
    capture_command = "fswebcam -r 640x480 --no-banner /tmp/frame.jpg"
    subprocess.run(capture_command, shell=True)

    #Read the captured image
    frame = cv2.imread('/tmp/frame.jpg')
    return frame

#save the data of any faces detected in a csv file
def save_face_data(face_data):
    face_data = []
    filename = "/tmp/face_data.csv"
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)

        for data in face_data:
            timestamp, x, y, w, h = data
            writer.writerow([timestamp, x, y, w, h])

#Main method
def main():
    #create an empty face_data list
    face_data = []

    while True:
        frame = capture_frame()
        faces = detect_faces(frame)
        print(f'Detected faces: {faces}')

        #save face data
        timestamp = datetime.now().strftime("%y-%m-%d %H:%M%S")
        for (x, y, w, h) in faces:
            face_data.append([timestamp, x, y, w, h])

        
        draw_faces(frame, faces)

        cv2.imshow('Face Tracking', frame)

        #save frames with detected faces as an image
        output_path = f'/tmp/frame_with_faces/{timestamp}.jpg'
        cv2.imwrite(output_path, frame)
        print(f'Saved frame with detected faces to {output_path}')

        #save the data as csv file
        save_face_data(face_data)

        #break the loop is 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #Stop the capture and close the window
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
