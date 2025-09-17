from lerobot.datasets.lerobot_dataset import LeRobotDataset  
from rich import print

# 加载数据集  
dataset = LeRobotDataset("/home/f/.cache/huggingface/lerobot/RM_Cube/Orange", episodes=[0])  
# print(dataset)

# 查看第一帧数据  
first_frame = dataset[0]  
print(first_frame.keys())  

# 查看第一帧数据  
first_frame = dataset[0]  
print(first_frame.values())  


  
# 查看数据集信息  
print(f"总帧数: {dataset.num_frames}")  
print(f"FPS: {dataset.fps}")  
print(f"特征: {dataset.features}")