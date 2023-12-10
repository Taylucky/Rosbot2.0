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
!python train_DAVE2.py /content/drive/<your path>/Rosbot/datasets/training_data/
```
### Training on the Slurm
Slurm is faster to train model on large quantities of data.
1. Log into the department portal nodes: ``ssh computing-id@portal.cs.virginia.edu``
2. Clone this repo into your home directory: ``git clone git@github.com:Taylucky/Rosbot2.0.git``
3. Get into the training folder ``cd ~/Rosbot2.0/training``
4. install requirements using the script provided: ``./install.sh``
5. Create a dataset directory and copy your local datasets to that remote directory:
On the remote terminal
```
mkdir -p ~/Rosbot2.0/datasets
```
On the local terminal
```
scp -r ~/Rosbot2.0/datasets computing-id@portal.cs.virginia.edu:/path/to/dataset 
```
7.  Edit the parent directory of dataset in the ``train.sh`` script
8.  Check what slurm gpu nodes are available via `sinfo` Nodes marked `idle` mean they are available for you to launch jobs on them. Refer to the CS documentation here for more info: [CS computing info](https://www.cs.virginia.edu/wiki/doku.php?id=start).
9.   Launch the job on slurm using one of the following configurations:
```
sbatch -w ai01 -p gnolim --gres=gpu:1 --exclusive=user train.sh # for gnolim partition nodes
```
If you don't have ``train.sh`` scripts, you can also run it directly
```
sbatch -w ai01 -p gnolim --gres=gpu:1 --exclusive=user python3 train_DAVE2.py /content/drive/<your path>/Rosbot/datasets/training_data/ # for gnolim partition nodes
```
10.  Check the job periodically to be sure it is progressing using the `squeue -u $USER` command, and check the log according to the `$SLURM_JOB_ID` in `slurm-$SLURM_JOB_ID.out`.
