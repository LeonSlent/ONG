import bcrypt
import sys

class Cryptograph:
    def __init__(self) -> None:
        self.salt_rounds = 12  # Ajustável conforme necessário

    def encrypt(self, password: str) -> str:
        try:
            salt = bcrypt.gensalt(self.salt_rounds)
            return bcrypt.hashpw(password.encode(), salt).decode()
        except Exception as e:
            print(f'{type(e).__name__}: {e} in line {sys.exc_info()[-1].tb_lineno} in file {sys.exc_info()[-1].tb_frame.f_code.co_filename}')
            return None

    def decrypt(self, hash: str, password: str) -> bool:
        try:
            return bcrypt.checkpw(password.encode(), hash.encode())
        except Exception as e:
            print(f'{type(e).__name__}: {e} in line {sys.exc_info()[-1].tb_lineno} in file {sys.exc_info()[-1].tb_frame.f_code.co_filename}')
            return False