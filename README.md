# fix_roop.py - 專為 2025 Colab 環境設計的 roop 修復補丁
import os
import numpy as np

def run_fix():
    print("🛠️ 開始執行 roop 自動化修復補丁...")
    
    # 1. 補回 Numpy 屬性
    np.int = int
    np.float = float
    np.bool = bool
    print("✅ Numpy 屬性修復完成")

    # 2. 修正 core.py
    file_path = '/content/roop/roop/core.py'
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        with open(file_path, 'w', encoding='utf-8') as f:
            for line in lines:
                if 'import tensorflow' in line or 'import opennsfw2' in line or 'tensorflow.' in line:
                    f.write('# ' + line)
                elif 'limit_resources()' in line:
                    f.write('    pass # limit_resources()\\n')
                else:
                    f.write(line)
        print("✅ core.py 代碼邏輯修正完成")
    else:
        print("❌ 錯誤：找不到 /content/roop/roop/core.py")

if __name__ == "__main__":
    run_fix()
