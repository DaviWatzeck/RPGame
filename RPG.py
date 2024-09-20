import random
import time

# Creator: Davi Watzeck Souza
# Code: Davi Watzeck Souza
# Logic : Davi Watzeck Souza
#


# Configurações
base_loot_chances = {
    'gold': 0.5,  # Probabilidade base de 50%
    'hp_potion': 0.35,  # Probabilidade base de 35%
    'mp_potion': 0.15,  # Probabilidade base de 15%
    'pedra_forja': 0.17,  # Probabilidade base de 17%
    'pedra_ressureicao': 0.09  # Probabilidade base de 09%
}

base_amounts = {
    'gold': 10,
    'hp_potion': 3,
    'mp_potion': 2,
    'pedra_forja': 1,
    'pedra_ressureicao': 1
}


prefixos = ['Kra', 'Zor', 'Vel', 'Mor', 'Tor', 'Gor', 'Fen', 'Drak', 'Lug', 'Vex', 'Ser', 'Thal', 'Bru', 'Mal']
meios = ['ra', 'lo', 'mo', 'zi', 'ka', 'ro', 'ba', 'fi', 'zu', 'ter', 'dor', 'gir']
sufixos = ['gath', 'dor', 'nak', 'rith', 'zan', 'lox', 'moth', 'vor', 'rak', 'gorn', 'tuk', 'kash']

village_name = "Vila Endllage"
npc_julie = "Julie - A treinadora:"
ancient_name = "Nyan - O ancião:"
npc_merchant = "Bueli - O mercante:"
npc_forger = "Tyson - O ferreiro:"

current_health = float(100)
current_mana = float(20)

health_max = float(100)
mana_max = float(20)
strength = float(10)
defense = float(10)


player_level = 1
xp = 0
xp_next_level = 10
gold = 0
hp_pot = 0
mp_pot = 0

armas_atributos = {
    'Peitoral de ferro fundido': {'defesa': 80},
    'Clava de titânio': {'ataque': 50, 'defesa': 50, 'chance_critico_arma': 0},
    'Espada de titânio': {'ataque': 45, 'defesa': 50, 'chance_critico_arma': 0},
    'Machado de titânio': {'ataque': 55, 'defesa': 40, 'chance_critico_arma': 0},
    'Peitoral de aço': {'defesa': 40},
    'Clava de ferro': {'ataque': 25, 'defesa': 25, 'chance_critico_arma': 0},
    'Espada de ferro': {'ataque': 20, 'defesa': 30, 'chance_critico_arma': 0},
    'Machado de ferro': {'ataque': 30, 'defesa': 20, 'chance_critico_arma': 0},
    'Peitoral de ferro': {'defesa': 30},
    'Clava de pedra': {'ataque': 10, 'defesa': 10, 'chance_critico_arma': 0},
    'Espada de pedra': {'ataque': 8, 'defesa': 12, 'chance_critico_arma': 0},
    'Machado de pedra': {'ataque': 12, 'defesa': 8, 'chance_critico_arma': 0},
    'Peitoral de pano': {'defesa': 10},
    'Clava de madeira': {'ataque': 5, 'defesa': 5, 'chance_critico_arma': 0},
    'Espada de madeira': {'ataque': 4, 'defesa': 6, 'chance_critico_arma': 0},
    'Machado de madeira': {'ataque': 6, 'defesa': 4, 'chance_critico_arma': 0}
}


itens_disponiveis_npc_merchant = {
    'Peitoral de ferro fundido': 105,
    'Clava de titânio': 95,
    'Espada de titânio': 95,
    'Machado de titânio': 95,
    'Peitoral de aço': 55,
    'Clava de ferro': 45,
    'Espada de ferro': 45,
    'Machado de ferro': 45,
    'Peitoral de ferro': 25,
    'Clava de pedra': 15,
    'Espada de pedra': 15,
    'Machado de pedra': 15,
    'Peitoral de pano': 5,
    'Clava de madeira': 5,
    'Espada de madeira': 5,
    'Machado de madeira': 5
}

primeira_visita = True
first_monster = True
first_forge = True

armaduras_compradas = []
armas_compradas = []

