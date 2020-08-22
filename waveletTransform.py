# coding:utf-8
import numpy as np
import math

def WaveletTransform(sourceImage, n = 5):
# openCV_array[rows = 2, columns = 3, channel = 3]
#   = [[[r, g, b], [r, g, b], [r, g, b]],
#      [[r, g, b], [r, g, b], [r, g, b]]]

  if not(sourceImage.shape[2]):
    sourceImage = sourceImage[:, :, np.newaxis]
  nChannel = sourceImage.shape[2]

  padding_bottom = math.ceil(sourceImage.shape[0] / pow(2, n)) * pow(2, n) - sourceImage.shape[0]
  padding_right = math.ceil(sourceImage.shape[1] / pow(2, n)) * pow(2, n) - sourceImage.shape[1]

  endBottomArray = sourceImage[sourceImage.shape[0] - 1, :, :]
  endBottomArray = endBottomArray.reshape(1, sourceImage.shape[1], sourceImage.shape[2])
  for i in range(0, padding_bottom):
    sourceImage = np.append(sourceImage, endBottomArray, axis = 0)

  endRightArray = sourceImage[:, sourceImage.shape[1] - 1, :]
  endRightArray = endRightArray.reshape(sourceImage.shape[0], 1, sourceImage.shape[2])
  for i in range(0, padding_right):
    sourceImage = np.append(sourceImage, endRightArray, axis = 1)

  sourceImage = sourceImage.astype(np.float32)
  rows, columns = sourceImage.shape[:2]
  resultImage = sourceImage.copy()
  for i in range(0, n):
    for channel in range(0, nChannel):
      for y in range(0, rows, 2):
        for x in range(0, columns, 2):
          half_y = y >> 1
          half_x = x >> 1
          half_rows = rows >> 1
          half_columns = columns >> 1

          valueIn_00 = sourceImage[y, x, channel]
          valueIn_01 = sourceImage[y, x + 1, channel]
          valueIn_10 = sourceImage[y + 1, x, channel]
          valueIn_11 = sourceImage[y + 1, x + 1, channel]

          valueOut_00 = (valueIn_00 + valueIn_01 + valueIn_10 + valueIn_11) / 4.0
          valueOut_01 = (valueIn_00 + valueIn_01 - valueIn_10 - valueIn_11) / 4.0
          valueOut_10 = (valueIn_00 - valueIn_01 + valueIn_10 - valueIn_11) / 4.0
          valueOut_11 = (valueIn_00 - valueIn_01 - valueIn_10 + valueIn_11) / 4.0

          resultImage[half_y, half_x, channel] = valueOut_00
          resultImage[half_y, half_columns + half_x, channel] = valueOut_01
          resultImage[half_rows + half_y, half_x, channel] = valueOut_10
          resultImage[half_rows + half_y, half_columns + half_x, channel] = valueOut_11

    sourceImage[:rows, :columns] = resultImage[:rows, :columns]
    rows = rows >> 1
    columns = columns >> 1
  return resultImage

def InverseWaveletTransform(sourceImage, n = 5):
  if not(sourceImage.shape[2]):
    sourceImage = sourceImage[:, :, np.newaxis]
  nChannel = sourceImage.shape[2]

  padding_bottom = math.ceil(sourceImage.shape[0] / pow(2, n)) * pow(2, n) - sourceImage.shape[0]
  padding_right = math.ceil(sourceImage.shape[1] / pow(2, n)) * pow(2, n) - sourceImage.shape[1]

  endBottomArray = sourceImage[sourceImage.shape[0] - 1, :, :]
  endBottomArray = endBottomArray.reshape(1, sourceImage.shape[1], sourceImage.shape[2])
  for i in range(0, padding_bottom):
    sourceImage = np.append(sourceImage, endBottomArray, axis = 0)

  endRightArray = sourceImage[:, sourceImage.shape[1] - 1, :]
  endRightArray = endRightArray.reshape(sourceImage.shape[0], 1, sourceImage.shape[2])
  for i in range(0, padding_right):
    sourceImage = np.append(sourceImage, endRightArray, axis = 1)

  sourceImage = sourceImage.astype(np.float32)
  rows, columns = sourceImage.shape[:2]
  rows = int(rows / pow(2, n - 1))
  columns = int(columns / pow(2, n - 1))
  resultImage = sourceImage.copy()
  for i in range(0, n):
    for channel in range(0, nChannel):
      for y in range(0, rows, 2):
        for x in range(0, columns, 2):
          half_y = y >> 1
          half_x = x >> 1
          half_rows = rows >> 1
          half_columns = columns >> 1

          valueIn_00 = sourceImage[half_y, half_x, channel]
          valueIn_01 = sourceImage[half_y, half_columns + half_x, channel]
          valueIn_10 = sourceImage[half_rows + half_y, half_x, channel]
          valueIn_11 = sourceImage[half_rows + half_y, half_columns + half_x, channel]

          valueOut_00 = (valueIn_00 + valueIn_01 + valueIn_10 + valueIn_11)
          valueOut_01 = (valueIn_00 + valueIn_01 - valueIn_10 - valueIn_11)
          valueOut_10 = (valueIn_00 - valueIn_01 + valueIn_10 - valueIn_11)
          valueOut_11 = (valueIn_00 - valueIn_01 - valueIn_10 + valueIn_11)

          resultImage[y, x, channel] = valueOut_00
          resultImage[y, x + 1, channel] = valueOut_01
          resultImage[y + 1, x, channel] = valueOut_10
          resultImage[y + 1, x + 1, channel] = valueOut_11

    sourceImage[:rows, :columns] = resultImage[:rows, :columns]
    rows = rows << 1
    columns = columns << 1
  return resultImage
  
