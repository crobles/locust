from faker import Faker
import json
import random
from math import ceil

fake = Faker()

def generate_product():
    return {
        "id_producto": fake.uuid4(),
        "nombre_producto": fake.word(),
        "precio": str(random.randint(1000, 100000)),
        "SKU": fake.uuid4()
    }

def generate_promotion(product_sku):
    return {
        "id_promocion": fake.uuid4(),
        "off": round(random.uniform(0.1, 0.5), 2),
        "sku": product_sku
    }

def generate_user_data(include_promotions=True):
    products = [generate_product() for _ in range(2)]
    promotions = [generate_promotion(product["SKU"]) for product in products] if include_promotions else []

    user_data = {
        "nombre": fake.first_name(),
        "apellido": fake.last_name(),
        "rut": str(fake.random_number(digits=8, fix_len=True)),
        "telefono": fake.phone_number(),
        "correo": fake.email(),
        "direccion": fake.address(),
        "fecha_nacimiento": fake.date_of_birth().strftime('%Y-%m-%d'),
        "fecha_creacion": fake.date().replace('-', '-'),
        "instagram": f"@{fake.user_name()}",
        "carrito": {
            "id_carrito": random.randint(1, 1000),
            "productos": products,
            "promociones": promotions
        }
    }

    return user_data

def generate_multiple_users(n=5, include_promotions=True):
    return [generate_user_data(include_promotions) for _ in range(n)]

if __name__ == "__main__":
    # Generar 10 usuarios con promociones
    users_with_promotions = generate_multiple_users(10, include_promotions=True)
    
    # Generar 10 usuarios sin promociones
    users_without_promotions = generate_multiple_users(10, include_promotions=False)
    
    # Combinar los datos en un solo array
    data_array = users_with_promotions + users_without_promotions
    
     # Calcular el 40% de los datos para repetir
    num_to_repeat = ceil(0.40 * len(data_array))

    # Seleccionar y duplicar el 40% de los datos
    repeated_data = random.sample(data_array, num_to_repeat)
    data_array.extend(repeated_data)

    # Mezclar los datos
    random.shuffle(data_array)

    # Guardar el resultado en un archivo JSON
    with open('fakeData.json', 'w', encoding='utf-8') as f:
        json.dump(data_array, f, ensure_ascii=False, indent=4)

    print("Datos generados y guardados en 'fakeData.json'.")