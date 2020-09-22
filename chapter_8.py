if __name__ == '__main__':
    def example(xmpl):
        """example"""
        print(f"Example {xmpl}")

    # def full_name(first_name, last_name, middle_name=''):
    #     """full information"""
    #     if middle_name:
    #         full = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    #     else:
    #         full = f"{first_name.title()} {last_name.title()}"
    #     return full
    # name = full_name('aliaksei', 'markevich')
    # print(name)
    # name_2 =full_name('aliaksei', 'markevich', 'vladimirovich')
    # print(name_2)

    my_name = 'aliaksei'
    my_last = 'markevich'
    my_age = 28
    # def name_in_dict(first_name, last_name, age=''):
    #     persone = {'first': first_name, 'last': last_name}
    #     if age:
    #         persone['age'] = age
    #     return  persone
    # print(name_in_dict(my_name, my_last, my_age))

    # def full (first_name, last_name):
    #     full_name = f"{first_name} {last_name}"
    #     return full_name.title()
    # while True:
    #     print("\nEnter 'q' for any time to quit")
    #     print("Please tell me your name :D")
    #     f_name = input("First name: ")
    #     if f_name == 'q':
    #         break
    #     l_name = input("Last name: ")
    #     if l_name == 'q':
    #         break
    #     full_name = full(f_name, l_name)
    #     print(f"Hello {full_name.title()}!!!")

    # def print_models(unprinted_designs, complete_models):
    #     while unprinted_designs:
    #         current_design = unprinted_designs.pop()
    #         print(f"Printing model: {current_design.title()}")
    #         complete_models.append(current_design)
    #
    # def show_completed(completed_models):
    #     print("\nCompleted models:")
    #     for completed_model in completed_models:
    #         print(completed_model.title())
    #
    # designes = ['car', 'ball', 'phone case']
    # completed = []
    # print_models(designes[:], completed)
    # show_completed(completed)

    # def make_pizza(*toppings):
    #     """Вывод списка заказанных дополнений."""
    #     print("\nMaking a pizza with the following toppings:")
    #     for topping in toppings:
    #         print(f"- {topping}")
    # make_pizza('pepperoni')
    # make_pizza('mushrooms', 'green peppers', 'extra cheese')

    # user info
    # def build_profile(first, last, **user_info):
    #     """Словарь с информацией о пользователе"""
    #     profile = {}
    #     profile['first'] = first
    #     profile['last'] = last
    #     for k, v in user_info.items():
    #         profile[k] = v
    #     return profile
    #
    #
    # user_profile = build_profile('albert', 'einstein',
    #                              location='princeton',
    #                              field='physics')
    # print(user_profile)
    