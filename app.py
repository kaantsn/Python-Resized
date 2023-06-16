import cv2

# Görüntüyü yükleme
image = cv2.imread('resim.jpg')

# Görüntüyü yeniden boyutlandırma
resized_image = cv2.resize(image, (800, 600))

# Yeniden boyutlandırılmış görüntüyü ekranda gösterme
cv2.imshow('Yeniden Boyutlandırılmış Görüntü', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
