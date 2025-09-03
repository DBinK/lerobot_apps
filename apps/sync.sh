uv run python -m lerobot.teleoperate \
    --robot.type=so101_follower \
    --robot.port=/dev/arm_left_follower \
    --robot.id=left_follower \
    --teleop.type=so101_leader \
    --teleop.port=/dev/arm_left_leader \
    --teleop.id=left_leader