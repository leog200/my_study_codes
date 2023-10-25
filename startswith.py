#O método startswith() retorna True se a string começar com o valor especificado, caso contrário, False.
#Neste exemplo, a função startswith() é usada para verificar se a string frase começa com a substring "Olá". 
#Dependendo do resultado da verificação, uma mensagem apropriada é exibida na saída.


frase = "Olá, como você está?"

if frase.startswith("Olá"):
    print("A frase começa com 'Olá'.")
else:
    print("A frase não começa com 'Olá'.")
