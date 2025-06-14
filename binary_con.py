import numpy as np
import cv2 as cv2

image = cv2.imread('image.png', cv2.IMREAD_GRAYSCALE) 

resized_image = cv2.resize(image, (1000, 500))  # (width, height)

flattened = resized_image.flatten()  # shape becomes (500000,)

binary_stream = np.unpackbits(flattened)

reshaped_array=binary_stream.reshape(1000000,4)
output_array=np.zeros((1000000,8),dtype=np.uint8)

def hamming(input,output):
   output[7]=input[3]
   output[6]=input[2]
   output[5]=input[1]
   output[3]=input[0]
   output[0]=(input[0])^(input[1])^(input[2])^(input[3])
   output[1]=(input[0])^(input[1])^(input[3])
   output[2]=(input[0])^(input[2])^(input[3])
   output[4]=(input[2])^(input[1])^(input[3])

for i in range(reshaped_array.shape[0]):
   hamming(reshaped_array[i],output_array[i])


packed = np.packbits(output_array.flatten().astype(np.uint8))

with open("output.bin", "wb") as f:
    f.write(packed)










