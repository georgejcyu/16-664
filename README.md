To run the code, first clone yolov5 by typing in a google colab file:
  !git clone https://github.com/ultralytics/yolov5  # clone
  %cd yolov5
  %pip install -qr requirements.txt  # install

  import torch
  import utils
  display = utils.notebook_init()  # checks

Begin by training yolov5s using the given cars.yaml, which contains the custom labels and images:
  !python train.py --img 640 --epochs 3 --data cars.yaml --weights yolov5s.pt
  
Then, use the best.pt to run on test data:
  !python detect.py --data cars.yaml --save-txt --weights best.pt
  
Finally, run myfile.py to get the submission.csv

