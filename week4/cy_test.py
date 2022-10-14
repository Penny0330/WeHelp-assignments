# 0. 載入模組
from cryptography.fernet import Fernet

# 1.產生密鑰
# 使用 Fernet.generate_key() 或 自己設定一個密碼
key = Fernet.generate_key()
print("key : ", key)
# key : b'q9j99TPGQZJW3ZdaRLVMqUmChobB6O2S4rzDXMlksJo='
f = Fernet(key)
print("f : ", f)
# f : <cryptography.fernet.Fernet object at 0x000001669FD17C40>
user = "penny"

# 2. 加密 f.encrypt()
# 需先將 user 轉成 bytes 型態
user_en = f.encrypt(user.encode())
print("原本的 : ", user, type(user))
# 原本的 :  penny <class 'str'>
print("加密的 : ", user_en, "\n", type(user_en))
# 加密的 :  b'gAAAAABjSVgiYIqU48lB0zHXyUKiJ3BzKxH8AgvRdcN-IcHmjiNT0J1kgpN4wiqoW9GQ_oLZOFcrnGs-cNAoz5dqziX0ikv4LQ=='
#  <class 'bytes'>

# 3. 解密 f.decrypt()
# 解密前先把型態轉回 str
user_str = f.decrypt(user_en).decode()
print("解密的 : ", user_str, "\n", type(user_str))
# 解密的 : penny <class 'str'>

# 解密前未先轉型態
user_str = f.decrypt(user_en)
print(user_str, type(user_str))
# b'penny' <class 'bytes'>
