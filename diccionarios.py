def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    poblacion_paises = {
        'Argentina': 444_444_2312,
        'Brasil': 444_444_2332_3211,
        'Alaska': 423_344_233,
    }

    for pais, poblacion in poblacion_paises.items():
        print('El pais: '+ pais + ' ' +str(poblacion)+' habitantes')

if __name__ == '__main__':
    run()
