
def serial_reg(input_var, output_var, n_state):

#implementation of function that check valid states from reduced automata

#function serial receives three input values: input state, output state, number of state

    states = {0:'000', 1:'001', 2:'010', 3:'011', 4:'100', 5:'101', 6:'110', 7:'111'} #create state dictionay
    st = list(states[int(n_state)]) #separate each bit of state
    st[2], st[1] = st[1], st[0] #move bits on second and third positions from left to right
    st[0] = input_var #set the input state at the first position from letf to tight

    ot = (not(int(st[0])) and (not(int(st[1])^(int(st[2]))))) or ((int(st[0])) and ((int(st[1])^(int(st[2]))))) #logical function for odd parity check

    if str(int(ot)) == output_var: #check if output function is equal to output state parameter
        return True #if equal return True
    else:
        return False #if not equl retun False