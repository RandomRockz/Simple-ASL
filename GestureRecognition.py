# Please run this program on Python 3.8.0 64-bit, Later version will not work
# Words you can use - Aunt, I Love You, Luck, Please, Thumbs Down, THumbs Up, and Yellow
# Image can be found in the folder ASL-Images
import cv2
import mediapipe as mp


mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0) 

def recognize_ily_sign(landmarks):
    thumb_tip = landmarks[4]
    middle_tip = landmarks[12]
    index_tip = landmarks[8]
    little_tip = landmarks[20]

    is_ily_sign = (
        thumb_tip.y > index_tip.y and
        thumb_tip.y > little_tip.y and 
        middle_tip.y > index_tip.y and
        middle_tip.y > little_tip.y 
    )

    return is_ily_sign
def recognize_please(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    little_tip = landmarks[20]

    is_please = (
        thumb_tip.y < index_tip.y and
        index_tip.y < middle_tip.y and
        middle_tip.y < ring_tip.y and
        ring_tip.y < little_tip.y and
        middle_tip.x < thumb_tip.x

    )
    return is_please
def recognize_yellow(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    little_tip = landmarks[20]


    is_yellow = (
        thumb_tip.y < index_tip.y and
        little_tip.y < middle_tip.y and
        little_tip.y < ring_tip.y and
        little_tip.y < thumb_tip.y 

    )
    return is_yellow

def recognize_luck(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    little_tip = landmarks[20]

    is_luck = (
        thumb_tip.y > index_tip.y and
        index_tip.y < middle_tip.y and
        middle_tip.y < ring_tip.y and
        ring_tip.y < little_tip.y and
        thumb_tip.y < middle_tip.y


    )
    return is_luck
def recognize_aunt(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    little_tip = landmarks[20]

    is_aunt = (
        thumb_tip.y < index_tip.y and
        thumb_tip.y < middle_tip.y and
        thumb_tip.y < ring_tip.y and
        thumb_tip.y < little_tip.y and
        little_tip.y > index_tip.y and
        index_tip.x < middle_tip.x



    )
    return is_aunt
def recognize_thumb_up(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    little_tip = landmarks[20]

    is_thumb_up = (
        thumb_tip.y < index_tip.y and
        index_tip.y < middle_tip.y and
        middle_tip.y < ring_tip.y and
        ring_tip.y < little_tip.y and
        middle_tip.x > thumb_tip.x and
        index_tip.x > middle_tip.x
    )
    return is_thumb_up
def recognize_thumb_down(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    little_tip = landmarks[20]

    is_thumb_down = (
        thumb_tip.y > index_tip.y and
        index_tip.y > middle_tip.y and
        middle_tip.y > ring_tip.y and
        ring_tip.y > little_tip.y 
        
    )
    return is_thumb_down
def recognize_h(landmarks):
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    middle_tip = landmarks[12]
    ring_tip = landmarks[16]
    little_tip = landmarks[20]

    is_h = (
        thumb_tip.y < middle_tip.y and
        thumb_tip.y > index_tip.y and
        index_tip.y < middle_tip.y and
        ring_tip.y < little_tip.y
    )
    return is_h
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame = cv2.flip(frame, 1) 
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            landmarks = []
            for point in hand_landmarks.landmark:
                landmarks.append(point)

            ily_sign = recognize_ily_sign(landmarks)
            please=recognize_please(landmarks)
            luck=recognize_luck(landmarks)
            yellow=recognize_yellow(landmarks)
            aunt=recognize_aunt(landmarks)
            thumb_up=recognize_thumb_up(landmarks)
            thumb_down=recognize_thumb_down(landmarks)
            h=recognize_h(landmarks)
            if ily_sign:
                cv2.putText(frame, "I Love You", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            if thumb_up:
                cv2.putText(frame, "Thumbs Up", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            if thumb_down:
                cv2.putText(frame, "Thumbs Down", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            if aunt:
                cv2.putText(frame, "Aunt", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)                    
            if please:
                cv2.putText(frame, "Please", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)               
            if luck:
                cv2.putText(frame, "Luck", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)               
            if yellow:
                cv2.putText(frame, "Yellow", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
            #if h:
            #    cv2.putText(frame, "H", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

                
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow("Gesture Recognition", frame)

    if cv2.waitKey(1) & 0xFF == 27:  
        break


cap.release()
cv2.destroyAllWindows()
