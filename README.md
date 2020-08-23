## WaveletTransform
- **Simple wavelet transform and inverse wavelet transform program written in Python.**

## Steps

Test script "main.py" uses OpenCV library.

1. Follow the instructions below to install OpenCV.
```bash
sudo python3 -m pip install opencv-python
```
2. Run.
```bash
python3 "path_to_the_main.py" "path_to_the_test1.png" True False 3
```
- **Argument[0] is the path to the main.py.**
- **Argument[1] is the path to the input image file.**
- **Argument[2] is a boolean value indicating whether to run the forward transform.**
- **Argument[3] is a boolean value indicating whether to run the inverse transform.**
- **Argument[4] is the number of times to transform.**

### My Results
- **Original image file.**
<div align="center">
	<img src="https://raw.githubusercontent.com/ImpactCrater/WaveletTransform/master/images/test1.png"/>
</div>
</a>

- **Forward wavelet transformed image.**
<div align="center">
	<img src="https://raw.githubusercontent.com/ImpactCrater/WaveletTransform/master/images/testResultForward.png"/>
</div>
</a>

- **Inverse wavelet transformed image.**
<div align="center">
	<img src="https://raw.githubusercontent.com/ImpactCrater/WaveletTransform/master/images/testResultInverse.png"/>
</div>
</a>
