import face_recognition
import numpy as np
from os import listdir

trainning_files = listdir('./images/trainning')
known_face_encodings = []
known_face_names = []

for filename in trainning_files:
    person_name = filename.split('.')[0]
    person_image = face_recognition.load_image_file("images/trainning/" + filename)
    person_encoding = face_recognition.face_encodings(person_image)[0]
    known_face_names.append(person_name)
    known_face_encodings.append(person_encoding)

unknown_image = face_recognition.load_image_file("images/check/unkown_1.jpeg")
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

persons_located = []

for face_encoding in face_encodings:
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    best_match_index = np.argmin(face_distances)
    if matches[best_match_index]:
        name = known_face_names[best_match_index]

    persons_located.append(name)

print("Who was found in the photo:")
for person in persons_located:
    print(person)