armadura_equipada = None
arma_equipada = None
pedra_forja = 0
pedra_ressureicao = 0
dano_arma = 0
defesa_arma = 0
chance_critico_arma = 0


def create_monster_name():
    prefixo = random.choice(prefixos)
    meio = random.choice(meios) if random.random() > 0.5 else ''
    sufixo = random.choice(sufixos)
    return prefixo + meio + sufixo


def create_monster_level():
    if first_monster is True:
        monster_level = random.randint(1, 1)
        hp_monster = random.randint(25, 30)
        strength_monster = random.randint(1, 10)
        defense_monster = random.randint(1, 10)
        xp_monster = random.randint(50, 75)
    else:
        monster_level = random.randint(max(1, player_level - 2), player_level + 2)
        hp_monster = random.randint(25, 50) * monster_level
        strength_monster = random.randint(1, 15) * monster_level
        defense_monster = random.randint(1, 15) * monster_level
        xp_monster = random.randint(20, 50) * monster_level
    return monster_level, hp_monster, strength_monster, defense_monster, xp_monster


def generate_random_monster():
    head = random.choice(['  ,_,  ', '  @.@  ', '  *-*  ', '  o.o  ', '  ^_^  '])
    eyes = random.choice([' (o_o)', ' (O_O)', ' (-.-)', ' (*_*)', ' (x_x)'])
    mouth = random.choice(['  \\_/  ', '  ~.~  ', '  [-]  ', '  ._.  ', '  ^_^  '])
    arms = random.choice(['  /|\\  ', '  \\|/  ', '  |||  ', '  /-\\  ', '  \\-/  '])
    body = random.choice(['  /|\\  ', '  |#|  ', '  |-o-|', '  |-|  ', '  ( )  '])
    legs = random.choice(['  / \\  ', '  | |  ', '  ||   ', ' /   \\ ', '  \\_/  '])

    # Montar o monstro
    monster_visual = f"""
    {head}
    {eyes}
    {mouth}
    {arms}
    {body}
    {legs}
    """
    return monster_visual


def generate_loot(monster_level):
    loot = {}
    for item, base_chance in base_loot_chances.items():
        # Calcula a chance de loot baseada no nível do monstro
        chance = min(base_chance + (monster_level * 0.01), 1.0)  # Aumenta a chance e limita a 100%

        # Calcula a quantidade do item baseada no nível do monstro
        base_amount = base_amounts[item]
        increased_amount = min(base_amount + int(base_amount * (monster_level * 0.02)), base_amount * 2)  # Limita a quantidade ao dobro do máximo base

        # Verifica se o item vai dropar
        if random.random() < chance:
            loot[item] = random.randint(1, increased_amount)  # Quantidade aleatória do item

    return loot


def format_item_name(item):
    # Formata o nome do item com base no tipo de item
    item_names = {
        'gold': "Moedas de Ouro",
        'mp_potion': "Poção de Mana",
        'hp_potion': "Poção de Vida",
        'pedra_forja': "Pedra de Forja",
        'pedra_ressureicao': "Pedra de Ressureicao"
    }
    return item_names.get(item, item.capitalize())


def update_attributes(strength, defense, health_max, mana_max):
    new_strength = strength * 1.05
    new_defense = defense * 1.07
    new_health_max = health_max * 1.12
    new_mana_max = mana_max * 1.08
    return new_strength, new_defense, new_health_max, new_mana_max


def player_name_choice():
    player_name = input('Digite seu nome: ')
    resposta = input('Você tem certeza que quer ficar com esse nome? Sim ou não?: ').upper()
    if resposta == 'SIM' or resposta == 'S':
        return player_name
    elif resposta == 'NÃO' or resposta == 'N' or resposta == 'NAO':
        print('Vamos escolher um novo nome...')
        return player_name_choice()
    else:
        print('Resposta inválida. Tente novamente.')
        return player_name_choice()


def tutorial_choice():
    tutorial = input(f"{npc_julie} Você deseja fazer o tutorial? (Sim/não): "
                     "\n")
    time.sleep(2)
    if tutorial.upper() == 'SIM' or tutorial.upper() == 'S':
        return True
    elif tutorial.upper() == 'NÃO' or tutorial.upper() == 'N' or tutorial.upper() == 'NAO':
        print('Vamos começar a aventura!')
        return False
    else:
        print('Resposta inválida. Tente novamente.')
        tutorial_choice()


