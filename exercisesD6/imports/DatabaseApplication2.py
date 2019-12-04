# import z określonej lokalizacji konkretnych składowych
# składowe są dostępne bez adresowania
# składowe są importowane tylko po nazwach
from exercisesD6.imports.SecretVariables import Hello
from exercisesD6.imports.SecretVariables import getConnection
from exercisesD6.imports.SecretVariables import username, password
import exercisesD6.imports.SecretVariables as secret
import exercisesD6.imports.SV as sv


# CTRL + ALt + O    -> optimize imports
print(secret.database)
print(sv.database)
print(username)
print(password)

# print(port) -> nie jest importowany
print(getConnection())
h = Hello("MK")
print(h)