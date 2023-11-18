import cv2
import face_recognition
import os
from datetime import datetime

path = './ImagesAttendance'

myList = os.listdir(path)
images = [cv2.imread(os.path.join(path, cl)) for cl in myList]
classNames = [os.path.splitext(cl)[0] for cl in myList]
print(classNames)

attendance = set()
def findEncodings(images):
    encodeList = []
    for idx, img in enumerate(images):
        try:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            face_encodings = face_recognition.face_encodings(img)
            if len(face_encodings) > 0:
                encodeList.append(face_encodings[0])
        except Exception as e:
            print(f"Error processing image {idx}: {e}")
    return encodeList


def markAttendance(name):
    if name not in attendance:
        with open('Attendance.csv', 'a') as f:
            if f.tell() == 0:  # Check if the file is empty
                f.write("Name,Date,Time\n")  # Write the headings
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.write(f'{name},{now.strftime("%Y-%m-%d")},{dtString}\n')
            attendance.add(name)


encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    try:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for faceLoc, encodeFace in zip(facesCurFrame, encodesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = faceDis.argmin()

            name = 'Unknown'
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()

            y1, x2, y2, x1 = [loc * 4 for loc in faceLoc]
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)

        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) == ord('q'):
            break

    except KeyboardInterrupt:
        break

    except Exception as e:
        print('An error occurred:', e)

cap.release()
cv2.destroyAllWindows()
