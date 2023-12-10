## Training the model
### Training on the Colab
Colab is easier to debug.
1. Upload Rosbot2.0 folder to your Google Drive
2. Create a python notebook on Colab, change the runtime type as GPU and mount your Google Drive
3. Change the working directory to the training part
```
import os
path = "/content/drive/<your path>/Rosbot/training"
os.chdir(path)
print(os.getcwd())
```
7. Install the packages
```
!pip install torch torchvision numpy black mypy scipy scikit-image pandas opencv-python matplotlib kornia
```
8. run the training code
```
!python train_DAVE2.py /content/drive/<your path>/Rosbot/datasets/traininf_data/
```
### Training on the Slurm
Slurm is faster to train model on large quantities of data.
