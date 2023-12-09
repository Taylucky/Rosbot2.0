import argparse
import torch
import torch.nn.functional as F
from torch.utils.data import DataLoader
import random
import sys
from torchvision.transforms import Compose, ToTensor

sys.path.append("../models")
from DatasetGenerator import MultiDirectoryDataSequence  # Make sure to import the appropriate class


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('model_path', type=str, help='path to the trained model')
    parser.add_argument('test_dataset', type=str, help='path to the test dataset')
    parser.add_argument("--batch", type=int, default=64)
    args = parser.parse_args()
    return args


def test(model, testloader, device):
    model.eval()
    total_loss = 0.0

    with torch.no_grad():
        for i, hashmap in enumerate(testloader, 0):
            x = hashmap['image'].float().to(device)
            y = hashmap['steering_input'].float().to(device)

            outputs = model(x)
            loss = F.mse_loss(outputs, y)
            total_loss += loss.item()

    average_loss = total_loss / len(testloader)
    print(f'Average Test Loss: {average_loss}')


if __name__ == '__main__':
    args = parse_arguments()

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # Load the trained model
    model = torch.load(args.model_path)
    model = model.to(device)

    # Create a DataLoader for the test dataset
    test_dataset = MultiDirectoryDataSequence(args.test_dataset, image_size=(640, 480), transform=Compose([ToTensor()]))
    print("test data number:")
    print(len(test_dataset))
    total_samples = len(test_dataset)
    num_samples_to_use = 1700

    # Randomly select 1700 indices
    random_indices = random.sample(range(total_samples), num_samples_to_use)

    # Create a Subset dataset with the randomly selected indices
    test_dataset_subset = torch.utils.data.Subset(test_dataset, random_indices)

    print("test data subset number:")
    print(len(test_dataset_subset))

    print(args.test_dataset)
    testloader = DataLoader(test_dataset, batch_size=args.batch, shuffle=False)
    print(len(testloader))
    # Run the testing function
    test(model, testloader, device)