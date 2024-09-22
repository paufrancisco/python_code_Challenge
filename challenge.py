import cv2

# Path to the video file
video_path = "/mnt/data/457284719_8036569953096620_2413166364008838760_n.mp4"

# Open the video file
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Frame counter
frame_number = 0

# Loop to read frames from the video
while True:
    ret, frame = cap.read()

    # If there are no more frames, break the loop
    if not ret:
        break

    # Display the current frame
    cv2.imshow("Frame", frame)

    # Save the current frame as an image file (optional)
    cv2.imwrite(f"frame_{frame_number}.png", frame)

    # Increment the frame counter
    frame_number += 1

    # Wait for a key press; if 'q' is pressed, exit the loop
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
