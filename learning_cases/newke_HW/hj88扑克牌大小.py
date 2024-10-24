# HJ88 扑克牌大小
#
# 描述
# 扑克牌游戏大家应该都比较熟悉了，一副牌由54张组成，含3~A、2各4张，小王1张，大王1张。牌面从小到大用如下字符和字符串表示（其中，小写joker表示小王，大写JOKER表示大王）：
# 3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
# 输入两手牌，两手牌之间用"-"连接，每手牌的每张牌以空格分隔，"-"两边没有空格，如：4 4 4 4 - joker JOKER。
# 请比较两手牌大小，输出较大的牌，如果不存在比较关系则输出ERROR。
# 基本规则：
# （1）输入每手牌可能是个子、对子、顺子（连续5张）、三个、炸弹（四个）和对王中的一种，不存在其他情况，由输入保证两手牌都是合法的，顺子已经从小到大排列；
# （2）除了炸弹和对王可以和所有牌比较之外，其他类型的牌只能跟相同类型的存在比较关系（如，对子跟对子比较，三个跟三个比较），不考虑拆牌情况（如：将对子拆分成个子）；
# （3）大小规则跟大家平时了解的常见规则相同，个子、对子、三个比较牌面大小；顺子比较最小牌大小；炸弹大于前面所有的牌，炸弹之间比较牌面大小；对王是最大的牌；
# （4）输入的两手牌不会出现相等的情况。
#
# 输入描述：
# 输入两手牌，两手牌之间用"-"连接，每手牌的每张牌以空格分隔，"-"两边没有空格，如4 4 4 4 - joker JOKER。
#
# 输出描述：
# 输出两手牌中较大的那手，不含连接符，扑克牌顺序不变，仍以空格隔开；如果不存在比较关系则输出ERROR。
#
# 示例1
# 输入：4 4 4 4 - joker JOKER
#
# 输出：joker JOKER

def compare_cards(card1, card2):
    cards_order = '3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER'.split()
    card1_type = get_card_type(card1)
    card2_type = get_card_type(card2)

    if card1_type == card2_type:
        if card1_type == 'single':
            return card1 if cards_order.index(card1[0]) > cards_order.index(card2[0]) else card2
        elif card1_type == 'pair':
            card1_value = cards_order.index(card1[0])
            card2_value = cards_order.index(card2[0])
            return card1 if card1_value > card2_value else card2
        elif card1_type == 'three':
            card1_value = cards_order.index(card1[0])
            card2_value = cards_order.index(card2[0])
            return card1 if card1_value > card2_value else card2
        elif card1_type == 'straight':
            return card1 if cards_order.index(card1[0]) > cards_order.index(card2[0]) else card2
        elif card1_type == 'bomb':
            card1_value = cards_order.index(card1[0])
            card2_value = cards_order.index(card2[0])
            return card1 if card1_value > card2_value else card2
    elif card1_type == 'bomb' or card2_type == 'bomb':
        return card1 if card1_type == 'bomb' else card2
    elif card1 == 'joker JOKER' or card2 == 'joker JOKER':
        return 'joker JOKER'
    else:
        return 'ERROR'

def get_card_type(cards):
    if len(cards.split()) == 1:
        return 'single'
    elif len(cards.split()) == 2 and cards.split()[0] == cards.split()[1]:
        return 'pair'
    elif len(cards.split()) == 3 and cards.split()[0] == cards.split()[1] == cards.split()[2]:
        return 'three'
    elif len(cards.split()) == 5 and is_straight(cards.split()):
        return 'straight'
    elif len(cards.split()) == 4:
        return 'bomb'
    elif cards == 'joker JOKER':
        return 'joker_joker'
    else:
        return None

def is_straight(cards):
    cards_order = '3 4 5 6 7 8 9 10 J Q K A 2'.split()
    values = [cards_order.index(card) for card in cards]
    sorted_values = sorted(values)
    return sorted_values == list(range(sorted_values[0], sorted_values[0] + 5))

input_cards = input()
card1, card2 = input_cards.split('-')
result = compare_cards(card1, card2)
print(result)

