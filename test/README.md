## Test the model
1. Replace the model path with the path of your best model file in the ``test/py``
2. Change the working directory to the training part
```
import os
path = "/content/drive/<your path>/Rosbot/training"
os.chdir(path)
print(os.getcwd())
```
3. Install the packages
```
!pip install torch torchvision numpy black mypy scipy scikit-image pandas opencv-python matplotlib kornia
```
4. run the test code
Run the ``test.sh`` or directly run it
```
!python Test_try.py /best_model.pt /content/drive/<your path>/Rosbot/datasets/test_data/
```
