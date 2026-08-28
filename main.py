def somar (valor_principal, acrescimo):
   '''
        Adiciona o acrescimo ao valor principal

         Args:
           valor principal (float):
           acrescimo (float): valor a ser adicionado ao valor inicial

        Returns:
           float: soma do valor principal e acrescimo
    '''
   return valor_principal + acrescimo

def testar_operacao_soma ():
   # Arrange
   valor1 = 100.0
   valor2 = 50.0
   # Act
   resultado = somar (valor1, valor2)
   # Assert
   assert (resultado == 150.0 ), "A soma falhou"
   print ("Teste de soma: PASSOU!")


def subtrair (valor_principal, acrescimo):
   '''
        Subtrai o acrescimo do valor principal

         Args:
           valor principal (float):
           acrescimo (float): valor a ser subtraído do valor inicial

        Returns:
           float: subtracao do valor principal e acrescimo
    '''
   return valor_principal - acrescimo

def testar_operacao_subtracao ():
   # Arrange
   valor1 = 100.0
   valor2 = 50.0
   # Act
   resultado = subtrair (valor1, valor2)
   # Assert
   assert (resultado == 50.0 ), "A subtracao falhou"
   print ("Teste de subtracao: PASSOU!")

testar_operacao_soma ()
testar_operacao_subtracao ()