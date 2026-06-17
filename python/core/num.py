import numpy as np

image = np.array([[100, 150], [200, 230]])
image2 = np.clip(image + 50, 0, 255)
print(image2)




