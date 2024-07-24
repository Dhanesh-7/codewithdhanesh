import cv2
import imutils
import os

# Initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Path to the image
image_path = "E:\photos\ped1.jpeg"  

# Escaped backslashes

# Check if the file exists
if not os.path.exists(image_path):
    print(f"Error: The file at path {image_path} does not exist.")
else:
    # Read the image
    image = cv2.imread(image_path)

    # Check if the image was successfully loaded
    if image is None:
        print(f"Error: Could not load image at {image_path}")
    else:
        # Resize the image
        image = imutils.resize(image, width=min(400, image.shape[1]))

        # Detect all the regions in the image that have pedestrians inside them
        (regions, _) = hog.detectMultiScale(image, 
                                            winStride=(4, 4),
                                            padding=(4, 4),
                                            scale=1.05)

        # Draw the regions in the image
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # Show the output image
        cv2.imshow("Image", image)
        cv2.waitKey(0)

        # Destroy all OpenCV windows
        cv2.destroyAllWindows()
