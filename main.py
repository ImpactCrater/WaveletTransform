import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import plotter
import wavelet_transform as WT

def ImageProcessing(imagePath):
  print("Now loading the image...")
  print("Image Path = {0}".format(imagePath))
  img = cv2.imread(imagePath)

  originalSize = img.shape[:2]
  resultImage = WT.WaveletTransform(img, n = 4)
  resultImage = WT.InverseWaveletTransform(resultImage, n = 4)
  resultImage = resultImage[:originalSize[0], :originalSize[1], :]

  resultImage = resultImage.clip(0,255)
  resultImage = np.uint8(resultImage)

  plt = plotter.Plotter(plot = False, num_images=1, out_filename="testResult.png")
  plt.save(resultImage)


def main():
  try:
    ImageProcessing(sys.argv[1])
  except Exception as e:
    print(e)


if __name__ == "__main__":
  main()
