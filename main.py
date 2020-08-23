import sys
import os
from distutils.util import strtobool
import cv2
import numpy as np

import plotter
import waveletTransform as WT

def ImageProcessing(imagePath, runForward = True, runInverse = False, n = 3):
  print("Now loading the image...")
  img = cv2.imread(imagePath, cv2.IMREAD_UNCHANGED)

  originalSize = img.shape[:2]

  if runForward:
    resultImage = WT.WaveletTransform(img, n)
    img = resultImage.copy()
    cv2.imwrite("./testResultForward.png", resultImage)
    print("Saved as './testResultForward.png' (16bit / ch)")

  if runInverse:
    resultImage = WT.InverseWaveletTransform(img, n)
    resultImage = resultImage[:originalSize[0], :originalSize[1], :]
    cv2.imwrite("./testResultInverse.png", resultImage)
    print("Saved as './testResultInverse.png' (16bit / ch)")

def main():
  try:
    ImageProcessing(sys.argv[1], strtobool(sys.argv[2]), strtobool(sys.argv[3]), int(sys.argv[4]))
  except Exception as e:
    print(e)

if __name__ == "__main__":
  main()
