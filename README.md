# face_mask_based_automation
Simple automation project using darket YOLOv4 image recognition on Jetson TX2 to control/monitor devices connected to raspberry pi

To run detection on Jetson, navigate to Jetson directory and execute following command
python3 darknet_images.py --input test/ --weights yolov4model/yolov4-tiny-obj_6000.weights --ext_output --config_file yolov4model/yolov4-tiny-obj.cfg --data_file yolov4model/obj.data --thresh 0.3

To start client on Raspberry pi, navigate to pi directory and execute following command
python3 home_auto_client.py

The results will be stored in pi/output/results.txt file
