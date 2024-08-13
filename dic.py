mexico = {
    "estado": "Nuevo León",
    "capital": "Monterrey",
    "no.municipios": 51
}

print("Estado:", mexico["estado"])  
print("Capital:", mexico["capital"])      
print("No.municipios:", mexico["no.municipios"]) 

mexico["estado"] = "Sinaloa"
print("Nuevo estado:", mexico["estado"])  

mexico["poblacion"] = "5.784 millones"

print("Poblacion:", mexico["poblacion"])  

for clave, valor in mexico.items():
    print(clave, ":", valor)
