import cv2
#read img
img1 =cv2.imread("BadBricks/Silicate/1.jpg")
img2 =cv2.imread("GoodBricks/Kz/1.jpg")
#show
cv2.imshow("silicate brick wall",img1)
cv2.imshow("normal brick",img2)
#edge detector
edges1 = cv2.Canny(img1, 100, 200)
edges2 = cv2.Canny(img2, 100, 200)
#show edge detector results
cv2.imshow("silicate brick wall edges",edges1 )
cv2.imshow("normal brick wall edges",edges2 )

cv2.waitKey(0)
