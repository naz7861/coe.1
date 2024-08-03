import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image_path = 'path/to/your/natural_landscape_image.jpg'
image = cv2.imread(image_path)

# Split the image into its BGR (Blue, Green, Red) channels
blue_channel, green_channel, red_channel = cv2.split(image)

# Calculate the histograms for each channel
histogram_blue = cv2.calcHist([blue_channel], [0], None, [256], [0, 256])
histogram_green = cv2.calcHist([green_channel], [0], None, [256], [0, 256])
histogram_red = cv2.calcHist([red_channel], [0], None, [256], [0, 256])

# Plotting the histograms
plt.figure(figsize=(10, 5))
plt.title('Color Channel Histograms')
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')

plt.plot(histogram_blue, color='blue', label='Blue Channel')
plt.plot(histogram_green, color='green', label='Green Channel')
plt.plot(histogram_red, color='red', label='Red Channel')

plt.legend()
plt.show()
