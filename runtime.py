from pathlib import Path
import os


PROJECT_ROOT = Path(__file__).resolve().parent
VENV = PROJECT_ROOT / ".venv"


CUDA_DLL_DIRS = [
    VENV / "Lib" / "site-packages" / "nvidia" / "cublas" / "bin",
    VENV / "Lib" / "site-packages" / "nvidia" / "cudnn" / "bin",
    VENV / "Lib" / "site-packages" / "nvidia" / "cuda_runtime" / "bin",
    VENV / "Lib" / "site-packages" / "nvidia" / "cuda_nvrtc" / "bin",
]


def initialize():
    for dll_dir in CUDA_DLL_DIRS:
        if dll_dir.exists():
            # PythonのDLL検索パス
            os.add_dll_directory(str(dll_dir))

            # CTranslate2などがPATHを見る場合にも対応
            os.environ["PATH"] = (
                str(dll_dir)
                + os.pathsep
                + os.environ.get("PATH", "")
            )
            