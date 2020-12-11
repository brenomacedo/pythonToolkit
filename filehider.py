import ctypes

attr_hide = 0x02
return_ = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', attr_hide)

if return_:
    print('o arquivo foi ocultado!')
else:
    print('arquivo nao foi ocultado!')
