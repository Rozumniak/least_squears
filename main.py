from sympy import symbols, exp, solve

x_list_val = [0.2, 0.3, 0.4, 0.6, 0.8, 0.9, 1.0, 1.2]
y_list_val = [1.4, 1.2, 1.1, 1.6, 2.0, 2.1, 2.3, 2.5]

def least_squares():
    x = symbols('x')
    c0, c1, c2 = symbols('c0 c1 c2')

    n = len(x_list_val) - 1

    x_sum = sum(x_list_val)

    x_sq_sum = 0
    x_sq_list = []
    for i, value in enumerate(x_list_val):
        x_sq_sum += value ** 2
        x_sq_list.append(value ** 2)

    x_qb_sum = 0
    x_qb_list = []
    for i, value in enumerate(x_list_val):
        x_qb_sum += value ** 3
        x_qb_list.append(value ** 3)

    x_4th_sum = 0
    x_4th_list = []
    for i, value in enumerate(x_list_val):
        x_4th_sum += value ** 4
        x_4th_list.append(value ** 4)

    x_5th_sum = 0
    x_5th_list = []
    for i, value in enumerate(x_list_val):
        x_5th_sum += value ** 5
        x_5th_list.append(value ** 5)

    y_sum = sum(y_list_val)

    yx_sum = 0
    yx_list = []
    for x_value, y_value in zip(x_list_val, y_list_val):
        yx_sum += y_value * x_value
        yx_list.append(y_value * x_value)

    yx_sq_sum = 0
    yx_sq_list = []
    for x_value, y_value in zip(x_list_val, y_list_val):
        yx_sq_sum += y_value * (x_value ** 2)
        yx_sq_list.append(y_value * (x_value ** 2))

    yx_qb_sum = 0
    yx_qb_list = []
    for x_value, y_value in zip(x_list_val, y_list_val):
        yx_qb_sum += y_value * (x_value ** 3)
        yx_qb_list.append(y_value * (x_value ** 3))

    e_x_sum = 0
    e_x_list = []
    for i, x_value in enumerate(x_list_val):
        e_x_sum += exp(x_value)
        e_x_list.append(exp(x_value))

    xe_x_sum = 0
    xe_x_list = []
    for i, x_value in enumerate(x_list_val):
        xe_x_sum += x_value * exp(x_value)
        xe_x_list.append(x_value * exp(x_value))

    e_2x_sum = 0
    e_2x_list = []
    for i, x_value in enumerate(x_list_val):
        e_2x_sum += exp(2 * x_value)
        e_2x_list.append(exp(2 * x_value))

    ye_x_sum = 0
    ye_x_list = []
    for x_value, y_value in zip(x_list_val, y_list_val):
        ye_x_sum += y_value * exp(x_value)
        ye_x_list.append(y_value * exp(x_value))


    # ____________ 1ша система _______________

    equations_phi_1 = [
        c0 * (n + 1) + c1 * x_sum - y_sum,
        c0 * x_sum + c1 * x_sq_sum - yx_sum
    ]
    print(f"Система рівнянь до розв'язання:\n"
          f"{equations_phi_1[0]}\n"
          f"{equations_phi_1[1]}\n")

    solutions = solve(equations_phi_1, (c0, c1))
    c_0 = solutions[c0]
    c_1 = solutions[c1]
    print(f"Знайдені коефіцієнти С0 = {c_0}, С1 = {c_1}")
    phi_1 = c_0 + c_1 * x
    print(f"Рівняння фі_1: {phi_1}\n")

    # ____________ 2га система _______________

    equations_phi_2 = [
        c0 * (n + 1) + c1 * x_sum + c2 * x_sq_sum - y_sum,
        c0 * x_sum + c1 * x_sq_sum + c2 * x_qb_sum - yx_sum,
        c0 * x_sq_sum + c1 * x_qb_sum + c2 * x_4th_sum - yx_sq_sum
    ]

    print(f"Система рівнянь до розв'язання:\n"
          f"{equations_phi_2[0]}\n"
          f"{equations_phi_2[1]}\n"
          f"{equations_phi_2[2]}\n")

    solutions = solve(equations_phi_2, (c0, c1, c2))
    c_0 = solutions[c0]
    c_1 = solutions[c1]
    c_2 = solutions[c2]

    print(f"Знайдені коефіцієнти С0 = {c_0}, С1 = {c_1}, С2 = {c_2}")
    phi_2 = c_0 + c_1 * x + c_2 * (x ** 2)
    print(f"Рівняння фі_2: {phi_2}\n")

    # ____________ 3тя система _______________

    equations_phi_3 = [
        c0 * (n + 1) + c1 * x_sum + c2 * x_qb_sum - y_sum,
        c0 * x_sum + c1 * x_qb_sum + c2 * x_4th_sum - yx_sum,
        c0 * x_qb_sum + c1 * x_4th_sum + c2 * x_5th_sum - yx_sq_sum
    ]
    print(f"Система рівнянь до розв'язання:\n"
          f"{equations_phi_3[0]}\n"
          f"{equations_phi_3[1]}\n"
          f"{equations_phi_3[2]}\n")

    solutions = solve(equations_phi_3, (c0, c1, c2))
    c_0 = solutions[c0]
    c_1 = solutions[c1]
    c_2 = solutions[c2]
    print(f"Знайдені коефіцієнти С0 = {c_0}, С1 = {c_1}, С2 = {c_2}")
    phi_3 = c_0 + c_1 * x + c_2 * (x ** 3)
    print(f"Рівняння фі_3: {phi_3}\n")

    # ____________ 4та система _______________

    equations_phi_4 = [
        c0 * (n + 1) + c1 * x_sum + c2 * e_x_sum - y_sum,
        c0 * x_sum + c1 * x_sq_sum + c2 * xe_x_sum - yx_sum,
        c0 * e_x_sum + c1 * xe_x_sum + c2 * e_2x_sum - ye_x_sum
    ]
    print(f"Система рівнянь:\n"
          f"{c0 * (n + 1) + c1 * x_sum + c2 * e_x_sum - y_sum}\n"
          f"{c0 * x_sum + c1 * x_sq_sum + c2 * xe_x_sum - yx_sum}\n"
          f"{c0 * e_x_sum + c1 * xe_x_sum + c2 * e_2x_sum - ye_x_sum}\n")

    solutions = solve(equations_phi_4, (c0, c1, c2))
    c_0 = solutions[c0]
    c_1 = solutions[c1]
    c_2 = solutions[c2]
    print(f"Знайдені коефіцієнти С0 = {c_0}, С1 = {c_1}, С2 = {c_2}")

    exp_x = symbols('exp_x')
    phi_4 = c_0 + c_1 * x + c_2 * exp(x)
    print(f"Рівняння фі_4: {c_0 + c_1 * x + c_2 * exp_x}\n")

    phi_1_list = []
    phi_2_list = []
    phi_3_list = []
    phi_4_list = []

    delta_phi_1_list = []
    delta_phi_2_list = []
    delta_phi_3_list = []
    delta_phi_4_list = []

    delta_phi_1_sq_list = []
    delta_phi_2_sq_list = []
    delta_phi_3_sq_list = []
    delta_phi_4_sq_list = []

    for i, value in enumerate(x_list_val):
        phi_1_val = phi_1.subs([(x, x_list_val[i])])
        phi_1_list.append(phi_1_val)
        delta_phi_1_list.append(y_list_val[i] - phi_1_val)
        delta_phi_1_sq_list.append((y_list_val[i] - phi_1_val) ** 2)

        phi_2_val = phi_2.subs([(x, x_list_val[i])])
        phi_2_list.append(phi_2_val)
        delta_phi_2_list.append(y_list_val[i] - phi_2_val)
        delta_phi_2_sq_list.append((y_list_val[i] - phi_2_val) ** 2)

        phi_3_val = phi_3.subs([(x, x_list_val[i])])
        phi_3_list.append(phi_3_val)
        delta_phi_3_list.append(y_list_val[i] - phi_3_val)
        delta_phi_3_sq_list.append((y_list_val[i] - phi_3_val) ** 2)

        phi_4_val = phi_4.subs([(x, x_list_val[i])])
        phi_4_list.append(phi_4_val)
        delta_phi_4_list.append(y_list_val[i] - phi_4_val)
        delta_phi_4_sq_list.append((y_list_val[i] - phi_4_val) ** 2)


    # print("Початкові та проміжні результати розрахунків за методом найменших квадратів:\n")
    # print("Значення для x^2 - x^5:")
    # print("{:<1} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |".format("№", "x", "y", "x^2", "x^3", "x^4", "x^5"))
    # print("_________________________________________________________________________________")
    #
    # for i in range(len(x_list_val)):
    #     i_val = i + 1
    #     x_val = "{:<10.4f}".format(x_list_val[i])
    #     y_val = "{:<10.4f}".format(y_list_val[i])
    #     x_sq_val = "{:<10.4f}".format(x_sq_list[i])
    #     x_qb_val = "{:<10.4f}".format(x_qb_list[i])
    #     x_4th_val = "{:<10.4f}".format(x_4th_list[i])
    #     x_5th_val = "{:<10.4f}".format(x_5th_list[i])
    #     print("{} | {} | {} | {} | {} | {} | {} | ".format(i_val, x_val, y_val, x_sq_val, x_qb_val, x_4th_val, x_5th_val))
    # print("_________________________________________________________________________________")
    #
    # print("{:<1} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |"
    #           .format(f"E", f"{round(x_sum, 4)}",
    #                   f"{round(y_sum, 4)}",
    #                   f"{round(x_sq_sum, 4)}",
    #                   f"{round(x_qb_sum, 4)}",
    #                   f"{round(x_4th_sum, 4)}",
    #                   f"{round(x_5th_sum, 4)}",))
    # print("_________________________________________________________________________________")
    #
    # print("\nЗначення для yx - yx^3, y*exp(x)")
    # print("_________________________________________________________________________________")
    # print("{:<1} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |".format("№", "x", "y", "yx", "yx^2", "yx^3", "y*exp(x)"))
    # print("_________________________________________________________________________________")
    # for i in range(len(x_list_val)):
    #     i_val = i + 1
    #     x_val = "{:<10.4f}".format(x_list_val[i])
    #     y_val = "{:<10.4f}".format(y_list_val[i])
    #     yx_val = "{:<10.4f}".format(yx_list[i])
    #     yx_sq_val = "{:<10.4f}".format(yx_sq_list[i])
    #     yx_qb_val = "{:<10.4f}".format(yx_qb_list[i])
    #     ye_x_val = "{:<10.4f}".format(ye_x_list[i])
    #     print(
    #         "{} | {} | {} | {} | {} | {} | {} | ".format(i_val, x_val, y_val, yx_val, yx_sq_val, yx_qb_val, ye_x_val))
    # print("_________________________________________________________________________________")
    # print("{:<1} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |"
    #           .format(f"E", f"{round(x_sum, 4)}",
    #                   f"{round(y_sum, 4)}",
    #                   f"{round(yx_sum, 4)}",
    #                   f"{round(yx_sq_sum, 4)}",
    #                   f"{round(yx_qb_sum, 4)}",
    #                   f"{round(ye_x_sum, 4)}", ))
    # print("_________________________________________________________________________________")
    #
    #
    # print("\nЗначення для exp(x), exp(2x), x * exp(x):")
    # print("____________________________________________________________________")
    # print("{:<1} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |"
    #       .format("№", "x", "y", "exp(x)", "exp(2x)", "x * exp(x)"))
    # print("____________________________________________________________________")
    # for i in range(len(x_list_val)):
    #     i_val = i + 1
    #     x_val = "{:<10.4f}".format(x_list_val[i])
    #     y_val = "{:<10.4f}".format(y_list_val[i])
    #     e_x_val = "{:<10.4f}".format(e_x_list[i])
    #     e_2x_val = "{:<10.4f}".format(e_2x_list[i])
    #     xe_x_val = "{:<10.4f}".format(xe_x_list[i])
    #     print(
    #         "{} | {} | {} | {} | {} | {} |".format(i_val, x_val, y_val, e_x_val, e_2x_val, xe_x_val))
    # print("____________________________________________________________________")
    # print("{:<1} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |"
    #       .format(f"E", f"{round(x_sum, 4)}",
    #               f"{round(y_sum, 4)}",
    #               f"{round(e_x_sum, 4)}",
    #               f"{round(e_2x_sum, 4)}",
    #               f"{round(xe_x_sum, 4)}"))
    # print("____________________________________________________________________")
    #
    # print("\nЗначення для фі1 - фі4:")
    # print("_________________________________________________________________________________")
    # print("{:<1} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |".format("№", "x", "y", "фі1", "фі2", "фі3",
    #                                                                              "фі4"))
    # print("_________________________________________________________________________________")
    # for i in range(len(x_list_val)):
    #     i_val = i + 1
    #     x_val = "{:<10.4f}".format(x_list_val[i])
    #     y_val = "{:<10.4f}".format(y_list_val[i])
    #     phi_1_val = "{:<10.4f}".format(phi_1_list[i])
    #     phi_2_val = "{:<10.4f}".format(phi_2_list[i].evalf())
    #     phi_3_val = "{:<10.4f}".format(phi_3_list[i].evalf())
    #     phi_4_val = "{:<10.4f}".format(phi_4_list[i].evalf())
    #
    #     print(
    #         "{} | {} | {} | {} | {} | {} | {} | ".format(i_val, x_val, y_val, phi_1_val, phi_2_val, phi_3_val, phi_4_val))
    # print("_________________________________________________________________________________")
    #
    # print("{:<1} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |"
    #       .format(f"E", f"{round(x_sum, 4)}",
    #               f"{round(y_sum, 4)}",
    #               f"{round(sum(phi_1_list), 4)}",
    #               f"{round(sum(phi_2_list), 4)}",
    #               f"{round(sum(phi_3_list), 4)}",
    #               f"{round(sum(phi_4_list), 4)}"))
    # print("_________________________________________________________________________________\n")
    #
    # print("Значення для (у - фі1) - (у - фі4)")
    # print("_________________________________________________________________________________")
    # print("{:<1} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |".format("№", "x", "y", "у - фі1", "у - фі2", "у - фі3",
    #                                                                              "у - фі4"))
    # print("_________________________________________________________________________________")
    # for i in range(len(x_list_val)):
    #     i_val = i + 1
    #     x_val = "{:<10.4f}".format(x_list_val[i])
    #     y_val = "{:<10.4f}".format(y_list_val[i])
    #     delta_phi_1_val = "{:<10.4f}".format(delta_phi_1_list[i])
    #     delta_phi_2_val = "{:<10.4f}".format(delta_phi_2_list[i])
    #     delta_phi_3_val = "{:<10.4f}".format(delta_phi_3_list[i])
    #     delta_phi_4_val = "{:<10.4f}".format(delta_phi_4_list[i])
    #
    #     print(
    #         "{} | {} | {} | {} | {} | {} | {} | ".format(i_val, x_val, y_val, delta_phi_1_val, delta_phi_2_val, delta_phi_3_val, delta_phi_4_val))
    # print("_________________________________________________________________________________")
    # print("{:<1} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |"
    #           .format(f"E", f"{round(x_sum, 4)}",
    #                   f"{round(y_sum, 4)}",
    #                   f"{round(sum(delta_phi_1_list), 4)}",
    #                   f"{round(sum(delta_phi_2_list), 4)}",
    #                   f"{round(sum(delta_phi_3_list), 4)}",
    #                   f"{round(sum(delta_phi_4_list), 4)}"))
    # print("_________________________________________________________________________________\n")

    print("Значення для (у - фі1)^2 - (у - фі4)^2:")
    print("_____________________________________________________________________________________")
    print("{:<1} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |".format("№", "x", "y", "(у - фі1)^2",
                                                                         "(у - фі2)^2", "(у - фі3)^2", "(у - фі4)^2"))
    print("_____________________________________________________________________________________")
    for i in range(len(x_list_val)):
        i_val = i + 1
        x_val = "{:<10.4f}".format(x_list_val[i])
        y_val = "{:<10.4f}".format(y_list_val[i])
        delta_phi_1_sq_val = "{:<10.4f}".format(delta_phi_1_sq_list[i])
        delta_phi_2_sq_val = "{:<10.4f}".format(delta_phi_2_sq_list[i])
        delta_phi_3_sq_val = "{:<10.4f}".format(delta_phi_3_sq_list[i])
        delta_phi_4_sq_val = "{:<10.4f}".format(delta_phi_4_sq_list[i])
        print(
            "{} | {} | {} | {} | {} | {} | {} | ".format(i_val, x_val, y_val, delta_phi_1_sq_val, delta_phi_2_sq_val, delta_phi_3_sq_val, delta_phi_4_sq_val))
    print("_________________________________________________________________________________")
    print("{:<1} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} | {:<10} |"
          .format(f"E", f"{round(x_sum, 4)}",
                  f"{round(y_sum, 4)}",
                  f"{round(sum(delta_phi_1_sq_list), 4)}",
                  f"{round(sum(delta_phi_2_sq_list), 4)}",
                  f"{round(sum(delta_phi_3_sq_list), 4)}",
                  f"{round(sum(delta_phi_4_sq_list), 4)}"))
    print("_________________________________________________________________________________\n")



def main():
    print("Комп'ютерний практикум №6 \nВаріант №11 \nРозумняк Руслан ")
    print("\n________Метод Найменших квадратів________")
    least_squares()
if __name__ == '__main__':
    main()