import os

def patch_roop():
    # 修正 core.py 縮排與 UI 衝突
    core_path = 'roop/core.py'
    if os.path.exists(core_path):
        with open(core_path, 'r') as f:
            lines = f.readlines()
        with open(core_path, 'w') as f:
            for line in lines:
                # 註解掉會導致崩潰的 UI 模組
                if 'import roop.ui as ui' in line or 'ui.init()' in line:
                    f.write(f'# {line}')
                else:
                    f.write(line)
        print("✅ core.py 修復完成")

    # 修正 face_swapper.py 裡過時的 NSFW 檢查
    swapper_path = 'roop/processors/frame/face_swapper.py'
    if os.path.exists(swapper_path):
        with open(swapper_path, 'r') as f:
            lines = f.readlines()
        with open(swapper_path, 'w') as f:
            for line in lines:
                if 'import opennsfw2' in line or 'opennsfw2.predict_video' in line:
                    f.write(f'# {line}')
                else:
                    f.write(line)
        print("✅ face_swapper.py 修復完成")

if __name__ == "__main__":
    patch_roop()
