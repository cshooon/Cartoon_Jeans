import numpy as np
import cv2

# Load image
img = cv2.imread('OMG.jpg')

#chatGPT code
# 이미지를 회색조로 변경합니다.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 가우시안 블러(흐리게) 처리합니다.
gray = cv2.medianBlur(gray, 5)
# 엣지 검출을 수행합니다.
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
# 컬러 이미지로 변경합니다.
color = cv2.bilateralFilter(img, 9, 300, 300)
# 컬러 이미지와 엣지를 합성합니다.
cartoon = cv2.bitwise_and(color, color, mask=edges)
# 결과를 출력합니다.

# Color Quantization Filter
# Reshape the image to a 2D array of pixels and 3 color channels
pixel_vals = img.reshape((-1, 3))
pixel_vals = np.float32(pixel_vals)
# Define the criteria for k-means clustering and apply k-means
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
num_colors = 9
_, labels, centers = cv2.kmeans(pixel_vals, num_colors, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
# Convert the centers to uint8 and apply the colors to the labels
centers = np.uint8(centers)
res = centers[labels.flatten()]
res2 = res.reshape(img.shape)

# pencil sketch filter
# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
# Apply the pencil sketch filter
_, pencil_sketch_img = cv2.pencilSketch(gray_img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)


# bilateral + median + stylization filter
# Apply bilateral filter to smooth the image
smoothed = cv2.bilateralFilter(img, 9, 75, 75)

# Apply median filter to remove noise and preserve edges
median = cv2.medianBlur(smoothed, 5)

# Apply stylization filter to enhance edges and produce a cartoon effect
stylized = cv2.stylization(median, sigma_s=60, sigma_r=0.07)


# Show the original and pencil sketch images side by side
# Display the original and color quantized images
cv2.imshow('Original', img)
cv2.imshow("Chatgpt", cartoon)
cv2.imshow('Color Quantized', res2)
cv2.imshow('Pencil Sketch', pencil_sketch_img)
cv2.imshow('Cartoonizing', stylized)
cv2.waitKey(0)
cv2.destroyAllWindows()
