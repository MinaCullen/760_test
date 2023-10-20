from tools import train
import sys
import os

sys.argv = ["train.py", "wsod/configs/wsod/wsddn_faster_rcnn_r50_argoverse.py"]
train.main()