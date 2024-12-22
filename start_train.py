if __name__ == '__main__':
    from ultralytics import YOLO

    # Load a model
    model = YOLO('yolov8m-WaveletPool.yaml')  # build a new model from YAML
    # model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
    # model = YOLO('path/to/the/YAML').load(
    #              'path/to/the/pre_trained/weights')  # build from YAML and transfer weights

    # Train the model
    model.train(data='ultralytics/cfg/datasets/datasets.yaml')
    # 已改gpu，device = 0
