import torch
from model import DAVE2v3
from dataset import TRANSFORM

# load model
def load_model(model_path):
    model = DAVE2v3()
    model.load_state_dict(torch.load(model_path))
    return model

# inference
def inference(model, image):
    # image is a RGB np array
    # transform image
    image = TRANSFORM(image)
    # add batch dimension
    image = image.unsqueeze(0)
    # get prediction
    prediction = model(image)
    return prediction

