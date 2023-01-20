import time

from PIL import Image
import numpy as np
import gzip

def sigmoid(weights, layer, bias):
    return 1/(1 + np.exp(-((weights @ layer) + bias)))

def expected_layer(weightsL, aL, expected, aL_1):
    return -weightsL.T @ (aL * (1 - aL) * 2 * (aL - expected)) + aL_1

def biases_change(layer, expected):
    return -layer * (1 - layer) * 2 * (layer - expected)

def weights_change(layer, expected, layer_1):
    return -(layer * (1 - layer) * 2 * (layer - expected)) @ layer_1.T

def max_index(array):
    return array.argmax()

def make_image(array):
    img = Image.new(mode="L",size=(420,420))
    pixels = img.load()
    for row in range(28):
        for col in range(28):
            for k in range(15):
                for l in range(15):
                    pixels[row*15 + k, col*15 + l] = int(255 - array[col][row])
    img.save("number.png")

with gzip.open('Images_labels/t10k-images-idx3-ubyte.gz', 'r') as f:
    image_size = 28
    num_images = 10000
    f.read(16)
    buffer = f.read(image_size * image_size * num_images)
    test_images = np.frombuffer(buffer, dtype=np.uint8).astype(np.float32)
    test_images = test_images.reshape(num_images, image_size, image_size, 1)
with gzip.open('Images_labels/t10k-labels-idx1-ubyte.gz', 'r') as f:
    f.read(8)
    buffer = f.read(10000)
    test_labels = np.frombuffer(buffer, dtype=np.uint8).astype(np.float32)

weights0_1 = np.genfromtxt('CSV_files/weights0_1.csv', delimiter=",").reshape(49, 784)
weights1_2 = np.genfromtxt('CSV_files/weights1_2.csv', delimiter=",").reshape(16, 49)
weights2_f = np.genfromtxt('CSV_files/weights2_f.csv', delimiter=",").reshape(10, 16)

biases0_1 = np.genfromtxt('CSV_files/biases0_1.csv', delimiter=",").reshape(49, 1)
biases1_2 = np.genfromtxt('CSV_files/biases1_2.csv', delimiter=",").reshape(16, 1)
biases2_f = np.genfromtxt('CSV_files/biases2_f.csv', delimiter=",").reshape(10, 1)

def main(number):
    image = test_images[number].reshape(784, 1)
    layer1 = sigmoid(weights0_1, image, biases0_1)
    layer2 = sigmoid(weights1_2, layer1, biases1_2)
    layer_f = sigmoid(weights2_f, layer2, biases2_f)

    guess = max_index(layer_f)
    actual = test_labels[number]
    image = image.astype(np.uint8)
    # img = Image.fromarray(255 - image.reshape(28, 28))
    make_image(image.reshape(28, 28))
    # img.save("number.png")
    return guess, actual

if __name__ == '__main__':
    main(int(time.time()) % 10000)
