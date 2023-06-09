import cv2
import numpy as np

# Function to calculate the distance between two circles
def calculate_distance(circle1, circle2):
    x1, y1, r1 = circle1
    x2, y2, r2 = circle2
    distance = np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Function to track a single circle in the frame
def track_circle(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Hough Circle Transform
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 20,
                               param1=55, param2=32, minRadius=200, maxRadius=300)

    # Check if a circle is detected
    if circles is not None:
        # Convert the (x, y) coordinates and radius of the circle to integers
        (x, y, r) = np.round(circles[0, :]).astype("int")[0]

        # If the circle's radius increased, update the information
        if r > track_circle.last_radius:
            track_circle.last_radius = r

        # Draw the circle and its center point on the frame
        cv2.circle(frame, (x, y), r, (0, 255, 0), 4)
        cv2.circle(frame, (x, y), 3, (0, 0, 255), -1)
        # Draw the information about the radius on every frame
        text = f"Baloon Radius: {track_circle.last_radius} px"
        cv2.putText(frame, text, (frame.shape[1] - 500, 1050), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Write the frame to the output video file
    output_video.write(frame)

    # Display the frame
    cv2.imshow("Circle Tracker", frame)
    cv2.waitKey(1)

# Initialize the last detected circle's radius to 0
track_circle.last_radius = 0

# Open the video file
input_video = cv2.VideoCapture("//Users//filipbak//Desktop//Nagranie z ekranu 2023-06-9 o 18.02.35.mov")

# Check if the video file is opened successfully
if not input_video.isOpened():
    print("Error opening video file")
    exit()

# Get the video properties from the input video
width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = input_video.get(cv2.CAP_PROP_FPS)

# Create a VideoWriter object to save the output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))

# Read the video frames until the video ends or manually interrupted
while True:
    # Read a frame from the input video
    ret, frame = input_video.read()

    # If frame is not read successfully, then the video has ended
    if not ret:
        break

    # Track the circle in the current frame
    track_circle(frame)

# Release the input and output video files
input_video.release()
output_video.release()

# Close the OpenCV windows
cv2.destroyAllWindows()

