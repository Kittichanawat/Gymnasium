import gymnasium as gym

# สร้าง environment
env = gym.make("AirRaid-v4", render_mode="human")
env.metadata["render_fps"] = 30  # ตั้งค่า fps

observation, info = env.reset(seed=42)

for i in range(1000):
    env.render()  # แสดงผลสภาพแวดล้อม
    action = env.action_space.sample()  # สุ่มเลือกการกระทำ
    observation, reward, terminated, truncated, info = env.step(action)  # ทำการ step

    if terminated or truncated:
        observation, info = env.reset()

env.close()  # ปิด environment