def tutorial_gameplay():
    print(f"{npc_julie} Bom vamos lá... a {village_name} foi fundada há 15 anos atrás...")
    time.sleep(5)
    print(f"{npc_julie} nosso glorioso ancião que fez tudo isso, ele continua"
          "\nconstruindo a nossa vila e permitindo que nossa raça evolua"
          "\nmais do que qualquer uma...")
    time.sleep(5)
    print(f'{npc_julie} como a vila é "Recém fundada", temos poucos lugares'
          '\nque você pode ir aqui, temos a Igreja, a Forja, a Loja de equipamentos e a Torre do conhecimento')
    time.sleep(5)
    print(f'{npc_julie} A igreja é um local onde você pode ser curado de envenenamentos'
          '\ne também poder comprar pots de cura e de mana')
    time.sleep(5)
    print(f'{npc_julie} A Forja é um lugar onde você pode melhorar seus equipamentos!')
    time.sleep(5)
    print(f'{npc_julie} A Loja de equipamentos é um lugar onde você'
          '\npode comprar armaduras, escudos, e outros equipamentos')
    time.sleep(5)
    print(f'{npc_julie} A Torre do conhecimento é um lugar onde você pode'
          '\nconseguir aprender novas habilidades, sejam elas de suporte,'
          '\nde ataque e aumento de skills temporárias')
    time.sleep(5)
    print(f'{npc_julie} E por fim você pode ir para a floresta, onde você'
          '\nencontra inimigos, matando eles, eles tem incríveis loots'
          '\nsejam moedas de ouro, peças de armaduras, pots de vida e até mesmo pedras de ressureição. ')
    time.sleep(7)
    print(f'{npc_julie} Você já está pronto para começar!')
    storygame()


def merchant_offer():
    print('Itens disponíveis:')
    for idx, (item, preco) in enumerate(itens_disponiveis_npc_merchant.items(), start=1):
        print(f'{idx}. {item:<20} {preco:>02}$')
    print(f'Você tem: {gold}$')


def buy_itens():
    global gold
    global primeira_visita

    while True:
        print('\n')
        print(f'{npc_merchant} Vai querer algo?')
        resposta = input('Sim ou não? ').upper()
        if resposta == 'SIM' or resposta == 'S':
            merchant_offer()
            idx_item = int(input('Digite o número do item: '))
            if idx_item in range(1, len(itens_disponiveis_npc_merchant) + 1):
                item, preco = list(itens_disponiveis_npc_merchant.items())[idx_item - 1]
                if item in ['Espada de madeira', 'Machado de madeira', 'Clava de madeira'] and primeira_visita:
                    if not any(i in ['Peitoral de pano'] for i in armaduras_compradas):
                        print('Você precisa comprar uma armadura antes de comprar uma arma.')
                        continue

                if gold >= preco:
                    gold -= preco
                    print(f'Você comprou {item} por {preco}$')
                    print(f'Você tem {gold} moedas de ouro')
                    if item == 'Peitoral de pano':
                        armaduras_compradas.append('Peitoral de pano')
                        del itens_disponiveis_npc_merchant[item]

                    elif item == 'Clava de madeira':
                        armas_compradas.append('Clava de madeira')
                        del itens_disponiveis_npc_merchant[item]

                    elif item == 'Espada de madeira':
                        armas_compradas.append('Espada de madeira')
                        del itens_disponiveis_npc_merchant[item]

                    elif item == 'Machado de madeira':
                        armas_compradas.append('Machado de madeira')
                        del itens_disponiveis_npc_merchant[item]

                    if primeira_visita and armaduras_compradas and armas_compradas:
                        primeira_visita = False

                else:
                    print('Você não tem ouro suficiente')
                    continue
            else:
                print('Nenhum item com esse indice!')
                print('\n')
                continue
        else:
            if primeira_visita and not armaduras_compradas:
                print('Você não pode sair sem comprar uma armadura.')
                continue
            elif primeira_visita and not armas_compradas:
                print('Você não pode sair sem comprar uma arma.')
                continue
            else:
                break


