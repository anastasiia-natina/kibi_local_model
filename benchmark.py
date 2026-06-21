import time
import psutil
import os
from EdTechModul import SecurityEnhancedVoiceEngine

def benchmark_engine():
    process = psutil.Process(os.getpid())
    
    # 1. ТЕСТ: Cold Start (Холодний старт)
    start_time = time.perf_counter()
    initial_mem = process.memory_info().rss / (1024 * 1024) # MB
    
    # Вкажіть повний шлях до вашої папки з моделлю
    engine = SecurityEnhancedVoiceEngine(model_path="C:/Users/anastasiia/model")
    
    end_time = time.perf_counter()
    final_mem = process.memory_info().rss / (1024 * 1024)
    
    print(f"--- COLD START RESULTS ---")
    print(f"Initialization Time: {end_time - start_time:.4f} seconds")
    print(f"Memory Usage Increase: {final_mem - initial_mem:.2f} MB")

    # 2. ТЕСТ: Під навантаженням (імітація обробки)
    cpu_before = process.cpu_percent(interval=None)
    # Імітуємо обробку 100 циклів
    for _ in range(100):
        engine.sanitize_and_process("jump")
        
    cpu_after = process.cpu_percent(interval=1)
    print(f"\n--- LOAD TEST RESULTS ---")
    print(f"CPU Load during inference: {cpu_after}%")

if __name__ == "__main__":
    benchmark_engine()