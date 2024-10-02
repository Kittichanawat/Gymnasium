import gymnasium as gym

# กำหนดจำนวน episodes และจำนวนขั้นตอนสูงสุดต่อ episode
num_episodes = 10
max_steps_per_episode = 200

# สร้าง environment ของ CartPole พร้อมกำหนด render_mode เป็น 'human' เพื่อแสดงผลบนหน้าจอ
env = gym.make('CartPole-v1', render_mode='human')

for episode in range(num_episodes):
    # เริ่มต้น environment และรับสถานะเริ่มต้น
    state, info = env.reset()
    
    total_reward = 0
    done = False
    truncated = False
    
    print(f"\nเริ่ม Episode {episode + 1}")
    
    for step in range(max_steps_per_episode):
        # เลือก action แบบสุ่ม (คุณสามารถเปลี่ยนเป็น policy ที่ดีขึ้นได้)
        action = env.action_space.sample()
        
        # ดำเนินการ action และรับผลลัพธ์
        next_state, reward, done, truncated, info = env.step(action)
        
        total_reward += reward
        
        # อัพเดตสถานะ
        state = next_state
        
        # แสดงผลลัพธ์ในแต่ละขั้นตอน
        print(f"Step {step + 1}: Action={action}, Reward={reward}, Total Reward={total_reward}")
        
        # ตรวจสอบว่า episode สิ้นสุดหรือไม่
        if done or truncated:
            print(f"Episode {episode + 1} จบหลังจาก {step + 1} ขั้นตอน ด้วยรางวัลรวม {total_reward}")
            break
    else:
        # หากไม่พบ done หรือ truncated ภายใน max_steps_per_episode
        print(f"Episode {episode + 1} จบหลังจาก {max_steps_per_episode} ขั้นตอน ด้วยรางวัลรวม {total_reward}")

# ปิด environment หลังจากสิ้นสุดการทดลองทั้งหมด
env.close()
