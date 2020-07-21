import cv2
from matplotlib import pyplot as plt
for x in range(0,4):
    img = cv2.imread(f'D:\\image.orig\\{x}.jpg',0)
    G = img.copy()
    gpA = [G]
    for i in range(6):
        G = cv2.pyrDown(G)
        gpA.append(G)
    lpA = [gpA[5]]
    for i in range(5, 0, -1):
        GE = cv2.pyrUp(gpA[i])
        L = cv2.subtract(gpA[i - 1], GE)
        lpA.append(L)
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(gpA[i],'gray')
        plt.xticks([]),plt.yticks([])
    plt.show()
    for i in range(4):
        plt.subplot(2,2,i+1),plt.imshow(lpA[i],'gray')
        plt.xticks([]),plt.yticks([])
    plt.show()