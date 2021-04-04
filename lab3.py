import lab2_new
import math

CONST_T = 2027
KR1 = 2
KR2 = 2


def get_T(t, p_sys):
    return round((-1) * t / math.log(p_sys))


def get_g_(revsys, sys):
    return round(revsys / sys, 2)


def pr_reverse_result(p, q, t):
    print("P-reverse ", p)
    print("Q-reverse ", q)
    print("T-reverse ", t)


def pr_winning_reliability(q, p, t):
    print("G_q = ", q)
    print("G_p = ", p)
    print("G_t = ", t)


def common_(parameter, K):
    print('Common', parameter, '->')
    print("-" * 16)
    if parameter == 'load':
        p_revsystem = 1 - math.pow(1 - p_system, K + 1)
        q_revsystem = 1 - p_revsystem
    elif parameter == 'unload':
        q_revsystem = q_system / math.factorial(K + 1)
        p_revsystem = 1 - q_revsystem
    else:
        print("Choose the right parameter!")
        return

    t_revsystem = get_T(CONST_T, p_revsystem)
    pr_reverse_result(p_revsystem, q_revsystem, t_revsystem)

    g_q = get_g_(q_revsystem, q_system)
    g_p = get_g_(p_revsystem, p_system)
    g_t = get_g_(t_revsystem, t_system)
    pr_winning_reliability(g_q, g_p, g_t)


def distribute_(parameter, K):
    newP = []
    newQ = []
    print('Distribute', parameter, '->')
    print("-" * 20)

    if parameter == 'load':
        for i in range(len(lab2_new.P)):
            newP.append(1 - math.pow(1 - lab2_new.P[i], K + 1))
            newQ.append(1 - newP[i])
    elif parameter == 'unload':
        for i in range(len(lab2_new.P)):
            newP.append(1 - (1 - lab2_new.P[i]) / math.factorial(K + 1))
            newQ.append(1 - newP[i])
    else:
        print("Choose the right parameter!")
        return

    lab2_new.P = newP
    p_revsystem = lab2_new.calculate_probability(lab2_new.work_path, lab2_new.scheme_size)

    q_revsystem = 1 - p_revsystem
    t_revsystem = get_T(CONST_T, p_revsystem)
    pr_reverse_result(p_revsystem, q_revsystem, t_revsystem)

    g_q = get_g_(q_revsystem, q_system)
    g_p = get_g_(p_revsystem, p_system)
    g_t = get_g_(t_revsystem, t_system)
    pr_winning_reliability(g_q, g_p, g_t)


def do_task(task):
    print("_" * 40)
    if task[0] == 'common':
        common_(parameter=task[1], K=task[2])
    elif task[0] == 'distribute':
        distribute_(parameter=task[1], K=task[2])


if __name__ == '__main__':
    task1 = ['common', 'load', KR1]
    task2 = ['common', 'unload', KR2]

    p_system = lab2_new.p_system
    q_system = 1 - p_system
    t_system = get_T(CONST_T, p_system)
    print("P-system: ", p_system)
    print("Q-system: ", q_system)
    print("T-system: ", t_system)

    do_task(task1)
    do_task(task2)
