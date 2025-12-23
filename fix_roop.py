import os
import numpy as np

def run_fix():
    print("🛠️ 正在執行 kity2233466 的自動化修復補丁...")
    
    # 1. 補回 Numpy 屬性
    np.int = int
    np.float = float
    np.bool = bool

    # 2. 修正 core.py 代碼
    file_path = '/content/roop/roop/core.py'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        with open(file_path, 'w', encoding='utf-8') as f:
            for line in lines:
                # 屏蔽 TensorFlow 與 NSFW 檢查
                if 'import tensorflow' in line or 'import opennsfw2' in line or 'tensorflow.' in line:
                    f.write('# ' + line)
                # 修復會崩潰的函數
                elif 'limit_resources()' in line:
                    f.write('    pass # limit_resources()\\n')
                else:
                    f.write(line)
        print("✅ 2025 版本相容性修正完成！")
    else:
        print("❌ 找不到 core.py，請確認是否已 clone roop")

if __name__ == "__main__":
    run_fix()
