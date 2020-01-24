# Gravious.inc

### Licence plate detection using Yolo :
In order to detect licence we will use Yolo ( You Only Look Once ) deep learning object detection architecture based on convolution neural networks.

Yolo v1 : Paper [link](https://arxiv.org/pdf/1506.02640.pdf).

Yolo v2 : Paper [link](https://arxiv.org/pdf/1612.08242.pdf).

Yolo v3 : Paper [link](https://arxiv.org/pdf/1804.02767.pdf).

Yolo is a single network trained end to end to perform a regression task predicting both object bounding box and object class.
This network is extremely fast, it processes images in real-time at 45 frames per second. A smaller version of the network, tiny YOLO, processes an astounding 155 frames per second.

You will find more information about how to train Yolo on your customized dataset in this [Link](https://towardsdatascience.com/automatic-license-plate-detection-recognition-using-deep-learning-624def07eaaf).

There is also other Deep learning object detector that you can use such as Single Shot Detector (SSD) and Faster RCNN.

We used python v3.7.3
install requirement
````
pip install -r req.txt
````