def backpack_itens():
    global armadura_equipada, arma_equipada, dano_arma, defesa_arma, strength, defense

    while True:
        print("\nEscolha o que deseja visualizar:")
        print("1. Ver armaduras")
        print("2. Ver armas")
        print("3. Ver poções")
        print("4. Sair")

        escolha = input("Digite o número da opção: ")

        if escolha == '1':
            # Mostrar armaduras
            print("\nArmaduras compradas:")
            if armadura_equipada:
                print(f"{armadura_equipada} (EQUIPADO)")
            for i, armadura in enumerate(armaduras_compradas, 1):
                print(f"{i}. {armadura}")

            # Perguntar se deseja equipar
            equipar_arma = input("\nDeseja equipar alguma arma? (Sim/Não): ").strip().upper()
            if equipar_arma in {'SIM', 'S'}:
                try:
                    idx_arma = int(input("\nDigite o número da arma para ver os atributos: "))
                    if 1 <= idx_arma <= len(armaduras_compradas):
                        armadura_nova = armaduras_compradas[idx_arma - 1]
                        atributos_nova = armas_atributos[armadura_nova]
                        print(f"{armadura_nova}, Defesa = {atributos_nova['defesa']}")

                        confirmar_equipar = input("Deseja equipar essa arma? (Sim/Não): ").strip().upper()
                        if confirmar_equipar in {'SIM', 'S'}:
                            if armadura_equipada:
                                # Remover atributos da arma atual
                                atributos_atual = armas_atributos[armadura_equipada]
                                defense -= atributos_atual['defesa']
                                print(f"Você removeu {armadura_equipada}.")

                            # Equipar nova arma
                            armadura_equipada = armadura_nova
                            defense += atributos_nova['defesa']
                            print(f"Você equipou {armadura_equipada}")

                        else:
                            print("Arma não equipada.")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
            else:
                print("Opção inválida, tente novamente.")

        elif escolha == '2':
            # Mostrar armas
            print("\nArmas compradas:")
            if arma_equipada:
                print(f"{arma_equipada} (EQUIPADO)")
            for i, arma in enumerate(armas_compradas, 1):
                print(f"{i}. {arma}")

            # Perguntar se deseja equipar
            equipar_arma = input("\nDeseja equipar alguma arma? (Sim/Não): ").strip().upper()
            if equipar_arma in {'SIM', 'S'}:
                try:
                    idx_arma = int(input("\nDigite o número da arma para ver os atributos: "))
                    if 1 <= idx_arma <= len(armas_compradas):
                        arma_nova = armas_compradas[idx_arma - 1]
                        atributos_nova = armas_atributos[arma_nova]
                        print(f"{arma_nova}, Dano = {atributos_nova['ataque']}, Defesa = {atributos_nova['defesa']}")

                        confirmar_equipar = input("Deseja equipar essa arma? (Sim/Não): ").strip().upper()
                        if confirmar_equipar in {'SIM', 'S'}:
                            if arma_equipada:
                                # Remover atributos da arma atual
                                atributos_atual = armas_atributos[arma_equipada]
                                strength -= atributos_atual['ataque']
                                defense -= atributos_atual['defesa']
                                print(f"Você removeu {arma_equipada}.")

                            # Equipar nova arma
                            arma_equipada = arma_nova
                            strength += atributos_nova['ataque']
                            defense += atributos_nova['defesa']
                            print(f"Você equipou {arma_equipada}")

                        else:
                            print("Arma não equipada.")
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Entrada inválida. Digite um número.")
            else:
                print("Opção inválida, tente novamente.")

        elif escolha == '3':
            # Mostrar poções
            print(f"\nPoções de vida: {hp_pot}")
            print(f"Poções de mana: {mp_pot}")

        elif escolha == '4':
            break

        else:
            print("Opção inválida, tente novamente.")


