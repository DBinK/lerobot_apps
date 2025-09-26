import sys
from pathlib import Path
import json
 
from lerobot.cameras.opencv.configuration_opencv import OpenCVCameraConfig
from lerobot.configs.policies import PreTrainedConfig
from lerobot.configs.types import NormalizationMode
from lerobot.record import (
    DatasetRecordConfig,
    RecordConfig,
    record,
)
from lerobot.robots.so101_follower import SO101FollowerConfig
 
# 创建摄像头配置
camera_width = 640
camera_height = 480
cameras = {
    "front": OpenCVCameraConfig(
        index_or_path=0, width=camera_width, height=camera_height, fps=30
    ),
    "side": OpenCVCameraConfig(
        index_or_path=2, width=camera_width, height=camera_height, fps=30
    ),
    "side2": OpenCVCameraConfig(
        index_or_path=4, width=camera_width, height=camera_height, fps=30
    ),
}
 
# 创建机器人配置
robot_config = SO101FollowerConfig(
    port="/dev/arm_left_follower",
    id="left_follower",
    cameras=cameras,
    disable_torque_on_disconnect=True,
    max_relative_target=None,
    use_degrees=False,
)
 
# 创建数据集配置
user_path = "Cube/Yellow2"
user_path_eval = "Cube/eval_Yellow2"
 
dataset_config = DatasetRecordConfig(
    repo_id=user_path_eval,
    single_task="Put lego brick into the transparent box",
    num_episodes=50,
    push_to_hub=False,
    episode_time_s=120,
    reset_time_s=2,
)
 
# 直接从本地配置文件加载策略配置
policy_path = Path("outputs/train") / user_path / "checkpoints" / "last" / "pretrained_model"
config_file = policy_path / "config.json"
 
if config_file.exists():
    with open(config_file, 'r') as f:
        config_dict = json.load(f)
    
    # 移除不需要的字段
    config_dict.pop('type', None)
    config_dict.pop('pretrained_path', None)
    
    # 转换normalization_mapping中的字符串为枚举类型
    if 'normalization_mapping' in config_dict:
        norm_mapping = config_dict['normalization_mapping']
        for key in norm_mapping:
            if isinstance(norm_mapping[key], str):
                norm_mapping[key] = NormalizationMode[norm_mapping[key]]
    
    # 创建ACT配置对象
    from lerobot.policies.act.configuration_act import ACTConfig
    policy_config = ACTConfig(**config_dict)
    
    # 设置预训练路径
    policy_config.pretrained_path = str(policy_path)
else:
    raise FileNotFoundError(f"Config file not found: {config_file}")
 
# 创建完整的录制配置
record_config = RecordConfig(
    robot=robot_config,
    dataset=dataset_config,
    policy=policy_config,
    display_data=True,
    play_sounds=True,
    resume=False,
)
 
# 启动录制
if __name__ == "__main__":
    dataset = record(record_config)