## 🍀 Source Code of the paper
### Title: [YOLO-Based Three-Stage Network for Bangla License Plate Recognition in Dhaka Metropolitan City](https://doi.org/10.1109/ICBSLP.2018.8554668)
#### Authors: Sohaib Abdullah; Md Mahedi Hasan; Sheikh Muhammad Saiful Islam
#### Abstract : 

Real-time Automatic License Plate Recognition (ALPR) is a challenging task in computer vision since license plates in real-world scenarios are difficult to recognize due to the presence of various factors like transparent background, occlusion, existence of multiple plates in an image, variance in illumination and viewing angle, etc. In most of the previous works related to the Bangla license plate, images used for ALPR were captured in ideal conditions due to the unavailability of datasets representing non-ideal conditions. In this paper, we present an approach for real-time Bangla license plate detection that is robust to enormous variations in complex real-world environments. A novel license plate recognition method is also presented making it a complete end-to-end deep learning-based ALPR system. We introduce a dataset by collecting 1, 500 different Bangladeshi vehicular license plate images that are captured manually from the street resembling various real-world scenarios. In this work, we have employed the YOLOv3 algorithm to localize the license plate and recognize the digits successfully. To recognize the character, we have also built a Bangla scene character dataset containing more than 6, 400 characters, with which we have trained a ResNet-20-based deep Convolutional Neural Network (CNN). Our proposed method achieves more than 85% Intersection over Union (IoU) in digit recognition. The ResNet-20-based CNN model achieves 92.7% accuracy in recognizing the Bangla character present on the license plate.


<div align="center"><img src=./Overview.png></div>
Figure: License plate recognition output of our proposed three-stage network. The proposed method correctly classifies digits and characters in Bangla license plates with higher accuracy in different conditions with a few failure instances marked with red.


# Bangla License Plate Dataset 
![ ](https://img.shields.io/badge/Cities-6-green.svg?style=plastic)
![ ](https://img.shields.io/badge/License-CC-green.svg?style=plastic)
![ ](https://img.shields.io/badge/Images-1291-ff69b4.svg?style=plastic)
![ ](https://img.shields.io/badge/Format-.jpg-ff69b4.svg?style=plastic)

To download the dataset visit [here](https://github.com/Mahedi-61/Bangla_License_Plate_Dataset)


## 📚 Feedback
Please you have any questions please send an [email](mailto:mahedi0803@gmail.com)


## ⭐Citation
#### <p align=center>“A picture🖼 is worth a thousand words📜~ ”</p>

If you find this work helpful for your research, please cite it as below:

```bibtex

@INPROCEEDINGS{Abdullah2018License,
  author={Abdullah, Sohaib and Mahedi Hasan, Md and Muhammad Saiful Islam, Sheikh},
  booktitle={2018 International Conference on Bangla Speech and Language Processing (ICBSLP)}, 
  title={YOLO-Based Three-Stage Network for Bangla License Plate Recognition in Dhaka Metropolitan City}, 
  year={2018},
  pages={1-6},
  doi={10.1109/ICBSLP.2018.8554668}
}

```
