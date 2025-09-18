from lerobot.cameras import CameraConfig
from lerobot.cameras.opencv.configuration_opencv import OpenCVCameraConfig

from lerobot.robots.so101_follower import SO101FollowerConfig
from lerobot.teleoperators.so101_leader import SO101LeaderConfig

from lerobot.record import (
    DatasetRecordConfig,
    RecordConfig,
    record,
)

# 添加摄像头配置，并显式指定类型
cameras: dict[str, CameraConfig] = {
    "front": OpenCVCameraConfig(
        index_or_path=0, width=1280, height=720, fps=30, warmup_s=1
    ),
    "side": OpenCVCameraConfig(
        index_or_path=2, width=1280, height=720, fps=30, warmup_s=1
    ),
    "side2": OpenCVCameraConfig(
        index_or_path=4, width=1280, height=720, fps=30, warmup_s=3
    ),
}

robot_config = SO101FollowerConfig(
    port="/dev/arm_left_follower",
    id="left_follower",
    cameras=cameras,  # 添加摄像头
    disable_torque_on_disconnect=True,
    max_relative_target=None,
    use_degrees=False,
)


# 创建远程操作配置（leader）
teleop_config = SO101LeaderConfig(port="/dev/arm_left_leader", id="left_leader")

# 创建数据集配置
dataset_config = DatasetRecordConfig(
    repo_id="Cube/Yellow",
    num_episodes=15,
    single_task="Grab the Yellow cube",
    push_to_hub=False,
    episode_time_s=15,
    reset_time_s=5,
)

# 创建完整的RecordConfig
config = RecordConfig(
    robot=robot_config,
    dataset=dataset_config,
    teleop=teleop_config,
    display_data=True,
    play_sounds=True,
    resume=False,
)

# 录制前执行清理
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
import clean_dateset

print("Starting cleanup before recording...")
target_path = str(Path.home() / ".cache/huggingface/lerobot" / dataset_config.repo_id)
clean_dateset.clean_directory(target_path, remove_dir=True)

# 使用配置启动录制
dataset = record(config)
