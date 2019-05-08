
# Emotion Recognition
Emotion recognition in Python using Azure's Cognitive Service

## Description
Emotion recognition is a CLI tool that sends an image from local computer to Azure’s Cognitive Service API and displays the picture with the confidence of each emotion. The image is displayed with squares around detected faces with the confidence level of five emotions,  happiness, sadness, neutral, contempt, and disgust. 


## Dependency
- Python2
- Opencv

## Setup
- Set up the Python2 environment (whatever python2 version you have)
`pyenv install anaconda2-2018.12`
- Install Opencv
`conda install opencv`

## Usage
1. Get the API key from Azure and create a file with the key called `.api_key.txt`
2. To generate an image with the confidence in each emotion and display it
`python main.py <image path>`
3. To exit the program, press any button on your computer. 

## Author
[@keiohtani](https://github.com/keiohtani)

## Reference
- [ms\_emotion.py](https://gist.github.com/JotaroS/ae3a56a91a16aa44635b1e02a7af67cd)

## Licence
This software is released under the MIT License, see LICENSE.
