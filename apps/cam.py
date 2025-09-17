
from lerobot.record import RecordConfig, record

RECORDING_CONFIG = {
    "robot": {
        "type": "so100_follower",
        "port": "/dev/tty.usbmodem58760431541",
        "id": "black",
        "cameras": {
            "laptop": {
                "type": "opencv",
                "camera_index": 0,
                "width": 640,
                "height": 480
            }
        }
    },
    "dataset": {
        "repo_id": "your_username/your_dataset",
        "num_episodes": 10,
        "single_task": "抓取立方体",
        "fps": 30
    },
    "teleop": {
        "type": "so100_leader",
        "port": "/dev/tty.usbmodem58760431551",
        "id": "blue"
    }
}

# 转换为RecordConfig对象并执行
config = RecordConfig(**RECORDING_CONFIG)
dataset = record(config)