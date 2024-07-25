from faker import Faker
import argparse
import json

fake = Faker('es_ES')  # Usar Faker con la localización española
parser = argparse.ArgumentParser(description='Ejemplo de pasar un parámetro a un script de Python.')
parser.add_argument('parametro', type=str, help='El parámetro que quieres pasar al script')
args = parser.parse_args()

base_json1 = {
  "nombre": "cristofer",
  "apellido": "robles",
  "rut": "1",
  "telefono": "987767876",
  "correo": "croblesr@ripley.com",
  "direccion": "mi casita",
  "fecha_nacimiento": "1987-06-23",
  "fecha_creacion": "2024-28-07",
  "instagram": "@crobles01",
  "carrito": {
    "id_carrito": 1,
    "productos": [
      {
        "id_producto": "3456ytgre3456y",
        "nombre_producto": "zapatilla",
        "precio": "29990",
        "SKU": "6789oikjhbgt678i"
      },
      {
        "id_producto": "7f8ikj5n6tygifo",
        "nombre_producto": "iphone",
        "precio": "1999990",
        "SKU": "5i98rf7gybhgnjk76"
      }
    ],
    "promociones": [
      {
        "id_promocion": "0h9u8t9g",
        "off": 0.5,
        "sku": "6789oikjhbgt678i"
      },
      {
        "id_promocion": "8ti56jk7uh",
        "off": 0.25,
        "sku": "5i98rf7gybhgnjk76"
      }
    ]
  }
}

base_json1 = {
  "nombre": "cristofer",
  "apellido": "robles",
  "rut": "1",
  "telefono": "987767876",
  "correo": "croblesr@ripley.com",
  "direccion": "mi casita",
  "fecha_nacimiento": "1987-06-23",
  "fecha_creacion": "2024-28-07",
  "instagram": "@crobles01",
  "carrito": {
    "id_carrito": 1,
    "productos": [
      {
        "id_producto": "3456ytgre3456y",
        "nombre_producto": "zapatilla",
        "precio": "29990",
        "SKU": "6789oikjhbgt678i"
      },
      {
        "id_producto": "7f8ikj5n6tygifo",
        "nombre_producto": "iphone",
        "precio": "1999990",
        "SKU": "5i98rf7gybhgnjk76"
      }
    ],
    "promociones": []
  }
}


def generar_datos():
    return {
        "nombre": fake.first_name(),
        "apellido": fake.last_name(),
        "rut": str(fake.random_number(digits=9, fix_len=True)),
        "telefono": fake.phone_number(),
        "correo": fake.email(),
        "direccion": fake.address(),
        "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
        "fecha_creacion": fake.date_this_year().strftime("%Y-%d-%m"),
        "instagram": f"@{fake.user_name()}"
    }

data_array = [generar_datos() for _ in range(int(args.parametro))]

#print(json.dumps(data_array, indent=4, ensure_ascii=False))

# Guardar el resultado en un archivo JSON
with open('fakeData.json', 'w', encoding='utf-8') as f:
    json.dump(data_array, f, ensure_ascii=False, indent=4)

print("Datos generados y guardados en fakeData.json")