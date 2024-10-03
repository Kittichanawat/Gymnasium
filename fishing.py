import gymnasium as gym

# สร้าง environment สำหรับ Fishing Derby
env = gym.make("FishingDerby-v0", render_mode="human")

# เริ่มต้น environment
obs, info = env.reset()

# เล่นเกม
for _ in range(1000):
    # เลือก action แบบสุ่ม
    action = env.action_space.sample()

    # โต้ตอบกับ environment ด้วย action ที่เลือก
    obs, reward, done, truncated, info = env.step(action)

    # แสดงผลลัพธ์
    print(f"Observation: {obs}, Reward: {reward}, Done: {done}")

    # ถ้าเกมจบ ให้เริ่มใหม่
    if done or truncated:
        obs, info = env.reset()

# ปิด environment เมื่อจบการเล่น
env.close()