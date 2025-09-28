from faker import Faker

fake = Faker("es_MX")  # Datos realistas de México

cantidad_usuarios = 1000

for i in range(cantidad_usuarios):
    # Generar nombre y apellido
    nombre = fake.first_name()
    apellido = fake.last_name()
    
    # Crear correo con hotmail.com
    correo = f"{nombre.lower()}.{apellido.lower()}@hotmail.com"
    
    # Crear usuario
    usuario = {
        "nombre": f"{nombre} {apellido}",
        "correo": correo,
        "telefono": fake.phone_number(),
        "direccion": fake.address()
    }
    
    # Imprimir verticalmente
    print(f"Usuario {i+1}:")
    print("Nombre:", usuario["nombre"])
    print("Correo:", usuario["correo"])
    print("Teléfono:", usuario["telefono"])
    print("Dirección:", usuario["direccion"])
    print("-" * 0)  # Separador