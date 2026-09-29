import cv2
import numpy as np

img = cv2.imread("images.jpeg", cv2.IMREAD_GRAYSCALE)
img = cv2.GaussianBlur(img, (5, 5), 1.4)
#img.show()
cv2.imshow("Canny edges", img)
cv2.waitKey(0)          # waits until you press any key
cv2.destroyAllWindows()

edges = cv2.Canny(img, 50, 150)

cv2.imshow("Canny edges", edges)
cv2.waitKey(0)          # waits until you press any key
cv2.destroyAllWindows()

print(type(edges))
print(edges.shape)
print(edges[0])

edges[edges == 0] = 0 
edges[edges > 0]  = 1

np.savetxt("edges.csv", edges, delimiter= ", ")

#np.save("edges.csv", edges)
