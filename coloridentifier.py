import cv2

def color_identifier(frame):
    # Convert the frame from BGR to HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color ranges in HSV
    color_ranges = {
        "Red": [(0, 70, 50), (10, 255, 255)],
        "Green": [(40, 70, 50), (80, 255, 255)],
        "Blue": [(100, 70, 50), (130, 255, 255)]
    }

    identified_color = "Unknown"

    # Iterate over each color range and check if any pixel falls within the range
    for color, (lower, upper) in color_ranges.items():
        mask = cv2.inRange(hsv_frame, lower, upper)
        if cv2.countNonZero(mask) > 0:
            identified_color = color
            break

    return identified_color

# Access the camera using DirectShow backend
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Failed to open the camera.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if frame reading was successful
    if not ret:
        print("Failed to retrieve a frame from the camera.")
        break

    # Apply color identification
    color = color_identifier(frame)

    # Display the color on the frame
    cv2.putText(frame, f"Color: {color}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame
    cv2.imshow("Camera Feed", frame)

    # Check for the 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()
