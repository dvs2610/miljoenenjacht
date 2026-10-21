# TEST_CASES = [
#     {"number": 1, "picked": False, "opened": False, "amount": 0.01},
#     {"number": 2, "picked": False, "opened": False, "amount": 0.20},
#     {"number": 3, "picked": False, "opened": False, "amount": 0.50},
#     {"number": 4, "picked": False, "opened": False, "amount": 1},
#     {"number": 5, "picked": False, "opened": False, "amount": 5},
#     {"number": 6, "picked": False, "opened": False, "amount": 10},
#     {"number": 7, "picked": False, "opened": False, "amount": 20},
#     {"number": 8, "picked": False, "opened": False, "amount": 50},
#     {"number": 9, "picked": False, "opened": False, "amount": 100},
#     {"number": 10, "picked": False, "opened": False, "amount": 500},
#     {"number": 11, "picked": False, "opened": False, "amount": 1000},
#     {"number": 12, "picked": True, "opened": False, "amount": 2500},
#     {"number": 13, "picked": False, "opened": False, "amount": 5000},
#     {"number": 14, "picked": False, "opened": False, "amount": 10000},
#     {"number": 15, "picked": False, "opened": False, "amount": 25000},
#     {"number": 16, "picked": False, "opened": False, "amount": 50000},
#     {"number": 17, "picked": False, "opened": False, "amount": 100000},
#     {"number": 18, "picked": False, "opened": False, "amount": 200000},
#     {"number": 19, "picked": False, "opened": False, "amount": 300000},
#     {"number": 20, "picked": False, "opened": False, "amount": 400000},
#     {"number": 21, "picked": False, "opened": False, "amount": 500000},
#     {"number": 22, "picked": False, "opened": False, "amount": 750000},
#     {"number": 23, "picked": False, "opened": False, "amount": 1000000},
#     {"number": 24, "picked": False, "opened": False, "amount": 2000000},
#     {"number": 25, "picked": False, "opened": False, "amount": 2500000},
#     {"number": 26, "picked": False, "opened": False, "amount": 5000000},
# ]

# AMOUNTS = [0.01, 0.20, 0.50, 1, 5, 10, 20, 50, 100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000, 2000000, 2500000, 5000000]

TEST_CASES = [
    {"number": 1, "picked": False, "opened": False, "amount": 1},
    {"number": 2, "picked": False, "opened": False, "amount": 5},
    {"number": 3, "picked": False, "opened": False, "amount": 10},
    {"number": 4, "picked": False, "opened": False, "amount": 20},
    {"number": 5, "picked": False, "opened": False, "amount": 50},
    {"number": 6, "picked": False, "opened": False, "amount": 100},
    {"number": 7, "picked": False, "opened": False, "amount": 500},
    {"number": 8, "picked": False, "opened": False, "amount": 1000},
    {"number": 9, "picked": True, "opened": False, "amount": 2500},
    {"number": 10, "picked": False, "opened": False, "amount": 5000},
    {"number": 11, "picked": False, "opened": False, "amount": 10000},
    {"number": 12, "picked": False, "opened": False, "amount": 25000},
    {"number": 13, "picked": False, "opened": False, "amount": 50000},
    {"number": 14, "picked": False, "opened": False, "amount": 100000},
    {"number": 15, "picked": False, "opened": False, "amount": 200000},
    {"number": 16, "picked": False, "opened": False, "amount": 300000},
    {"number": 17, "picked": False, "opened": False, "amount": 400000},
    {"number": 18, "picked": False, "opened": False, "amount": 500000},
    {"number": 19, "picked": False, "opened": False, "amount": 750000},
    {"number": 20, "picked": False, "opened": False, "amount": 1000000},
]

# def create_game():
#     cases = TEST_CASES.copy()
#     amounts = AMOUNTS.copy()
#     for case in cases:
#         case['opened'] = False
#         case['picked'] = False
#     # For testing hardcoded picked case
#     cases[9]['picked'] = True
#     shuffle(amounts)
#     for case, amount in zip(cases, amounts):
#         case["amount"] = amount
#     return cases

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         if request.form.get('action') == 'new_game':
#             create_game()
#         else:
#             case_number = request.form.get('case_number', type=int)
#             case = next((case for case in TEST_CASES if case['number'] == case_number), None)
#             if case is not None and not case['picked'] and not case['opened']:
#                 case['opened'] = True
#             # offer = calculate_offer()
#         return redirect(url_for('index'))
#     return render_template('index.html', cases=cases, offer=calculate_offer(), amounts=AMOUNTS)

# CASE = {
#     "number": None,
#     "amount": None,
#     "opened": False,
#     "is_player_case": False
# }