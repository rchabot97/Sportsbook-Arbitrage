import tkinter as tk


class A:

    def __init__(self, master):

        master.title("Sportsbook GUI")

        self.bet_amount = int(input('Top bet amount: '))
        self.low_amount = int(input('Low bet amount: '))
        self.percent_threshold = round(float(input('Threshold (%): ')),2)

        self.master = master
        self.master.configure(bg='grey')

        self.odds1 = 0
        self.odds2 = 0

        self.label1 = tk.Label(self.master)
        self.label1.grid(row=1, column=1, padx=4, pady=4, columnspan=2)
        self.label1.configure(text='Team 1 odds:', bg='grey')

        self.label2 = tk.Label(self.master)
        self.label2.grid(row=1, column=3, padx=4, pady=4, columnspan=2)
        self.label2.configure(text='Team 2 odds:', bg='grey')

        self.odds_input1 = tk.Entry(self.master)
        self.odds_input1.grid(row=2, column=1, padx=4, pady=4, columnspan=2)

        self.odds_input2 = tk.Entry(self.master)
        self.odds_input2.grid(row=2, column=3, padx=4, pady=4, columnspan=2)

        self.thresh = tk.Label(self.master)
        self.thresh.grid(row=2, column=5, padx=4, pady=4)
        self.thresh.configure(text='thresh: {}%'.format(self.percent_threshold), bg='grey')

        self.output_label = tk.Label(self.master)
        self.output_label.grid(row=0, column=1, padx=4, pady=4, columnspan=4)
        self.output_label.configure(text='-', bg='grey')

        self.barrier_label = tk.Label(self.master)
        self.barrier_label.grid(row=3, column=0, padx=4, pady=4, columnspan=6)
        self.barrier_label.configure(text='================================================================', bg='grey')

        self.barrier_label2 = tk.Label(self.master)
        self.barrier_label2.grid(row=11, column=0, padx=4, pady=4, columnspan=6)
        self.barrier_label2.configure(text='================================================================', bg='grey')

        self.label3 = tk.Label(self.master)
        self.label3.grid(row=12, column=1, padx=4, pady=4, columnspan=2)
        self.label3.configure(text='Threshold %:', bg='grey')

        self.thresh_input = tk.Entry(self.master)
        self.thresh_input.grid(row=13, column=1, padx=4, pady=4, columnspan=2)

        self.label4 = tk.Label(self.master)
        self.label4.grid(row=12, column=3, padx=4, pady=4, columnspan=2)
        self.label4.configure(text='Top Bet ($):', bg='grey')

        self.top_input = tk.Entry(self.master)
        self.top_input.grid(row=13, column=3, padx=4, pady=4, columnspan=2)

        self.button = tk.Button(self.master)
        self.button.configure(text='Update', command=self.update_button)
        self.button.grid(row=13, column=5, padx=4, pady=4, columnspan=1, rowspan=2)

        self.label5 = tk.Label(self.master)
        self.label5.grid(row=14, column=3, padx=4, pady=4, columnspan=2)
        self.label5.configure(text='Low Bet ($):', bg='grey')

        self.low_input = tk.Entry(self.master)
        self.low_input.grid(row=15, column=3, padx=4, pady=4, columnspan=2)

        for i in range(5):
            self.top_label = tk.Label(self.master, width=10, fg='black', bg='grey', text="Label {}".format(i + 1))
            self.top_label.grid(row=4, column=i + 1, padx=4, pady=4)

        for i in range(5):
            self.side_label = tk.Label(self.master, width=5, fg='black', bg='grey', text="Label {}".format(i + 1))
            self.side_label.grid(row=i+5, column=0, padx=4, pady=4)

        for i in range(5):
            i+=5
            for j in range(5):

                if i == 7 and j == 2:
                    self.e = tk.Label(self.master, highlightthickness=4, highlightbackground='black', highlightcolor='red', width=10, fg='black', bg='white', text="$1000\n$2000")
                    self.e.grid(row=i, column=j + 1, padx=4, pady=4)

                else:
                    self.e = tk.Label(self.master, width=10, fg='black', bg='white', text="$1000\n$2000")
                    self.e.grid(row=i, column= j + 1, padx=4, pady=4)

        master.bind('<Return>', self.button_action)

    def update_button(self):

        new_thresh1 = self.thresh_input.get()
        if new_thresh1 != "":
            new_thresh = round(float(new_thresh1), 2)
            self.percent_threshold = new_thresh

        new_top1 = self.top_input.get()
        if new_top1 != "":
            new_top = int(new_top1)
            self.bet_amount = new_top

        new_low1 = self.low_input.get()
        if new_low1 != "":
            new_low = int(new_low1)
            self.low_amount = new_low

    def grid_udpate(self):

        self.thresh.configure(text='thresh: {}%'.format(self.percent_threshold), bg='grey')

        if abs(self.odds1) > 160 and abs(self.odds2) > 160:

            for i in range(5):
                odds1 = self.odds1 - 20 + (i * 10)
                if odds1 < 100 and self.odds1 > 99:
                    odds1 -= 200
                elif odds1 > -100 and self.odds1 < -99:
                    odds1 += 200

                if odds1 > 100:
                    self.top_label = tk.Label(self.master, width=10, fg='black', bg='grey', text="+{}".format(odds1))
                    self.top_label.grid(row=4, column=i + 1, padx=4, pady=4)
                else:
                    self.top_label = tk.Label(self.master, width=10, fg='black', bg='grey', text="{}".format(odds1))
                    self.top_label.grid(row=4, column=i + 1, padx=4, pady=4)

            for i in range(5):
                odds2 = self.odds2 - 20 + (i * 10)
                if odds2 < 100 and self.odds2 > 99:
                    odds2 -= 200
                elif odds2 > -100 and self.odds2 < -99:
                    odds2 += 200

                if odds2 > 100:
                    self.side_label = tk.Label(self.master, width=5, fg='black', bg='grey', text="+{}".format(odds2))
                    self.side_label.grid(row=i + 5, column=0, padx=4, pady=4)
                else:
                    self.side_label = tk.Label(self.master, width=5, fg='black', bg='grey', text="{}".format(odds2))
                    self.side_label.grid(row=i + 5, column=0, padx=4, pady=4)

            for i in range(5):

                odds2 = self.odds2 - 20 + (i * 10)
                if odds2 < 100 and self.odds2 > 99:
                    odds2 -= 200
                elif odds2 > -100 and self.odds2 < -99:
                    odds2 += 200
                x = i + 5

                for j in range(5):

                    odds1 = self.odds1 - 20 + (j * 10)
                    if odds1 < 100 and self.odds1 > 99:
                        odds1 -= 200
                    elif odds1 > -100 and self.odds1 < -99:
                        odds1 += 200

                    amount1, amount2, percent1, percent2 = self.arbitrage(self.bet_amount, self.low_amount, odds1, odds2)
                    combo_percent = (percent1 + percent2) / 2
                    print("odds1:", odds1, "odds2:", odds2, "amount1:", amount1, "amount2:", amount2, "row:", x, "column:", j+1)

                    if amount1 == -1 or percent1 < 0 or percent2 < 0:
                        self.e = tk.Label(self.master, height = 2, width=10, fg='black', bg='red',
                                          text="X".format(amount1, amount2))
                        self.e.grid(row=x, column=j + 1, padx=4, pady=4)

                    elif x == 7 and j == 2 and combo_percent > self.percent_threshold:
                        self.e = tk.Label(self.master, highlightthickness=4, highlightbackground='black', highlightcolor='red', width=10, fg='black', bg='green', text="${}\n${}".format(amount1, amount2))
                        self.e.grid(row=x, column=j + 1, padx=4, pady=4)

                    elif x == 7 and j == 2 and combo_percent <= self.percent_threshold:
                        self.e = tk.Label(self.master, highlightthickness=4, highlightbackground='black', highlightcolor='red', width=10, fg='black', bg='yellow', text="${}\n${}".format(amount1, amount2))
                        self.e.grid(row=x, column=j + 1, padx=4, pady=4)

                    elif combo_percent > self.percent_threshold:
                        self.e = tk.Label(self.master, width=10, fg='black', bg='green',text="${}\n${}".format(amount1, amount2))
                        self.e.grid(row=x, column=j + 1, padx=4, pady=4)

                    else:
                        self.e = tk.Label(self.master, width=10, fg='black', bg='yellow', text="${}\n${}".format(amount1, amount2))
                        self.e.grid(row=x, column= j + 1, padx=4, pady=4)

        else:

            for i in range(5):
                odds1 = self.odds1 - 10 + (i * 5)
                if odds1 < 100 and self.odds1 > 99:
                    odds1 -= 200
                elif odds1 > -100 and self.odds1 < -99:
                    odds1 += 200

                if odds1 > 100:
                    self.top_label = tk.Label(self.master, width=10, fg='black', bg='grey', text="+{}".format(odds1))
                    self.top_label.grid(row=4, column=i + 1, padx=4, pady=4)
                else:
                    self.top_label = tk.Label(self.master, width=10, fg='black', bg='grey', text="{}".format(odds1))
                    self.top_label.grid(row=4, column=i + 1, padx=4, pady=4)

            for i in range(5):
                odds2 = self.odds2 - 10 + (i * 5)
                if odds2 < 100 and self.odds2 > 99:
                    odds2 -= 200
                elif odds2 > -100 and self.odds2 < -99:
                    odds2 += 200

                if odds2 > 100:
                    self.side_label = tk.Label(self.master, width=5, fg='black', bg='grey', text="+{}".format(odds2))
                    self.side_label.grid(row=i + 5, column=0, padx=4, pady=4)
                else:
                    self.side_label = tk.Label(self.master, width=5, fg='black', bg='grey', text="{}".format(odds2))
                    self.side_label.grid(row=i + 5, column=0, padx=4, pady=4)

            for i in range(5):

                odds2 = self.odds2 - 10 + (i * 5)
                if odds2 < 100 and self.odds2 > 99:
                    odds2 -= 200
                elif odds2 > -100 and self.odds2 < -99:
                    odds2 += 200
                x = i + 5

                for j in range(5):

                    odds1 = self.odds1 - 10 + (j * 5)
                    if odds1 < 100 and self.odds1 > 99:
                        odds1 -= 200
                    elif odds1 > -100 and self.odds1 < -99:
                        odds1 += 200

                    amount1, amount2, percent1, percent2 = self.arbitrage(self.bet_amount, self.low_amount, odds1, odds2)
                    combo_percent = (percent1 + percent2) / 2
                    print("odds1:", odds1, "odds2:", odds2, "amount1:", amount1, "amount2:", amount2, "row:", x,
                          "column:", j + 1)

                    if amount1 == -1 or percent1 < 0 or percent2 < 0:
                        self.e = tk.Label(self.master, height=2, width=10, fg='black', bg='red',
                                          text="X".format(amount1, amount2))
                        self.e.grid(row=x, column=j + 1, padx=4, pady=4)

                    elif x == 7 and j == 2 and combo_percent > self.percent_threshold:
                        self.e = tk.Label(self.master, highlightthickness=4, highlightbackground='black',
                                          highlightcolor='red', width=10, fg='black', bg='green',
                                          text="${}\n${}".format(amount1, amount2))
                        self.e.grid(row=x, column=j + 1, padx=4, pady=4)

                    elif x == 7 and j == 2 and combo_percent <= self.percent_threshold:
                        self.e = tk.Label(self.master, highlightthickness=4, highlightbackground='black',
                                          highlightcolor='red', width=10, fg='black', bg='yellow',
                                          text="${}\n${}".format(amount1, amount2))
                        self.e.grid(row=x, column=j + 1, padx=4, pady=4)

                    elif combo_percent > self.percent_threshold:
                        self.e = tk.Label(self.master, width=10, fg='black', bg='green',
                                          text="${}\n${}".format(amount1, amount2))
                        self.e.grid(row=x, column=j + 1, padx=4, pady=4)

                    else:
                        self.e = tk.Label(self.master, width=10, fg='black', bg='yellow',
                                          text="${}\n${}".format(amount1, amount2))
                        self.e.grid(row=x, column=j + 1, padx=4, pady=4)

    def button_action(self, event):

        if not self.odds_input1.get() == "" and not self.odds_input2.get == "":

            self.odds1 = int(self.odds_input1.get())
            self.odds2 = int(self.odds_input2.get())

            bet_amount1, bet_amount2, percentage1, percentage2 = self.arbitrage(self.bet_amount, self.low_amount, self.odds1, self.odds2)

            print("BA1:", bet_amount1, "BA2:", bet_amount2)

            self.output_label.configure(text='{}% return:  Bet ${} on Team 1 and ${} on Team 2'.format(round((percentage1 + percentage2) / 2, 2), bet_amount1, bet_amount2))
            self.grid_udpate()

    def myround(self, x, base=50):
        return int(base * round(float(x)/base))

    def convert_odds(self, odds):

        if odds > 0:
            odds_percentage = 100 / (100 + odds)

        elif odds < 0:
            odds_percentage = odds / (odds - 100)

        else:
            odds_percentage = 0

        return odds_percentage

    def arbitrage2(self, risk, odds_1, odds_2, rounding=50):
        odds_1_percentage = self.convert_odds(odds_1)
        odds_2_percentage = self.convert_odds(odds_2)

        print(odds_1_percentage)
        print(odds_2_percentage)

        if odds_1_percentage + odds_2_percentage < 1:

            print('odds_1 + odds_2: ', odds_1_percentage + odds_2_percentage)

            amount_1 = self.myround(odds_1_percentage * risk / (odds_1_percentage + odds_2_percentage), rounding)
            amount_2 = self.myround(risk - amount_1, rounding)

            print('Bet {} on team 1, {} on team 2'.format(amount_1, amount_2))
            print('Expected payout if team 1 wins:', amount_1 / odds_1_percentage)
            print('Expected payout if team 2 wins:', amount_2 / odds_2_percentage)
            # print('Expected profit: ', amount_1/odds_1_percentage - risk)
            print('Percentage return if team 1 wins: {}%'.format(100 * (amount_1 / odds_1_percentage - risk) / risk))
            print('Percentage return if team 2 wins: {}%'.format(100 * (amount_2 / odds_2_percentage - risk) / risk))

            print("amount 1:", amount_1, "amount 2:", amount_2)

            return(amount_1, amount_2, 100 * (amount_1 / odds_1_percentage - (amount_1 + amount_2)) / (amount_1 + amount_2), 100 * (amount_2 / odds_2_percentage - (amount_1 + amount_2)) / (amount_1 + amount_2))

        else:
            print('no arbitrage')
            return(-1, -1, -1, -1)


    def arbitrage(self, top_bet, low_bet, odds_1, odds_2, rounding=50):
        odds_1_percentage = self.convert_odds(odds_1)
        odds_2_percentage = self.convert_odds(odds_2)

        print(odds_1_percentage)
        print(odds_2_percentage)

        if odds_1_percentage + odds_2_percentage < 1:

            if max(odds_1_percentage, odds_2_percentage) * low_bet > min(odds_1_percentage, odds_2_percentage) * top_bet:

                if odds_1 < odds_2:
                    amount_1 = top_bet
                    amount_2 = top_bet * odds_2_percentage / odds_1_percentage

                else:
                    amount_2 = top_bet
                    amount_1 = top_bet * odds_1_percentage / odds_2_percentage

                return(self.myround(amount_1, 50), self.myround(amount_2, 50), 100 * (amount_1 / odds_1_percentage - (amount_1 + amount_2)) / (amount_1 + amount_2), 100 * (amount_2 / odds_2_percentage - (amount_1 + amount_2)) / (amount_1 + amount_2))

            else:

                if odds_1 < odds_2:
                    amount_1 = low_bet * odds_1_percentage / odds_2_percentage
                    amount_2 = low_bet

                else:
                    amount_2 = low_bet * odds_2_percentage / odds_1_percentage
                    amount_1 = low_bet

                return (self.myround(amount_1, 50), self.myround(amount_2, 50),
                        100 * (amount_1 / odds_1_percentage - (amount_1 + amount_2)) / (amount_1 + amount_2),
                        100 * (amount_2 / odds_2_percentage - (amount_1 + amount_2)) / (amount_1 + amount_2))

        else:
            print('no arbitrage')
            return(-1, -1, -1, -1)

root = tk.Tk()
print('initializing A')
A(root)
root.mainloop()

# print(myround(103225))