def hunt():
    monster_name = create_monster_name()
    monster_config = create_monster_level()
    monster_level = monster_config[0]
    hp_monster = monster_config[1]
    strength_monster = monster_config[2]
    defense_monster = monster_config[3]
    xp_monster = monster_config[4]
    time.sleep(2)
    print(f"Você encontrou um {monster_name}")
    time.sleep(1)
    print(f"Seu level: {player_level}, level do monstro: {monster_level}")
    time.sleep(1)
    print(f"Sua vida atual: {current_health}, vida do monstro: {hp_monster}")
    time.sleep(1)
    print(f"Sua força: {strength}, força do monstro: {strength_monster}")
    time.sleep(1)
    print(f"Sua defesa: {defense}, defesa do monstro: {defense_monster}")
    time.sleep(1)
    battle(monster_name, monster_level, hp_monster, strength_monster, defense_monster, xp_monster)


def battle(monster_name, monster_level, hp_monster, strength_monster, defense_monster, xp_monster):
    global current_health, current_mana, health_max, mana_max
    global xp, xp_next_level
    global hp_pot, mp_pot, gold, pedra_forja, pedra_ressureicao
    global defense, strength
    global player_level
    monster_visual = generate_random_monster()
    current_health_monster = hp_monster
    rodada_monstro = False
    while current_health_monster > 0 or current_health > 0:
        # Monstro HP
        percent_hp_monster = current_health_monster / hp_monster
        bar_length_monster = 20
        filled_length_monster = int(bar_length_monster * percent_hp_monster)
        health_bar_monster = '█' * filled_length_monster + '-' * (bar_length_monster - filled_length_monster)

        print(monster_visual)
        print(f'{monster_name} HP: [{health_bar_monster}] {current_health_monster:.2f}/{hp_monster:.2f}')

        time.sleep(1)
        # Player HP
        percent_hp_player = current_health / health_max
        bar_length_player = 20
        filled_length_player = int(bar_length_player * percent_hp_player)

        # Construir a barra de vida
        health_bar_player = '█' * filled_length_player + '-' * (bar_length_player - filled_length_player)

        # Player MP
        percent_mp_player = current_mana / mana_max
        bar_length_player_mp = 20
        filled_length_player_mp = int(bar_length_player_mp * percent_mp_player)

        # Construir a barra de vida
        mana_bar_player = '█' * filled_length_player_mp + '-' * (bar_length_player_mp - filled_length_player_mp)

        # Exibir a barra de vida com o valor numérico ao lado
        print('\n')
        print('Você: ‾\O/‾') # noqa : W605
        print(f'{player_name} HP: [{health_bar_player}] {current_health:.2f}/{health_max:.2f}')
        print(f'{player_name} MP: [{mana_bar_player}] {current_mana:.2f}/{mana_max:.2f}')
        time.sleep(1)
        print("\nEscolha sua ação:")
        print("[1] Atacar 🗡️")
        print("[2] Defender 🛡️")
        print("[3] Usar Poção 🧪")
        print("[4] Usar Magia 🔮")
        player_choice = input('').upper()
        if player_choice == '1':  # Atacar
            damage_dealt = round(float((random.randint(int(strength - 5), int(strength))) + (0.35 * strength)), 2)
            if round(damage_dealt - (0.15 * defense_monster), 2) <= 0.00:
                print('Você errou seu ataque.')
            else:
                current_health_monster -= round(damage_dealt - (0.15 * defense_monster), 2)
                print(f'Você atacou o monstro, causando {round(damage_dealt - (0.15 * defense_monster), 2)} de dano')
            rodada_monstro = True
            time.sleep(1)

        elif player_choice == '2':  # Defender
            defense_boost = random.randint(1, defense) + (0.25 * defense)
            print(f'Você se preparou para defender, aumentando sua defesa em {defense_boost}')
            defense += defense_boost
            rodada_monstro = True
            time.sleep(1)

        elif player_choice == '3':  # Usar Poção
            if hp_pot > 0 or mp_pot > 0:
                pergunta_pot = input(
                    "Qual poção você quer usar?\n"
                    "[1] Poção de Vida 🧪❤️ (Restantes: {})\n"
                    "[2] Poção de Mana 🧪💙 (Restantes: {})\n".format(hp_pot, mp_pot)
                )
                if pergunta_pot == '1':
                    if hp_pot > 0:
                        current_health += 25
                        hp_pot -= 1
                        print('Você usou uma Poção de Vida e restaurou 25 pontos de vida.')
                        rodada_monstro = True
                    else:
                        print('Você não tem mais Poções de Vida.')
                elif pergunta_pot == '2':
                    if mp_pot > 0:
                        current_mana += 25
                        mp_pot -= 1
                        print('Você usou uma Poção de Mana e restaurou 25 pontos de mana.')
                        rodada_monstro = True
                    else:
                        print('Você não tem mais Poções de Mana.')
                else:
                    print('Opção inválida.')
            else:
                print('Você não possui mais poções.')

        elif player_choice == '4':  # Magia
            print("Sem magias por enquanto...")

        else:
            print('Opção inválida')
            continue

        if current_health_monster <= 0.00:
            print(f'Você derrotou o {monster_name}!')
            xp += xp_monster
            print(f"Você ganhou {xp_monster} XP.")
            time.sleep(1)
            if xp >= xp_next_level:
                print("Parabéns! Você subiu de nível!")
                player_level += 1
                xp -= xp_next_level
                xp_next_level = int(xp_next_level * 1.5)
                new_strength, new_defense, new_health_max, new_mana_max = update_attributes(strength, defense, health_max, mana_max)
                print("Seus atributos aumentaram:")
                time.sleep(1.5)
                print(f"\nForça: {strength:.2f} -> {new_strength:.2f}")
                time.sleep(1.5)
                print(f"\nDefesa: {defense:.2f} -> {new_defense:.2f}")
                time.sleep(1.5)
                print(f"\nVida Máxima: {health_max:.2f} -> {new_health_max:.2f}")
                time.sleep(1.5)
                print(f"\nMana Máxima: {mana_max:.2f} -> {new_mana_max:.2f}")
                time.sleep(2)
                # Atualiza os atributos do jogador
                strength, defense, health_max, mana_max = new_strength, new_defense, new_health_max, new_mana_max

            loot = generate_loot(monster_level)
            if loot != {}:
                for item, amount in loot.items():
                    name = format_item_name(item)
                    print(f'Você encontrou {amount} {name}!')
                    if item == 'gold':
                        gold += amount
                    elif item == 'hp_potion':
                        hp_pot += amount
                    elif item == 'mp_potion':
                        mp_pot += amount
                    elif item == 'pedra_forja':
                        pedra_forja += amount
                    elif item == 'pedra_ressureicao':
                        pedra_ressureicao += amount
            else:
                print('O monstro não dropou nenhum item.')
            time.sleep(1)
            break

        else:
            if rodada_monstro is True:
                rodada_monstro = False
                damage_dealt = round(float((random.randint(int(strength_monster - 5), int(strength_monster))) + (0.35 * strength_monster)), 2)
                if round(damage_dealt - (0.15 * defense), 2) <= 0.00:
                    print('Você desviou do ataque do monstro!')
                else:
                    current_health -= round(damage_dealt - (0.15 * defense), 2)
                    print(f'O monstro atacou você, causando {round(damage_dealt - (0.15 * defense), 2)} de dano')
                time.sleep(1)

        if current_health <= 0:
            print("Você foi derrotado! Game Over.")
            break

    # Mensagem final após a batalha
    print('Batalha encerrada.')


