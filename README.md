# Sagemaker Local Development Example

This repo demonstrates how to develop a SageMaker model from your local environment. 

[local_dev.ipynb](/local_dev.ipynb) notebook demonstrates how to develop and deploy a model from your local environment. Note that you need to input your own IAM role. The role cannot be automatically generated using: 

from sagemaker import get_execution_role

role = get_execution_role()

The above function only works if you are developing the model using SageMaker Studio or a SageMaker Notebook instance.
The youtube video I made about this set up can be found **[here](https://youtu.be/5SGhHXe8GHw)**

[train.py](/train.py) script contains the training logic used during model training.. 

[setup_commands.txt](/setup_commands.txt) lists the steps to follow for setting up your local environment for SageMaker development.

[data](/data/) data folder contains the Iris dataset used for model training and testing. 
[local_training](/local_training.ipynb) notebook demonstrates how to train and deploy sagemaker model on your local machine.  You can watch the video of this demonstration **[here](https://youtu.be/xWet3n9pwT4)** 






