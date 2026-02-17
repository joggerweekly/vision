# cv2.imshow is not supported in colab because it crashes

import matplotlib.pyplot as plt
import cv2
import numpy as np
import urllib.request

def url_to_image(url):
    # Download the image, convert it to a NumPy array, and then read it into OpenCV format
    try:
        url_response = urllib.request.urlopen(url)
        # Read the response and convert to a byte array
        img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
        # Use cv2.imdecode to turn the array into an image
        image = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        return image
    except Exception as e:
        print(f"Error fetching or decoding image: {e}")
        return None

# Example Usage:
image_url = "https://github.com/joggerweekly/vision/blob/main/4.jpg?raw=true" # Replace with a valid image URL
img = url_to_image(image_url)

if img is not None:
    # Display the image in a window
   print(img.shape)
else:
    print("Could not load image. Check the URL and your internet connection.")

figsize = (10, 10)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=figsize)
plt.imshow(img)
plt.title("berry")
plt.show()

