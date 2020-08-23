import sys
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import plotter
import waveletTransform as WT

def ImageProcessing(imagePath, runForward = True, runInverse = False, n = 3):
  print("Now loading the image...")
  print("Image Path = {0}".format(imagePath))
  img = cv2.imread(imagePath)
  originalSize = img.shape[:2]

  if runForward:
    img = WT.WaveletTransform(img, n)
    resultImage = img.copy()
    resultImage = np.uint8(resultImage)
    plt = plotter.Plotter(plot = False, num_images=1, out_filename="testResultForward.png")
    plt.save(resultImage)
  else:
    print(runForward)

  if runInverse:
    resultImage = WT.InverseWaveletTransform(img, n)
    resultImage = resultImage[:originalSize[0], :originalSize[1], :]
    resultImage = resultImage.clip(0,255)
    resultImage = np.uint8(resultImage)
    plt = plotter.Plotter(plot = False, num_images=1, out_filename="testResultInverse.png")
    plt.save(resultImage)


def main():
  try:
    ImageProcessing(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
  except Exception as e:
    print(e)


if __name__ == "__main__":
  main()
