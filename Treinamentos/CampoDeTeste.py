notas = input().split()
n1, n2, n3, n4 = float(notas[0]), float(notas[1]), float(notas[2]), float(notas[3])

calculo_media = (n1*2 + n2*3 + n3*4 + n4) / 10
print(f'Media: {calculo_media:.1f}')

if calculo_media >= 7:
    print('Aluno aprovado')
elif calculo_media >= 5.0 and calculo_media <= 6.9:
    print('Aluno em Exame')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    nova_media = (calculo_media + nota_exame) / 2
    if nova_media >= 5.0:
        print('Aluno aprovado')
    else:
        print('Aluno Reprovado')
    print(f'Media final: {nova_media:.1f}')
        
else:
    print('Aluno reprovado')