import ui
from PySide2 import QtWidgets
import sys
from field import Board
from field import visited
from PySide2 import QtCore
from PySide2.QtGui import *
from test import run_test
mode = "EASY"

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.board = Board()
        self.win = ui.Ui_MainWindow()
        self.win.setupUi(self)
        self.update_scores()
        self.show()
        self.win.bt1.clicked.connect(lambda: self.field_clicked(1))
        self.win.bt2.clicked.connect(lambda: self.field_clicked(2))
        self.win.bt3.clicked.connect(lambda: self.field_clicked(3))
        self.win.bt4.clicked.connect(lambda: self.field_clicked(4))
        self.win.bt5.clicked.connect(lambda: self.field_clicked(5))
        self.win.bt6.clicked.connect(lambda: self.field_clicked(6))
        self.win.next.clicked.connect(lambda: self.play_opp_move())

    def field_clicked(self, number):
        if self.board.turn:
            last = self.board.fields[number].move_stones(self.board.turn)
            self.board.check_if_last_beats(last)
            self.board.decide_turn_after_move(last)
            self.update_scores()
            end = self.board.check_if_end()
            if end:
                self.update_scores()

    def play_opp_move(self):
        if mode == "EASY":
            self.board.next_move_with_minimax(3, True)
        if mode == "MED":
            self.board.next_move_with_minimax(5, True)
        else:
            self.board.next_move_with_minimax(7, True)
        self.update_scores()
        end = self.board.check_if_end()
        if end:
            self.update_scores()

    def update_scores(self):
        print(self.board.possible_moves())
        if self.board.turn:
            self.win.turn.setText("YOU")
            self.win.next.setEnabled(False)
        else:
            self.win.turn.setText("OPP")
            self.win.next.setEnabled(True)
        self.win.sc1.setText(self.board.fields[1].return_score())
        self.win.sc2.setText(self.board.fields[2].return_score())
        self.win.sc3.setText(self.board.fields[3].return_score())
        self.win.sc4.setText(self.board.fields[4].return_score())
        self.win.sc5.setText(self.board.fields[5].return_score())
        self.win.sc6.setText(self.board.fields[6].return_score())
        self.win.sc7.setText(self.board.fields[8].return_score())
        self.win.sc8.setText(self.board.fields[9].return_score())
        self.win.sc9.setText(self.board.fields[10].return_score())
        self.win.sc10.setText(self.board.fields[11].return_score())
        self.win.sc11.setText(self.board.fields[12].return_score())
        self.win.sc12.setText(self.board.fields[13].return_score())
        self.win.scYOU.setText(self.board.fields[7].return_score())
        self.win.scOPP.setText(self.board.fields[0].return_score())


if __name__ == '__main__':
    #run_test(10)

    #board = Board()
    #board.ai_simulation_with_random_first_move(6)
    #print(visited)
    #print("---------------------------------")
    #for i in range(0, 6):
    #    board = Board()
    #    board.ai_simulation_with_random_first_move(3)
        #board.print_board()
    #run_test(100)
    #board.ai_simulation_with_random_first_move(4)
    #board.ai_simulation(4)
    mode = input()
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())