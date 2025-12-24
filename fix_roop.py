import os
import numpy as np

# 1. 補回 Numpy 屬性 (這是核心修復)
np.int = int
np.float = float
np.bool = bool

def run_patch():
    path = '/content/roop/roop/core.py'
    if os.path.exists(path):
        with open(path, 'r') as f:
            lines = f.readlines()
        with open(path, 'w') as f:
            for line in lines:
                # 屏蔽報錯套件
                if 'import tensorflow' in line or 'import opennsfw2' in line:
                    f.write('#' + line)
                # 修復語法錯誤
                elif 'limit_resources()' in line:
                    f.write('    pass # patched\\n')
                else:
                    f.write(line)
        print("✅ GitHub 補丁：core.py 修復完成！")

if __name__ == "__main__":
    run_patch()
