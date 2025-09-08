from lerobot.teleoperate import TeleoperateConfig, teleoperate
from lerobot.robots.so101_follower import SO101FollowerConfig
from lerobot.teleoperators.keyboard import KeyboardEndEffectorTeleopConfig
 
# 创建SO101机器人配置
robot_config = SO101FollowerConfig(
    port="/dev/arm_left_follower",
    id="left_follower"
)
 
# 创建键盘远程操作配置
teleop_config = KeyboardEndEffectorTeleopConfig(
    use_gripper=True,  # 启用夹爪控制
    id="keyboard_controller"
)
 
# 创建远程操作总配置
teleoperate_config = TeleoperateConfig(
    teleop=teleop_config,
    robot=robot_config,
    fps=30,  # 控制频率
    display_data=True  # 显示实时数据
)
 
# 执行远程操作
teleoperate(teleoperate_config)