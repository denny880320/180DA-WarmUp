import cv2
import numpy as np
from sklearn.cluster import KMeans

def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
    
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter("test.mp4", fourcc, 20.0, (1280,720))
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    kM = KMeans(n_clusters=3)
    KM.fit(diff)
    color = np.bincount(KM.labels_).argmax()

    cv2.rectangle(frame1,  (500, 300), (160, 160), color, 2)

    image = cv2.resize(frame1, (1280,720))
    clt.fit(imgage)
    out.write(image)
    cv2.imshow("feed", frame1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
out.release()
