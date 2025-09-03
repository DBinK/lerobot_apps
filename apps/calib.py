from lerobot.robots.so101_follower import SO101Follower, SO101FollowerConfig

config = SO101FollowerConfig(
    port="/dev/arm_left_leader",
    id="left_leader",

    # port="/dev/arm_left_follower",
    # id="left_follower",

    # port="/dev/arm_right_leader",
    # id="right_leader",

    # port="/dev/arm_right_follower",
    # id="right_follower",
)

follower = SO101Follower(config)
follower.connect(calibrate=False)
follower.calibrate()
follower.disconnect()
