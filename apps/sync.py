from lerobot.teleoperate import TeleoperateConfig, teleoperate
from lerobot.robots.so101_follower import SO101FollowerConfig
from lerobot.teleoperators.so101_leader import SO101LeaderConfig
 
# 创建机器人配置（follower）
robot_config = SO101FollowerConfig(
    port="/dev/arm_left_follower",
    id="left_follower"
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
    display_data=False,  # 是否显示数据
    teleop_time_s=None  # 运行时间，None 表示无限运行
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