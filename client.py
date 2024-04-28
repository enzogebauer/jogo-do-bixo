import xmlrpc.client
import sys

if len(sys.argv) != 3:
    print("Informe os parâmetros corretamente!")
    sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

server = xmlrpc.client.ServerProxy("http://localhost:8000")
result = server.add(num1, num2)

print(result)