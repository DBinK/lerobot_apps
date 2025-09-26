import sys
from pathlib import Path
 
from lerobot.configs.train import TrainPipelineConfig
from lerobot.configs.default import DatasetConfig, WandBConfig
from lerobot.policies.act.configuration_act import ACTConfig
from lerobot.scripts.train import train
 
# 创建数据集配置
dataset_config = DatasetConfig(
    repo_id="Cube/Yellow2",
    use_imagenet_stats=True
)
 
# 创建ACT策略配置
policy_config = ACTConfig(
    device="cuda",
    use_amp=True,
    push_to_hub=False,
    chunk_size=30,
    n_action_steps=30,
    use_vae=False,
    dim_model=256,
    dim_feedforward=1024,
    n_encoder_layers=2
)
 
# 创建WandB配置
wandb_config = WandBConfig(
    enable=False
)
 
# 创建训练配置
train_config = TrainPipelineConfig(
    dataset=dataset_config,
    policy=policy_config,
    output_dir=Path("outputs/train/Cube/Yellow2"),  # 修改为与数据集名称一致的输出目录
    job_name="clamp_Cube",
    batch_size=2,
    steps=100000,
    wandb=wandb_config
)
 
# 启动训练
if __name__ == "__main__":
    train(train_config)