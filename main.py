import cv2
import mediapipe as mp
from tensorflow.keras.models import load_model
import pyautogui

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    x, y, c = frame.shape

    frame = cv2.flip(frame, 1)
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(framergb)

    gesture = ''
    num_fingers = 0

    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])

            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)

            if len(landmarks) > 0:
                if landmarks[4][0] < landmarks[3][0]:
                    num_fingers += 1
                if landmarks[8][1] < landmarks[6][1]:
                    num_fingers += 1
                if landmarks[12][1] < landmarks[10][1]:
                    num_fingers += 1
                if landmarks[16][1] < landmarks[14][1]:
                    num_fingers += 1
                if landmarks[20][1] < landmarks[18][1]:
                    num_fingers += 1
            if num_fingers == 1:
                cv2.putText(frame, "Accelerate", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2, cv2.LINE_AA)
                pyautogui.keyUp("down")
                pyautogui.keyUp("right")
                pyautogui.keyDown("up")
                pyautogui.keyUp("left")

            elif num_fingers == 2:
                cv2.putText(frame, "Break", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2, cv2.LINE_AA)
                pyautogui.keyUp("up")
                pyautogui.keyDown("down")
                pyautogui.keyUp("right")
                pyautogui.keyUp("left")
            elif num_fingers == 3:
                cv2.putText(frame, "Right", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2, cv2.LINE_AA)
                pyautogui.keyUp("up")
                pyautogui.keyUp("down")
                pyautogui.keyDown("right")
                pyautogui.keyUp("left")
            elif num_fingers == 4:
                cv2.putText(frame, "Left", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2, cv2.LINE_AA)
                pyautogui.keyUp("up")
                pyautogui.keyUp("down")
                pyautogui.keyUp("right")
                pyautogui.keyDown("left")
            elif num_fingers == 5:
                cv2.putText(frame, "Nothing", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2, cv2.LINE_AA)
                pyautogui.keyUp("up")
                pyautogui.keyUp("down")
                pyautogui.keyUp("right")
                pyautogui.keyUp("left")
            else:
                cv2.putText(frame, "Nothing", (10, 50), cv2.FONT_HERSHEY_SIMPLEX,
                            1, (0, 0, 255), 2, cv2.LINE_AA)
                pyautogui.keyUp("up")
                pyautogui.keyUp("down")
                pyautogui.keyUp("right")
                pyautogui.keyUp("left")

    cv2.imshow("TechVidvan", frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
