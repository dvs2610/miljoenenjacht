from flask import Flask, redirect, render_template, url_for, request
from pathlib import Path
from random import shuffle
import statistics
import secrets

app = Flask(__name__)
SECRET_KEY_FILE = Path(__file__).with_name("secret_key.txt")
if not SECRET_KEY_FILE.exists():
	SECRET_KEY_FILE.write_text(secrets.token_hex(32), encoding="utf-8")
app.config["SECRET_KEY"] = SECRET_KEY_FILE.read_text(encoding="utf-8").strip()


@app.template_filter("format_number")
def format_number(value):
    return f"{value:,}".replace(",", ".")


AMOUNTS = [1, 5, 10, 20, 50, 100, 500, 1000, 2500, 5000, 10000, 25000, 50000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]


class Game:
    def __init__(self):
        self.player_case = None
        self.num_opened = 0
        self.cases = []
        self.offers = []
        self.offer = None
        self.offer_round = None
        self.finished = False
        self.result = None
        self.result_type = None

class Case:
    def __init__(self):
        self.number = None
        self.amount = None
        self.opened = False
        self.is_player_case = False


def create_new_game():
    amounts = AMOUNTS.copy()
    shuffle(amounts)

    game = Game()

    for num in range(20):
         case=Case()
         case.number = num+1
         case.amount = amounts[num]
         game.cases.append(case)

    return game


def calculate_offer(game: Game):
    if game.num_opened not in [5, 9, 12, 14, 15, 16, 17, 18]:
        return None

    amounts_in_game = []
    for case in game.cases:
        if not case.opened:
            amounts_in_game.append(case.amount)
    average = statistics.mean(amounts_in_game)

    if game.num_opened == 5:
        return int(average * 0.35)
    elif game.num_opened == 9:
        return int(average * 0.45)
    elif game.num_opened == 12:
        return int(average * 0.6)
    elif game.num_opened == 14:
        return int(average * 0.7)
    elif game.num_opened == 15:
        return int(average * 0.8)
    elif game.num_opened == 16:
            return int(average * 0.9)
    elif game.num_opened == 17:
            return int(average)
    elif game.num_opened == 18:
            return int(average)
    return int(average)


game=create_new_game()


@app.route('/', methods=['GET', 'POST'])
def index():
    global game

    if request.method == 'POST':
        if request.form.get('action') == 'new_game':
            game = create_new_game()
        elif not game.finished:
            action = request.form.get('action')
            if action == 'accept_offer' and game.offer is not None:
                game.finished = True
                game.result = game.offer
                game.result_type = 'offer'
                game.offer = None
            elif action == 'decline_offer' and game.offer is not None:
                game.offers.append({
                    'round': game.num_opened,
                    'amount': game.offer,
                })
                game.offer = None
                game.offer_round = game.num_opened
            elif action is None and game.offer is None:
                case_num = request.form.get('case_number', type=int)
                if case_num is not None:
                    for case in game.cases:
                        if case.number == case_num:
                            if game.player_case is None:
                                game.player_case = case
                                case.is_player_case = True
                            elif not case.is_player_case and not case.opened:
                                case.opened = True
                                game.num_opened += 1
                                if game.num_opened == 19 and game.player_case is not None:
                                    game.player_case.opened = True
                                    game.num_opened += 1
                                    game.finished = True
                                    game.result = game.player_case.amount
                                    game.result_type = 'case'
                            break
        return redirect(url_for('index'))
    
    if not game.finished and game.offer is None and game.offer_round != game.num_opened:
        game.offer = calculate_offer(game)
    return render_template('index.html', game=game, offer=game.offer, amounts=AMOUNTS)


if __name__ == '__main__':
	app.run()
