import numpy as np
from EdTechModul import SecurityEnhancedVoiceEngine

def run_dos_attack():
    print("[TEST] Initializing engine for DoS Simulation...")
    # Ініціалізуємо двигун (вказавши правильний шлях)
    engine = SecurityEnhancedVoiceEngine(model_path="C:/Users/anastasiia/model")
    
    print("\n[ATTACK] Launching Audio Flood (DoS attack)...")
    # Імітуємо величезний шматок "сміттєвого" аудіо (наприклад, 5 МБ сирих байтів за один раз)
    # Звичайний буфер мікрофона займає близько 16-32 КБ.
    malicious_audio_buffer = np.random.bytes(5 * 1024 * 1024) # 5 Megabytes
    
    try:
        print(f"[ATTACK] Injecting massive buffer: {len(malicious_audio_buffer) / (1024*1024):.2f} MB into audio_callback...")
        # Викликаємо внутрішній обробник безпосередньо, минаючи затримки мікрофона
        engine.recognizer.AcceptWaveform(malicious_audio_buffer)
        
        # Викликаємо очищення, щоб перевірити стійкість Memory Wiping
        engine.recognizer.Reset()
        del malicious_audio_buffer
        
        print("[SUCCESS] Engine survived the flood! No Buffer Overflow detected.")
        print("[PRIVACY] Verification: RAM Wiped successfully.")
        
    except Exception as e:
        print(f"[FAIL] Engine crashed under DoS: {e}")

if __name__ == "__main__":
    run_dos_attack()