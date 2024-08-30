import math

def calculadora(operacao,op1 = 0, op2 = 0, op3 =0, op4=0):
    match operacao:
        case 'soma':
            return op1 + op2
        
        case 'subtracao':
            return op1 - op2
        
        case 'multiplicacao':
            return op1 * op2
        
        case 'divisao':
            if op2 == 0:
                
                raise ValueError
                
            else:
                return op1 / op2
        
        case 'potenciacao':
                return op1 ** op2
        
        case 'radiciacao':
            if op1 < 0:
                raise ValueError
            else: 
                return op1 ** (1/op2)

        case 'exponencial':
            return math.exp(op1)
        
        case 'modulo':
            return op1 % op2

        case 'divisao_inteira':
            return op1 // op2

        case 'conversao_graus_radianos':
            if op1 == 180:
                return math.pi
            elif op1 == 90:
                return math.pi/2
            
        case 'conversao_radianos_graus':
            if op1 == math.pi:
                return 180
            elif op1 == math.pi/2:
                return 90

        case 'calculo_hipotenusa':
            catetos = ((op1 * op1) + (op2 * op2))
            return pow(catetos, 1/2)
        
        case 'arredondamento':
            return round(op1)

        case 'arredondamento_para_cima':
            return math.ceil(op1)

        case 'arredondamento_para_baixo':
            return math.ceil(op1) - 1 

        case 'maior':
            if op1 > op2:
                return op1
            else:
                return op2
        
        case 'menor':
            if op1 < op2:
                return op1
            else:
                return op2

        case 'distancia_entre_pontos':
            dist = ((op3 - op1) ** 2) + ((op4 - op2) ** 2)
            return pow(dist, 1/2)

        case 'determinante_matriz_2x2':
            deter = (op1 * op4) - (op2 * op3)
            return deter
        
        case 'solucao_equacao_primeiro_grau':
            return math.ceil((op3 - op2)/op1)
        
        case 'area_retangulo':
            return op1 * op2
        
        case 'perimetro_retangulo':
            return 2 * (op1 + op2)
        
        case 'area_circulo':
            return math.pi * op1 * op1
        
        case 'circunferencia_circulo':
            return 2 * math.pi * op1
        
        case 'verificacao_triangulo':
            if (op1 + op2) > op3:
                return True
            else:
                return False

        case 'verificacao_numeros_primos':
            for x in range(2, op1 - 1):
                if (op1 % x) == 0:
                    return False
                    # break
            return True

        # case 'conversor_unidades':
        #     strop3 = str(op3)
        #     match strop3:
        #         case 'milhas_para_km':
        #             return op1 * 1,609
        #         case 'metros_para_pes':
        #             return op1 * 3,281

        case 'juros_simples':
            return op1 * op2 * op3
        
        case 'juros_compostos':
            return ((1 + op2) ** op3) * op1
        
        case 'soma_numeros_naturais':
            for x in range(op1):
                op1 += x
            return op1
        
        case 'fatorial': 
            return math.factorial(op1)

        case 'permutacao':
            return math.factorial(op1)/math.factorial(op2-1)

        case 'combinacao':
            return math.comb(op1, op2)

        # case 'conversor_bases':
        #     ???????

        case 'media':
            return sum(op1)/len(op1)
        
        # case 'desvio_padrao':
        #     ???????

        # case 'tangente_reta':
        #     ??????
        
print(calculadora('media', [10, 20, 30] ))


