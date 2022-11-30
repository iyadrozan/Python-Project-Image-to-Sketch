import cv2

# Read The image in RGB format
img = cv2.imread('dummy.jpg')

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Invert the grayscale image
inverted_img = 255-gray_img

# Create the pencil sketch
blurr = cv2.GaussianBlur(inverted_img,(25,25),0)
inverted_blurr= 255-blurr
pencil_sketch = cv2.divide(gray_img,inverted_blurr,scale=256.0)
# Show Image
cv2.imshow("original image",img)
cv2.imshow("Sketch",pencil_sketch)
cv2.waitKey(0)