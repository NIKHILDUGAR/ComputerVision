#BY - NIKHIL DUGAR BT17GCS068
import cv2
import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt

for x in range(0,5):
    image = cv2.imread(f'{x}.jpg',0)
    try:
        img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    except:
        img = image  # incase image is already gray scale
    img = cv2.GaussianBlur(img, (5,5),0)
    threshimg =  cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    L=[img,threshimg]
    gaussianlist = [threshimg]
    lower=threshimg

    for i in range(2):
        lower = cv2.pyrDown(lower)
        gaussianlist.append(lower)
    laplacian_top = gaussianlist[-1]
    laplaclist = [laplacian_top]
    for i in range(1, 0, -1):
        size = (gaussianlist[i - 1].shape[1], gaussianlist[i - 1].shape[0])
        gaussian_exp = cv2.pyrUp(gaussianlist[i], dstsize=size)
        lapla = cv2.subtract(gaussianlist[i - 1], gaussian_exp)
        laplaclist.append(lapla)
    L+=laplaclist
    moment=[]
    for i in range(len(laplaclist)):
        edges = cv2.Canny(laplaclist[i], 100, 200)
        L.append(edges)
        moment.append(cv2.moments(edges))
    for i in moment[0].keys():
        print(f"moments [{i}] - ", moment[0][i])
    for i in range(len(L)):
        plt.subplot(1,len(L),i+1), plt.imshow(L[i], 'gray')
        plt.xticks([]),plt.yticks([])
    plt.subplot(1,len(L),1).set_title('Original image',fontsize = 6)
    plt.subplot(1, len(L), 2).set_title('Image after thresholding', fontsize=6)
    plt.subplot(1, len(L), 3).set_title('Laplacian pyramid level 1 image', fontsize=6)
    plt.subplot(1, len(L), 4).set_title('Laplacian pyramid level 2 image', fontsize=6)
    plt.subplot(1, len(L), 5).set_title('Edges of Laplacian pyramid level 1 image', fontsize=6)
    plt.subplot(1, len(L), 6).set_title('Edges of Laplacian pyramid level 2 image', fontsize=6)
    plt.show()
