from lerobot.teleoperate import TeleoperateConfig, teleoperate
from lerobot.robots.so101_follower import SO101FollowerConfig
from lerobot.teleoperators.so101_leader import SO101LeaderConfig
 
from lerobot.cameras.opencv.configuration_opencv import OpenCVCameraConfig
 
# 添加摄像头配置
cameras = {
    "front": OpenCVCameraConfig(
        # type="opencv",
        index_or_path=0,
        width=640,
        height=480,
        fps=30
    )
}
 
robot_config = SO101FollowerConfig(
    port="/dev/arm_left_follower",
    id="left_follower",
    cameras=cameras,  # 添加摄像头
    disable_torque_on_disconnect=True,
    max_relative_target=None,
    use_degrees=False
)
 

# 创建远程操作配置（leader）
teleop_config = SO101LeaderConfig(
    port="/dev/arm_left_leader",
    id="left_leader"
)
 
# 创建远程操作总配置
teleoperate_config = TeleoperateConfig(
    teleop=teleop_config,
    robot=robot_config,
    fps=60,  # 控制频率
    display_data=True,  # 是否显示数据
    teleop_time_s=300  # 运行5分钟
)
 

 
# 执行远程操作
teleoperate(teleoperate_config)

"""
uv run python -m lerobot.teleoperate \
    --robot.type=so101_follower \
    --robot.port=/dev/arm_left_follower \
    --robot.id=left_follower \
    --teleop.type=so101_leader \
    --teleop.port=/dev/arm_left_leader \
    --teleop.id=left_leader
"""