def forge():
    global first_forge, pedra_forja, gold, chance_critico_arma
    print("Seja bem vindo a forja...")
    if first_forge is False:
        print(f'{npc_forger} Fala meu guerreiro, vai querer aprimorar o que hoje?')
    time.sleep(2)
    while True:
        if first_forge is True:
            print(f'{npc_julie} Na forja é possível melhorar suas armas e armaduras...')
            time.sleep(2)

            print(f'{npc_julie} Existem 2 tipos de melhoria na arma e armadura:')
            time.sleep(2)

            print(f'{npc_julie} 1° Tipo de melhoria na arma:')
            print(f'{npc_julie} Você adiciona uma possibilidade do seu dano no inimigo critar (x0,5 a mais do ano)')
            time.sleep(6.5)

            print(f'{npc_julie} 2° Tipo de melhoria na arma:')
            print(f'{npc_julie} Você aumenta o dano base, a defesa base e escalonamento do crítico')
            time.sleep(4.5)

            print(f'{npc_julie} 1° Tipo de melhoria na armadura:')
            print(f'{npc_julie} Você aumenta a possibilidade de defender um ataque')
            time.sleep(5.5)

            print(f'{npc_julie} 2° Tipo de melhoria na armadura:')
            print(f'{npc_julie} Você aumenta a possibilidade do seu dano refletir no inimigo (baseado no dano que ele te deu)')
            time.sleep(7)

            print(f'{npc_julie} Mas é claro que tudo tem seu preço e nem sempre voce pode ter sucesso ao melhorar sua arma hahahaha...')
            time.sleep(5)
            print(f'{npc_julie} Vamos começar?')
            time.sleep(2)
            if pedra_forja == 1:
                print(f'{npc_julie} Eu te darei os 50 de ouro, mas vejo que no primeiro monstro você dropou uma pedra de forja, vou poupar a minha então hahahaha')
                time.sleep(6)
            else:
                print(f'{npc_julie} Vou te emprestar a minha pedra de forja e te dar 50 de ouro')
                time.sleep(2)
                pedra_forja += 1
                print('Você ganhou 1 pedra de forja de Julie')
            time.sleep(3)
            gold += 50
            print('Você ganhou 50 moedas de ouro de Julie')
            time.sleep(2)

        if first_forge is True:
            escolha = input("[1] Aprimorar armas ⚔️ 🦯 🪓")
        else:
            escolha = input("[1] Aprimorar armas ⚔️ 🦯 🪓"
                            "[2] Aprimorar armadura 🛡️"
                            "[3] Sair 🚪")
        time.sleep(2)
        if escolha == '1':
            if first_forge is True:
                print(f'{npc_forger} Qual tipo de aprimoramento?')
                escolha_1 = input("[1] Aprimorar chance de crítico ➕💥 - (50 de gold e 1 pedra de forja)")
            else:
                print(f'{npc_forger} Qual tipo de aprimoramento?')
                escolha_1 = input("[1] Aprimorar chance de crítico ➕💥 - (50 de gold e 1 pedra de forja)"
                                  "[2] Aprimorar dano base, defesa base e escalonamento do crítico da arma ➕💪 (100 de gold e 2 pedra de forja)"
                                  "[3] Voltar 🚪")
            time.sleep(2)
            if escolha_1 == '1':
                if gold >= 50 and pedra_forja >= 1:
                    if first_forge is True:
                        print(f'{npc_forger} Você aumentou a chance de crítico em 10%!')
                        chance_critico_arma += 0.1  # 10% chance de crítico
                        time.sleep(2)
                        print('Você usou 50 moedas de ouro e 1 pedra de forja')
                        gold -= 50
                        pedra_forja -= 1
                        time.sleep(2)
                        first_forge = False
                    else:
                        # Logica para ser 75% de chance de sucesso
                        print(f'{npc_forger} Você aumentou a chance de crítico em 10%!')
                        chance_critico_arma += 0.1  # 10% chance de crítico
                        time.sleep(2)
                        print('Você usou 50 moedas de ouro e 1 pedra de forja')
                        gold -= 50
                        pedra_forja -= 1
                        time.sleep(2)
                else:
                    print(f'{npc_forger} Você não possui moedas de ouro ou pedras de forja suficiente')
                    time.sleep(2)
                    continue
            elif escolha_1 == '2' and first_forge is False:
                if gold >= 100 and pedra_forja >= 2:
                    print(f'{npc_forger} Você aumentou o dano base, defesa base e escalonamento do crítico em 10%!')
                    # damage_base += 0.1  # 10% aumento de dano base
                    # defense_base += 0.1  # 10% aumento de defesa base
                    # escalonamento_critico += 0.1  # 10% aumento de escalonamento do crítico
                    # time.sleep(2)
                    # print('Você usou 100 moedas de ouro e 2 pedras de forja')
                    # gold -= 100
                    # pedra_forja -= 2
                    # time.sleep(2)
                else:
                    print(f'{npc_forger} Você não possui moedas de ouro ou pedras de forja suficiente')
                    time.sleep(2)
                    continue
            elif escolha_1 == '3' and first_forge is False:
                continue
            else:
                print('Opção inválida')
        elif escolha == '2' and first_forge is False:
            ...
            # Logica a ser implementada
        elif escolha == '3' and first_forge is False:
            print(f'{npc_forger} Até mais {player_name}, volte sempre!')
            break
        else:
            print('Opção inválida')


