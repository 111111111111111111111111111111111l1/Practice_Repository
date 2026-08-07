import cv2
import mediapipe as mp
import numpy as np

def analyze_video(input_path, output_path, model):

    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        raise Exception(f"Could not open {input_path}")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    ###output_path = output_path.replace(".mp4", ".avi")

    writer = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps if fps > 0 else 30,
        (width, height)
    )
    if not writer.isOpened():
        raise Exception(f"Could not create output video: {output_path}")

    pose = mp.solutions.pose.Pose()

    good_frames = 0
    total_frames = 0

    while True:

        success, frame = cap.read()

        if not success:
            break

        # --------------------
        # TODO:
        # Convert frame to RGB
        # Run MediaPipe
        # Compute elbow angle
        # Compute knee angle
        # Predict with SVM
        # Draw skeleton
        # Draw feedback
        # --------------------

        writer.write(frame)

    cap.release()
    writer.release()
    writer.release()
    cap.release()

    test = cv2.VideoCapture(output_path)
    print("Can read output:", test.isOpened())

    ret, frame = test.read()
    print("First frame:", ret)

    test.release()
    score = round(100 * good_frames / max(total_frames, 1))

    return {
        "score": score,
        "feedback": "Video analyzed successfully."
    }
    print(width, height, fps)