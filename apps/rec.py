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
    "front": OpenCVCameraConfig(index_or_path=0, width=1270, height=720, fps=30)
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
    repo_id="your_hf_username/record-test",
    num_episodes=5,
    single_task="Grab the black cube",
    push_to_hub=True,
    episode_time_s=30,
    reset_time_s=30,
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

# 使用配置启动录制
dataset = record(config)
