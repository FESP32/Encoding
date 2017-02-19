import matplotlib.pyplot as plt
import numpy as np
import ManchesterEncoding as me
import HDB3 as hd
import B3ZS as b3

user_input = raw_input("binary strings: ")
# original
original_string = []
for i in user_input:
    original_string.append(int(i) + 2)

# manchester
manchester_data = me.binarystring_to_list(me.manchester_encoding(user_input))

# hdb3
hd.output(user_input)
hdb3_string = hd.strOutput
hdb3_data = []
for i in hdb3_string:
    i = int(i) - 2
    hdb3_data.append(i)

# b3zs
b3.output(user_input)
b3zs_string = b3.strOutput
b3zs_data = []
for i in b3zs_string:
    i = int(i) - 5
    b3zs_data.append(i)

# original plot
x = np.arange(1, len(original_string) + 1, 1)
plt.step(x, original_string, label='Original')

# manchester plot
x = np.arange(1, len(manchester_data) + 1, 1)
plt.step(x, manchester_data, label='Manchester')

# hdb3 plot
x = np.arange(1, len(hdb3_data) + 1, 1)
plt.step(x, hdb3_data, label='HDB3')

# b3zs plot
x = np.arange(1, len(b3zs_data) + 1, 1)
plt.step(x, b3zs_data, label='B3ZS')


plt.xlim(0, len(manchester_data) + 1)
plt.ylim(-7, 5)
plt.legend()
plt.title('Manchester, HDB3 & B3ZS Encoding')
plt.show()








