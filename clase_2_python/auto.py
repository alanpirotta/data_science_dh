def crear_auto (fabricante, modelo, **keyword):
    keyword['fabricante']=fabricante
    keyword['modelo']=modelo
    print(f'{keyword}')