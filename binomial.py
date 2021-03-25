# PURPOSE: Take in n, p, k vals and performs a binomial calculation to solve a problem
from math import factorial as fac
import PySimpleGUIQt as sg

def binomial(n,p,k):
    prob = fac(n) / (fac(k) * fac(n - k)) * p**k * (1-p)**(n-k)
    return prob

def calcProb(n,p,k,op):
    prob = 0
    if op == '=':
        prob = binomial(n,p,k)
    elif op == '<':
        prob = 0
        for i in range(0,k):
            prob += binomial(n,p,i)
    elif op == '<=':
        for i in range(0,k+1):
            prob += binomial(n,p,i)
    elif op == '>':
        prob = 0
        for i in range(k+1,n+1):
            prob += binomial(n,p,i)
    elif op == '>=':
        prob = 0
        for i in range(k,n+1):
            prob += binomial(n,p,i)
    return prob


r_keys= ['=','<','<=','>','>=']
sg.change_look_and_feel('DarkBlue1') #colour
layout = [
    [sg.Text('| -N- | Sample space:'), sg.InputText(key='-N-')],
    [sg.Text('| -P- | Success rate: '), sg.InputText(key='-P-')],
    [sg.Text('| -K- | Number of successes:'), sg.InputText(key='-K-')],
    [sg.Text('Choose an operation: ')],
    [sg.Radio('=', 1, key=r_keys[0], default = True),
        sg.Radio('<', 1, key=r_keys[1]),
        sg.Radio('<=', 1, key=r_keys[2]),
        sg.Radio('>', 1, key=r_keys[3]),
        sg.Radio('>=', 1, key=r_keys[4])],
    [sg.Button('Calculate'), sg.Button('Clear'), sg.Button('Exit')],
    [sg.Output(size=(30,10), key='_output_')]
]
window = sg.Window('Binomial Calculator', layout) #makes window

while True:
    event, values = window.read()

    n = values['-N-']
    p = values['-P-']
    k = values['-K-']
    op = [ key for key in r_keys if values[key]][0] 

    if event in (None, 'Exit'):
        window.close()
    if event == 'Calculate':
        try:
            print(calcProb(int(n),float(p),int(k),op))
        except:
            print("Missing values")
    if event == 'Clear':
        window.FindElement('_output_').Update('') #clears element

 