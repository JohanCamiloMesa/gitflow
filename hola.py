#Listo para subir

def es_par_o_impar(numero):
  """
  Verifica si un número entero es par o impar.

  Args:
    numero: Un número entero.

  Returns:
    "Par" si el número es par, "Impar" si el número es impar.
  """
  if numero % 2 == 0:
    return "Par"
  else:
    return "Impar"

# Ejemplo de uso
numero = 10
resultado = es_par_o_impar(numero)
print(f"El número {numero} es {resultado}")

numero = 7
resultado = es_par_o_impar(numero)
print(f"El número {numero} es {resultado}")