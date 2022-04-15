from textwrap import wrap
from turtle import width

def caixa(frase, width):
    print('+-' + '-' * width + '-+')
    for line in wrap(frase, width):
        print('| {0:^{1}} |'.format(line, width))
        print('+-' + '-'*(width) + '-+')