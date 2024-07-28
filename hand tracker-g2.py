import mediapipe
import cv2
#این کد برای اجرای نهایی پروژه میباشد
my_name = "Fazel-3/8/2024"
def display_name(frame):
    cv2.putText(frame, my_name, (350, 460), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 150), 3)

drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, 
                        min_tracking_confidence=0.7, max_num_hands=2) as hands:

    while True:
        ret, frame = cap.read()
        frame1 = cv2.resize(frame, (640, 480))
        results = hands.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))

        if results.multi_hand_landmarks:
            for idx, handLandmarks in enumerate(results.multi_hand_landmarks):
                handSide = "Left" if results.multi_handedness[idx].classification[0].label == "Right" else "Right"
                handLabel = f"{handSide}-Hand {idx + 1}"
                drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
                cv2.putText(frame1, handLabel, (10, 30*(idx+1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 25, 80), 2)
        
        display_name(frame1)

        cv2.imshow("Frame", frame1)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()