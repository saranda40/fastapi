import bcrypt

def encriptar_contraseña(contraseña: str) -> str:
    return bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def des_encriptar_contraseña(contraseña: str, contraseña_encriptada: str) -> bool:
    return bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_encriptada.encode('utf-8'))

def verificar_contraseña(contraseña: str, contraseña_encriptada: str) -> bool:
    return bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_encriptada.encode('utf-8'))
