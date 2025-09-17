from lerobot.teleoperators.so101_leader import SO101Leader, SO101LeaderConfig

config = SO101LeaderConfig(
    port="/dev/arm_left_follower",
    id="left_follower",
    # port="/dev/arm_right_follower",
    # id="right_follower",
)

leader = SO101Leader(config)
leader.connect(calibrate=False)
leader.calibrate()
leader.disconnect()
