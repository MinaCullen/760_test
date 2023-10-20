from mmdet.apis import init_detector, inference_detector

#config_file = 'configs/faster_rcnn/faster-rcnn_r50_fpn_1x_coco.py'
config_file = 'configs/wsod/wsddn_faster_rcnn_r50_argoverse.py'
# checkpoint_file = 'checkpoints/wsod/vgg16.pth'
device = 'cuda:0'
# init a detector
model = init_detector(config_file, device=device)
# inference the demo image
inference_detector(model, 'data/Argoverse/Argoverse-1.1/tracking/test/00c561b9-2057-358d-82c6-5b06d76cebcf/ring_front_center/ring_front_center_315969629022515560.jpg')