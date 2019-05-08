# reference: http://jotarout.hatenablog.com/

# Calling Emotion APIs is
# restricted to 20 transactions per minute
# and 30,000 transactions per month.
# 20 transactions per 60 seconds
# 1 transaction per 3 seconds

# python ms_emotion.py tani.jpg

import httplib
import os
import sys
import cv2
import json

def get_emotion(file_path, headers):
    try:
        conn = httplib.HTTPSConnection('centralus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?returnFaceId=true&returnFaceLandmarks=false&returnFaceAttributes=emotion&recognitionModel=recognition_01&returnRecognitionModel=false",
                     open(file_path, 'rb'), headers)
        response = conn.getresponse()
        data = response.read()
        conn.close()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
        print(e.message)

def detect_expression(data,img):
    print(data)
    font = cv2.FONT_HERSHEY_PLAIN
    font_size = 1
    data = json.loads(data)
    for face in data:
        f_rec  =  face['faceRectangle']
        width  =  f_rec['width']
        height =  f_rec['height']
        left   =  f_rec['left']
        top    =  f_rec['top']
        emotion  =  face['faceAttributes']['emotion']
        emotion = sorted(emotion.items(), key=lambda x:x[1],reverse = True)
        cv2.rectangle(img,(left,top),(left+width,top+height),(130,130,130),2)
        cv2.rectangle(img,(left+width,top),(left+width+150,top+50),(130,130,130),-1)

        for i in range(0,5):
            val = round(emotion[i][1],3)
            emo = emotion[i][0]
            cv2.rectangle(img,(left+width,top+10*i),(left+width+int(val*150),top+10*(i+1)),(180,180,180),-1)
            cv2.putText(img, emo+" "+str(val),(left+width,top+10*(i+1)),font, font_size,(255,255,255),1)
    return img

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage: # python %s /path/to/image' % sys.argv[0]
        quit()

    with open('.api_key.txt', 'r') as f:
        key = f.read().rstrip('\n')

    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': key,
    }

    data = get_emotion(sys.argv[1], headers)
    img = cv2.imread(sys.argv[1],-1)
    img = detect_expression(data, img)
    
    cv2.imshow('image', img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
