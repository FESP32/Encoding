import numpy as np
import matplotlib.pyplot as plt

# string = input("Ingresa la cadena: ")
# string = str(string)

strOutput = []
strOutputLabel = []


def output(string):

    contador = 0
    pulso_anterior = 0
    violaciones = 0
    pulso_violacion = 0

    for bit in string:
        if bit == str(1):
            if pulso_anterior == 1:
                strOutput.append(-1)
                strOutputLabel.append(-1)
                pulso_anterior = -1
                pulso_violacion = -1
                violaciones += 1
            elif pulso_anterior == -1:
                strOutput.append(1)
                strOutputLabel.append(1)
                pulso_anterior = 1
            elif pulso_anterior == 0:
                strOutput.append(bit)
                strOutputLabel.append(bit)
                pulso_anterior = int(bit)
        elif bit == str(0):
            contador += 1
            if contador == 4:
                strOutput.pop()
                strOutput.pop()
                strOutput.pop()
                strOutputLabel.pop()
                strOutputLabel.pop()
                strOutputLabel.pop()

                # Check if the number is even

                if violaciones % 2 == 0:
                    #
                    # B00V
                    #
                    pulso_violacion = pulso_anterior * -1
                    strOutput.extend([pulso_violacion, 0, pulso_violacion])
                    strOutputLabel.extend(["B", 0, "V"])
                    violaciones += 1
                    pulso_anterior = pulso_violacion

                # the number is odd

                else:
                    #
                    # 000V
                    #
                    strOutput.extend([0, 0, pulso_violacion])
                    strOutputLabel.extend([0, 0, "V"])
                    violaciones += 1
                contador = 0
            else:
                strOutput.append(bit)
                strOutputLabel.append(bit)


# output()
#
# # Graph
#
# x = np.arange(1, len(strOutput) + 1, 1)
#
# plt.step(x, strOutput)
# plt.xlabel(strOutputLabel)
# plt.xlim(0, len(strOutput))
# plt.ylim(-2, 2)
# plt.title('HDB3 Encoding')
# plt.show()