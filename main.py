import requests

# Tu clave de API de ExchangeRate-API
API_KEY = '837fd2a6e8e0257aef8e1394'
BASE_URL = 'https://v6.exchangerate-api.com/v6'

def obtener_tasas_de_cambio(base_currency):
    url = f"{BASE_URL}/{API_KEY}/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['result'] == 'success':
            return data['conversion_rates']
        else:
            print("Error en la solicitud:", data['error-type'])
            return None
    else:
        print("Error en la solicitud HTTP:", response.status_code)
        return None

def convertir_moneda(cantidad, tasa):
    return cantidad * tasa

def menu():
    while True:
        print("\nMenú de Conversión de Moneda")
        print("1. Dólar => Peso argentino")
        print("2. Peso argentino => Dólar")
        print("3. Dólar => Real brasileño")
        print("4. Real brasileño => Dólar")
        print("5. Dólar => Peso colombiano")
        print("6. Peso colombiano => Dólar")
        print("7. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            tasa_dolar_a_peso_arg = obtener_tasas_de_cambio('USD').get('ARS')
            if tasa_dolar_a_peso_arg:
                cantidad = float(input("Introduce la cantidad en Dólares: "))
                convertido = convertir_moneda(cantidad, tasa_dolar_a_peso_arg)
                print(f"{cantidad} Dólares = {convertido:.2f} Pesos argentinos")
            else:
                print("No se pudo obtener la tasa de cambio.")
        
        elif opcion == "2":
            tasa_peso_arg_a_dolar = 1 / obtener_tasas_de_cambio('ARS').get('USD')
            if tasa_peso_arg_a_dolar:
                cantidad = float(input("Introduce la cantidad en Pesos argentinos: "))
                convertido = convertir_moneda(cantidad, tasa_peso_arg_a_dolar)
                print(f"{cantidad} Pesos argentinos = {convertido:.2f} Dólares")
            else:
                print("No se pudo obtener la tasa de cambio.")
        
        elif opcion == "3":
            tasa_dolar_a_real_brl = obtener_tasas_de_cambio('USD').get('BRL')
            if tasa_dolar_a_real_brl:
                cantidad = float(input("Introduce la cantidad en Dólares: "))
                convertido = convertir_moneda(cantidad, tasa_dolar_a_real_brl)
                print(f"{cantidad} Dólares = {convertido:.2f} Reales brasileños")
            else:
                print("No se pudo obtener la tasa de cambio.")
        
        elif opcion == "4":
            tasa_real_brl_a_dolar = 1 / obtener_tasas_de_cambio('BRL').get('USD')
            if tasa_real_brl_a_dolar:
                cantidad = float(input("Introduce la cantidad en Reales brasileños: "))
                convertido = convertir_moneda(cantidad, tasa_real_brl_a_dolar)
                print(f"{cantidad} Reales brasileños = {convertido:.2f} Dólares")
            else:
                print("No se pudo obtener la tasa de cambio.")
        
        elif opcion == "5":
            tasa_dolar_a_peso_col = obtener_tasas_de_cambio('USD').get('COP')
            if tasa_dolar_a_peso_col:
                cantidad = float(input("Introduce la cantidad en Dólares: "))
                convertido = convertir_moneda(cantidad, tasa_dolar_a_peso_col)
                print(f"{cantidad} Dólares = {convertido:.2f} Pesos colombianos")
            else:
                print("No se pudo obtener la tasa de cambio.")
        
        elif opcion == "6":
            tasa_peso_col_a_dolar = 1 / obtener_tasas_de_cambio('COP').get('USD')
            if tasa_peso_col_a_dolar:
                cantidad = float(input("Introduce la cantidad en Pesos colombianos: "))
                convertido = convertir_moneda(cantidad, tasa_peso_col_a_dolar)
                print(f"{cantidad} Pesos colombianos = {convertido:.2f} Dólares")
            else:
                print("No se pudo obtener la tasa de cambio.")
        
        elif opcion == "7":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    menu()
