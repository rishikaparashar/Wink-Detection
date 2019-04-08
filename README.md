# Wink-Detection
Wink Detection in a live video and in the images using opencv and python
In this project there are two programs to detect \winking". In writing the programs I have used all of the high level functionality of OpenCV. The only cascade classifiers that can be used are those provided by OpenCV, as well as those available in the following link:
http://alereimondo.no-ip.org/OpenCV/34.
The cascade classifiers provided by OpenCV can be found in:
https://github.com/opencv/opencv/tree/master/data/haarcascades.
They are also available as part of the OpenCV distribution. If you have a mac, they are most likely
in the following folder:
/ Library /Frameworks/Python . framework/Ve r s ions /3.6/ l i b /python3 . 6 /
s i t e packages / cv2 / data /
On windows they may be in following folders:
C: / opencv/ bui ld / e t c / haar cas cade s
C: / opencv/ s our c e s / data / haar cas cade s
C: / User s /name/AppData/ Local /Programs/Python/Python35/Lib/ s i t e packages / cv2 / data
The input to each program is a folder containing images or a live video feed. The program displays each image, and marks each detected face with a distinct color. It also computes and prints the total number of detections.
