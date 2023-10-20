# Object Detection Models for Autonomous Driving:

## Dataset:
### Argoverse:
* Download Argoverse-HD-Full.zip from https://drive.google.com/file/d/1st9qW3BeIwQsnR0t8mRpvbsSWIo16ACi/view?usp=drive_link into datasets/

* Note that since annotations were not supplied for the original test data, we create our own train/val/test split by moving scenes from the training and validation sets into a new test set. The specific scenes we move are:

* Train -> Test:
    * c6911883-1843-3727-8eaa-41dc8cda8993
    * cd38ac0b-c5a6-3743-a148-f4f7b804ed17
    * d4d9e91f-0f8e-334d-bd0e-0d062467308a
    * d60558d2-d1aa-34ee-a902-e061e346e02a
    * dcdcd8b3-0ba1-3218-b2ea-7bb965aad3f0
    * de777454-df62-3d5a-a1ce-2edb5e5d4922
    * e17eed4f-3ffd-3532-ab89-41a3f24cf226
    * e8ce69b2-36ab-38e8-87a4-b9e20fee7fd2
    * e9bb51af-1112-34c2-be3e-7ebe826649b4
    * ebe7a98b-d383-343b-96d6-9e681e2c6a36
    * f0826a9f-f46e-3c27-97af-87a77f7899cd
    * f3fb839e-0aa2-342b-81c3-312b80be44f9
    * fa0b626f-03df-35a0-8447-021088814b8b
    * fb471bd6-7c81-3d93-ad12-ac54a28beb84
    * ff78e1a3-6deb-34a4-9a1f-b85e34980f06

* Val -> Test:
    * 39556000-3955-3955-3955-039557148672
    * e9a96218-365b-3ecd-a800-ed2c4c306c78
    * cb0cba51-dfaf-34e9-a0c2-d931404c3dd8
    * 00c561b9-2057-358d-82c6-5b06d76cebcf
    * 64724064-6472-6472-6472-764725145600

* run format_Argoverse.py

### MCG:
Download MCG_region_proposals.zip here: [LINK] and unzip into datasets/region_proposals.

Running the MCG code to recreate region proposals requires installing Matlab with the Parallel Processing and Image Visualisation Packages. This is not necessary, as we provide downloads for the region proposals, but if you would like to run this section:

Open Matlab in MCG/

run install.m

ensure that MCG/datasets/Argoverse/images/ contains links to the train, val, test image folders in datasets/Argoverse-1.1/images/

run MCG/scripts/im2mcg_all.m

## Models:

Download weights.zip from [LINK]. Place in weights/

### YOLOv7:
Set up environment:

```
cd environments/
conda env create -f YOLOv7.yml
conda activate YOLOv7
```

Running YOLO processes:

```
cd model_libraries/YOLOv7/
```

Training YOLOv7 on Argoverse:
```
python train.py --workers 8 --device 0 --batch-size 8 --data data/Argoverse.yaml --img 640 640 --cfg cfg/training/yolov7_argoverse.yaml --weights ../../weights/YOLOv7/pretrained/yolov7_training.pt --name new-train-run --hyp data/hyp.scratch.custom.yaml --epochs 50 --freeze 50 0 1 2
```

Results will be saved to runs/train/new-train-run/

Testing YOLOv7 on Argoverse:
```
python test.py --data data/Argoverse.yaml --img 640 --batch 8 --conf 0.001 --iou 0.65 --device 0 --weights c../../weights/YOLOv7/finetuned/best.pt --name new-test-run --task test
```

Results will be saved to runs/test/new-test-run/

### WSDDN:
Set up environment:

```
cd environments/
conda env create -f WSDDN.yml
conda activate WSDDN
```
Install MMCV:
```
cd model_libraries/WSDDN/
git clone https://github.com/open-mmlab/mmcv.git
cd mmcv
MMCV_WITH_OPS=1 pip install -e .
cd ..
```
Install MMDetection:
```
pip install -r requirements/build.txt
pip install -v -e .  # or "python setup.py develop"
cd ..
```
Install other dependencies:
```
pip install mmengine
pip install pytest
```

Running WSDDN processes:

```
cd model_libraries/WSDDN/
```

Training WSDDN on Argoverse:
```
python tools/train.py config/wsod/wsddn_faster_rcnn_r50_argoverse.py
```
