#NIKHIL DUGAR BT17GCS068
import matplotlib.pyplot as plt
import cv2

for x in range(5):
    print(f"IMAGE-{x}")
    moments = []
    image=cv2.imread(f'{x}.jpg',0)
    try:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except:
        gray=image # incase image is already gray scale
    G = gray.copy()
    gpA=[image]
    gpA.append(G)
    for i in range(2):
        G = cv2.pyrDown(G)
        gpA.append(G)
        edges=cv2.Canny(G, 128, 200)
        moments=(cv2.moments(edges))
        # print(moments) uncommment to see all moments
        print("moments[m00] - ", moments["m00"])
        print("moments[m10] - ", moments["m10"])
        print("moments[m01] - ", moments["m01"])
        print("moments[m20] - ", moments["m20"])
        print("moments[m11] - ", moments["m11"])
        print("moments[m02] - ", moments["m02"])
        print("moments[m21] - ", moments["m21"])
        print("moments[m12] - ", moments["m12"])
        gpA.append(edges)
    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(gpA[i],'gray')
        plt.xticks([]),plt.yticks([])
    print(moments)
    #first image is original, 2nd image gray ,3rd is pyramid 1 ,4th is edge of pyramid 1 output,5th is pyramid 2 , 6 th is edge of pyramid 2
    plt.show()
