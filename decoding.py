import cv2 as cv2
import numpy as np

with open("received.bin", "rb") as f:
    data = np.frombuffer(f.read(), dtype=np.uint8)

with open("Array_to_be_Xored.bin","rb") as f:
    data1 = np.frombuffer(f.read(), dtype=np.uint8)

mask_bits=np.unpackbits(data1)

output_bits=np.unpackbits(data)
output_bits=output_bits.reshape(1000000,8)
output_image_array=np.zeros((1000000,4),dtype=np.uint8)

def hamming_decode(input,output):
    c1=(input[1])^(input[3])^(input[5])^(input[7])
    c2=(input[2])^(input[3])^(input[5])^(input[7])
    c3=(input[4])^(input[5])^(input[6])^(input[7])
    c4=(input[3])^(input[5])^(input[6])^(input[7])
    num=(4*c3)+(2*c2)+(1*c1)
    input[num]=input[num]^(1)
    output[0]=input[3]
    output[1]=input[5]
    output[2]=input[6]
    output[3]=input[7]

for i in range(output_bits.shape[0]):
    hamming_decode(output_bits[i],output_image_array[i])

output_image_array=output_image_array.flatten()

output_image_array=output_image_array^mask_bits

output_image_array=np.packbits(output_image_array)

image=output_image_array.reshape(500,1000)

cv2.imwrite("outputimage.png", image)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()





    