def storygame():
    print(f'{npc_julie} Antes de começar, te darei 10 moedas de ouro'
          '\npara que você compre uma armadura e uma arma')
    time.sleep(3)
    global gold
    gold += 10
    print(f'Você tem {gold} moedas de ouro')
    print('Voce entrou na loja de equipamentos...')
    time.sleep(2)
    print(f'{npc_merchant} Fala meu guerreiro, tudo bem? o que deseja pra hoje?')
    buy_itens()
    print('Você saiu da loja de equipamentos...')
    time.sleep(2)
    print(f'{npc_julie} Agora vamos equipar seus itens, {player_name}')
    backpack_itens()
    time.sleep(2)
    print(f'{npc_julie} Agora você pode ir se aventurar na floresta')
    hunt()
    time.sleep(2)
    print(f'{npc_julie} Ora ora... vejo que você se saiu muito bem!')
    time.sleep(2)
    print(f'{npc_julie} Agora iremos visitar a forja')
    forge()


def gameplay():
    print('Alguem se aproxima de você...')
    time.sleep(3)
    print(f"{npc_julie} Olá! Seja bem vindo {player_name} a {village_name}")
    time.sleep(5)
    print(f"{npc_julie} Sou a treinadora da vila")
    time.sleep(5)
    tutorial = tutorial_choice()
    if tutorial is True:
        tutorial_gameplay()
    elif tutorial is False:
        storygame()


