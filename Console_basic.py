from statemachine import State
from Generator import *
from machines_setup.master import master
from machines_setup.slave import slave
from machines_setup.transition_dict import transitions_dict
from transitions import Transitions_setup



def machines_setup():
    master['states'], master['transitions'] = Transitions_setup(master['form'], master['states'], 'm')
    slave['states'], slave['transitions'] = Transitions_setup(slave['form'], slave['states'], 's')

    global Master, Slave, Node
    Master = Generator.create_master(master['states'], master['transitions'])
    Slave = Generator.create_master(slave['states'], slave['transitions'])
    Node = Master


def display_curr_state():
    print("\033[1;32;1m###################################################\033[0;37;1m")
    print("Znajdujesz się w stanie:  \033[0;31;1m" + Node.current_state.name + "\033[0;37;1m")


def display_possibilities():
    print("\033[1;32;1m###################################################\033[0;37;1m")
    print("Znajdujesz się w stanie:  \033[0;31;1m" +Node.allowed_transitions[0].identifier[2] + " - " + Node.current_state.name + "\033[0;37;1m")
    bufor = []
    for i in range(len(Node.current_state.transitions)):
        x = Node.allowed_transitions[i].identifier[4]
        print("Możliwe przejścia:  \033[0;31;1m" + x + " - " + Node.states[int(x)].name + "\033[0;37;1m")
        bufor.append(x)
    bufor.append("exit")
    #print("Aktualnie stoisz w:\033[0;31;1m", Node.allowed_transitions[i].identifier[2] + "\033[0;37;1m")
    return bufor, Node.allowed_transitions[i].identifier[2]


def change_state(current_dest, goal):
    if Node.allowed_transitions[0].identifier[0] == 'm':
        master['transitions']['m_' + str(current_dest) + '_' + str(goal)]._run(Node)
    else:
        slave['transitions']['s_' + str(current_dest) + '_' + str(goal)]._run(Node)


if __name__ == '__main__':
    machines_setup()
    while True:
        bufor, current_dest = display_possibilities()
        inp = input("Podaj nastepny stan z wyswietlonych: ")
        while inp not in bufor:
            print("\033[0;31;1m" + "Zla sciezka, wybierz ponownie!\n" + "\033[0;37;1m")
            display_possibilities()
            inp = input("Podaj nastepny stan z wyswietlonych: ")
        change = Node.allowed_transitions[0].identifier
        change = change[:4] + str(inp)
        if inp == "exit":
            print("\033[0;31;1m" + "Zakończenie programu" + "\033[0;37;1m")
            break
        elif str(change) == "m_2_3":
            change_state(current_dest, inp)
            Node = Slave
            print("\033[0;33;1m" + "Rozpoczęcie pracy SLAVE" + "\033[0;37;1m")
        elif change == 's_1_4' or change == "s_2_5" or change == "s_3_4" or change == "s_3_5":
            change_state(current_dest, inp)
            slave['transitions']['s_' + str(inp) + '_' + str(0)]._run(Node)
            print("\033[0;33;1m" + "Koniec pracy SLAVE" + "\033[0;37;1m")
            print("\033[0;33;1m" + "Powrót do pracy MASTER" + "\033[0;37;1m")
            Node = Master
        else:
            change_state(current_dest, inp)
