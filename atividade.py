# Programa Python 3 para encontrar
# pirâmide de altura máxima de
# a largura do objeto fornecida.

# Retorna o número máximo
# de níveis piramidais n
# caixas de larguras fornecidas.
def maxLevel(boxes, n):
	
	# Classificar objetos em aumento
    # ordem de larguras
	boxes.sort()

	ans = 1 # Inicializar resultado

    # Largura total do anterior
    # nível e número total de
    # objetos no nível anterior
	prev_width = boxes[0]
	prev_count = 1

	# Número de objeto em
    # nível atual.
	curr_count = 0

	# Largura do nível atual.
	curr_width = 0
	for i in range(1, n):

		# Escolher o objeto. Então
        # aumenta a largura atual
        # e número do objeto.
		curr_width += boxes[i]
		curr_count += 1

		# Se a largura atual e
        # número de objeto é
        # maior que o anterior.
		if (curr_width > prev_width and
			curr_count > prev_count):

			# Atualize a largura anterior,
            # número de objeto em
            # nível anterior.
			prev_width = curr_width
			prev_count = curr_count

			# Redefina a largura da corrente
            # nível, número de objeto
            # no nível atual.
			curr_count = 0
			curr_width = 0

			# Aumentar o número do nível.
			ans += 1
	return ans

# Código do Driver
if __name__ == "__main__":
	boxes= [10, 20, 30, 50, 60, 70]
	n = len(boxes)
	print(maxLevel(boxes, n))

# Este código foi contribuído
# por ChitraNayal