def main():
    print('\n')
    print("Seja bem vindo ao jogo de RPG")
    time.sleep(2)
    print('Você é um novo integrante da vila')
    time.sleep(3)
    print('Você precisa escolher um nome para seu personagem:')
    global player_name
    player_name = player_name_choice()
    time.sleep(2)
    print(f'Seja muito bem vindo a vila, {player_name}')
    time.sleep(4)
    print('Vamos começar a aventura!')
    time.sleep(2)
    gameplay()


if __name__ == '__main__':
    main()


# ascii_art = """
#          ,     .
#         /(     )\               A
#    .--.( `.___.' ).--.     ^   /_\   ^
#    `._ `%_&%#%$_ ' _.'    /|  <___>  |\
#       `|(@\\*%%/@)|'     / (__ |L| __) \
#        |  |%%#|  |      J d8bo |=|od8b  L
#         \\ \$#%/ /      | 8888 |=|8888  |
#         |\\|%%#|/|      J Y8P"_|=|_"Y8P F
#         | (.".)%|        \\ (  |L|  ) //
#     ___.'  `-'  `.___     \\|  |L|  |//
#   .'#*#`-       -'$#*`.       /(_)
#  /#%^#%*_ *%^%_  #  %$%\\    .(__)
#  #&  . %%%#% ###%*.   *%\\.-'&(__)
#  %*  J %.%#_|_#$.\\J* \\ %'#%*(__)
#  *#% J %$%%#|#$#$ J\\%   *   .-(_)
#  |%  J\\ `%%#|#%%' / `.   _.'  |L|
#  |#$%||` %%%$### '|   `-'      |L|
#  (#%%||` #$#$%%% '|            |L|
#  | ##||  $%%.%$%  |            |L|
#  |$%^||   $%#$%   |  VK/cf     |L|
#  |&^ ||  #%#$%#%  |            |L|
#  |#$*|| #$%$$#%%$ |\\          |L|
#  ||||||  %%(@)$#  |\\\\        |L|
#  `|||||  #$$|%#%  | L|         |L|
#       |  #$%|$%%  | ||l        |L|
#       |  ##$H$%%  | |\\\\      |L|
#       |  #%%H%##  | |\\\\|     |L|
#       |  ##% $%#  | Y|||       |L|
#       J $$#* *%#% L  |E/       \=/
#       J#%$ | |%%#%L  F/         V
#       |$$%#& & %%#|
#       J##$ J % %%$F
#        %$# * * %#&
#        %#$ | |%#$%
#        *#$%| | #$*
#       /$#' ) ( `%%\\
#      /#$# /   \\ %$%\\
#     ooooO'     `Ooooo
# """

# print(ascii_art)
