import random
import copy
import math
import time
visited = 0
graczA = 0
graczB = 0
class Field:

    def __init__(self, number):
        self.next = None
        self.stones = 4
        self.number = number
        self.opposite = None

    def move_stones(self, turn):
        stm = self.stones
        self.stones = 0
        if stm > 0:
            return Field.next_stone(self.next, stm, turn)

    @staticmethod
    def next_stone(field, temps, turn):
        if turn and field.number == -1:
            return Field.next_stone(field.next, temps, turn)
        elif not turn and field.number == 0:
            return Field.next_stone(field.next, temps, turn)
        field.stones += 1
        if temps == 1:
            return field.number
        return Field.next_stone(field.next, temps-1, turn)

    def return_score(self):
        if self.stones == 0:
            return ""
        else:
            return str(self.stones)


class Board:

    def __init__(self):
        #self.turn = random.choice([True, False])
        self.turn = True
        self.fields = [Field(-1), Field(1), Field(2), Field(3), Field(4), Field(5), Field(6), Field(0), Field(7), Field(8), Field(9), Field(10), Field(11), Field(12)]
        self.fields[0].stones = 0
        self.fields[7].stones = 0
        self.connect_fields()
        self.set_opposites()

    def get_fields(self):
        return self.fields

    def connect_fields(self):
        for i in range(0, 13):
            self.fields[i].next = self.fields[i+1]
        self.fields[13].next = self.fields[0]

    def set_opposites(self):
        for i in range(1, 7):
            self.fields[i].opposite = self.fields[14-i]
            self.fields[14-i].opposite = self.fields[i]

    def decide_turn_after_move(self, number):
        if self.turn:
            if number != 0:
                self.turn = False
        else:
            if number != -1:
                self.turn = True

    def check_if_end(self):
        low = 1
        up = 7
        if not self.turn:
            low = 8
            up = 14
        for i in range(low, up):
            if self.fields[i].stones != 0:
                return False
        self.when_end()
        return True

    @staticmethod
    def h1_right_most(board, starts):
        if starts:
            return board.fields[6].stones
        else:
            return board.fields[13].stones

    def when_end(self):
        low = 1
        up = 7
        ind = 7
        if self.turn:
            low = 8
            up = 14
            ind = 0
        for i in range(low, up):
            self.fields[ind].stones += self.fields[i].stones
            self.fields[i].stones = 0
        #print("END")

    @staticmethod
    def eval_function(board):
        return board.fields[7].stones - board.fields[0].stones

    @staticmethod
    def eval_heur_function(board, no_moves, starts):
        num = 1
        if not starts:
            num = -1
        right = Board.h1_right_most(board, starts)
        return (board.fields[7].stones - board.fields[0].stones) + 0.37 * no_moves * num + 0.198 * right * num

    def next_move_with_minimax(self, depth, is_alpha_beta):
        #moves = Board.minimax(self, depth, self.turn)[1]
        if is_alpha_beta:
            #result = Board.minimax_alpha_beta(self, depth, -math.inf, math.inf, self.turn)
            result = Board.minimax_alpha_beta_heuristics(self, depth, -math.inf, math.inf, self.turn, self.turn, 0)
        else:
            result = Board.minimax(self, depth, self.turn)
        moves = result[1]
        global graczA
        global graczB
        if self.turn:
            graczA += len(moves)
        else:
            graczB += len(moves)
        self.make_moves_from_list(moves)
        self.turn = not self.turn

    @staticmethod
    def minimax(node, depth, is_maximizing):
        global visited
        visited += 1
        moves = []
        if depth == 0 or node.check_if_end():
            return Board.eval_function(node), moves
        if is_maximizing:
            best_val = -math.inf
            for i in node.possible_moves():
                child = copy.deepcopy(node)
                child.make_moves_from_list(i)
                result = Board.minimax(child, depth-1, False)[0]
                del child
                if result > best_val:
                    best_val = result
                    moves = i
            return best_val, moves
        else:
            best_val = math.inf
            for i in node.possible_moves():
                child = copy.deepcopy(node)
                child.make_moves_from_list(i)
                result = Board.minimax(child, depth - 1, True)[0]
                del child
                if result < best_val:
                    best_val = result
                    moves = i
            return best_val, moves

    @staticmethod
    def minimax_alpha_beta(node, depth, alpha, beta, is_maximizing):
        global visited
        visited += 1
        moves = []
        if depth == 0 or node.check_if_end():
            return Board.eval_function(node), moves
        if is_maximizing:
            best_val = -math.inf
            for i in node.possible_moves():
                child = copy.deepcopy(node)
                child.make_moves_from_list(i)
                result = Board.minimax_alpha_beta(child, depth - 1, alpha, beta, False)[0]
                del child
                if result > best_val:
                    best_val = result
                    moves = i

                alpha = max(alpha, result)
                if beta <= alpha:
                    break
            return best_val, moves
        else:
            best_val = math.inf
            for i in node.possible_moves():
                child = copy.deepcopy(node)
                child.make_moves_from_list(i)
                result = Board.minimax_alpha_beta(child, depth - 1, alpha, beta, True)[0]
                del child
                if result < best_val:
                    best_val = result
                    moves = i

                beta = min(beta, result)
                if beta <= alpha:
                    break
            return best_val, moves

    @staticmethod
    def minimax_alpha_beta_heuristics(node, depth, alpha, beta, is_maximizing, starts, no_moves):
        global visited
        visited += 1
        moves = []
        if depth == 0 or node.check_if_end():
            return Board.eval_heur_function(node, no_moves, starts), moves
        if is_maximizing:
            best_val = -math.inf
            for i in node.possible_moves():
                child = copy.deepcopy(node)
                child.make_moves_from_list(i)
                if starts == is_maximizing:
                    no_moves += len(i)
                result = Board.minimax_alpha_beta_heuristics(child, depth - 1, alpha, beta, False, starts, no_moves)[0]
                del child
                if result > best_val:
                    best_val = result
                    moves = i

                alpha = max(alpha, result)
                if beta <= alpha:
                    break
            return best_val, moves
        else:
            best_val = math.inf
            for i in node.possible_moves():
                child = copy.deepcopy(node)
                child.make_moves_from_list(i)
                if starts == is_maximizing:
                    no_moves += len(i)
                result = Board.minimax_alpha_beta_heuristics(child, depth - 1, alpha, beta, True,  starts, no_moves)[0]
                del child
                if result < best_val:
                    best_val = result
                    moves = i

                beta = min(beta, result)
                if beta <= alpha:
                    break
            return best_val, moves

    def make_moves_from_list(self, moves):
        for i in moves:
            self.make_move(i)

    def cpu_move(self):
        r = random.randint(8, 13)
        while self.fields[r].stones == 0:
            r = random.randint(8, 13)
        return self.fields[r].move_stones(self.turn)

    def check_if_last_beats(self, number):
        if (self.turn and 1 <= number <= 6) or (not self.turn and 7 <= number <= 12):

            # needed due to shift of fields (water well between them)
            if number > 6:
                number += 1

            if self.fields[number].opposite is not None and self.fields[number].stones == 1:
                opp_stones = self.fields[number].opposite.stones
                if opp_stones > 0:
                    self.fields[number].stones = 0
                    self.fields[number].opposite.stones = 0
                    if self.turn:
                        self.fields[7].stones += opp_stones+1
                    else:
                        self.fields[0].stones += opp_stones+1
                    #print("BEAT!")

    def next_move(self):
        low = 1
        up = 6
        if not self.turn:
            low = 8
            up = 13
        r = random.randint(low, up)
        while self.fields[r].stones == 0:
            r = random.randint(low, up)
        return self.fields[r].move_stones()

    def make_move(self, index):
        last = self.fields[index].move_stones(self.turn)
        self.check_if_last_beats(last)
        end = self.check_if_end()
        return last, end

    def possible_moves(self):
        moves = [[x] for x in self.possible_choices()]
        done = []
        Board.append_combo_moves(self, moves, done)
        return done

    def possible_choices(self):
        low = 1
        up = 7
        if not self.turn:
            low = 8
            up = 14
        moves = list()
        for i in range(low, up):
            if self.fields[i].stones > 0:
                moves.append(i)
        return moves

    def is_stopping_in_own_well(self, index):
        if self.turn:
            if index == 0:
                return True
        else:
            if index == -1:
                return True
        return False

    @staticmethod
    def append_combo_moves(board, moves_list, done_list):
        for move in moves_list:
            last_element = move[-1]
            newboard = copy.deepcopy(board)
            last, end = newboard.make_move(last_element)
            if not end and newboard.is_stopping_in_own_well(last):
                pos_choices = newboard.possible_choices()
                next_choices = []
                for i in pos_choices:
                    next_choices.append(move+[i])
                Board.append_combo_moves(newboard, next_choices, done_list)
                del newboard
            else:
                del newboard
                done_list.append(move)

    def print_board(self):
        print("===========================================")
        print("    ",self.fields[6].stones,self.fields[5].stones, self.fields[4].stones,self.fields[3].stones,self.fields[2].stones,self.fields[1].stones)
        print(self.fields[7].stones,"                      ",self.fields[0].stones)
        print("    ",self.fields[8].stones,self.fields[9].stones, self.fields[10].stones,self.fields[11].stones,self.fields[12].stones,self.fields[13].stones)
        print("===========================================")

    def ai_simulation(self, depth, mode):
        end = False
        while not end:
            Board.next_move_with_minimax(self, depth, True)
            if mode == 0:
                self.print_board()
            end = self.check_if_end()
        print("THE END")
        self.print_board()
        print("AI 1: ", self.fields[7].stones)
        print("AI 2: ", self.fields[0].stones)

    def ai_simulation_with_random_first_move(self, depth):
        global graczA
        global graczB
        graczA = 0
        graczB = 0
        end = False
        t = 0
        counter = 0
        total = 0
        mademoves = 0
        while not end:
            if t < 2:
                all_moves = self.possible_moves()
                move_to_make = all_moves[random.randint(0, len(all_moves)-1)]
                self.make_moves_from_list(move_to_make)
                self.turn = not self.turn
            else:
                global visited
                start = int(round(time.time() * 1000))
                if not self.turn:
                    Board.next_move_with_minimax(self,1 ,False)
                else:
                    Board.next_move_with_minimax(self, depth, True)
                stop = int(round(time.time() * 1000))
                result = stop - start
                total += result
                counter += 1
                #print("visited: ", visited / counter)
            mademoves += 1
            end = self.check_if_end()
            t += 1

        #if self.fields[0].stones < self.fields[7].stones:
        print(self.fields[7].stones - self.fields[0].stones)
        #else:
            #print(self.fields[0].stones - self.fields[7].stones)
        #print("THE END")
        #self.print_board()
        #print(str(total/counter).replace('.',','))
        #print("AI 1: ", self.fields[7].stones)
        #print("AI 2: ", self.fields[0].stones)


    def ai_simulation2(self):
        end = False
        while not end:
            print(self.possible_moves())
            print(Board.minimax(self, 5, self.turn))
            last = self.next_move()
            self.check_if_last_beats(last)
            self.decide_turn_after_move(last)
            end = self.check_if_end()
        print("THE END")
        print("AI 1: ", self.fields[7].stones)
        print("AI 2: ", self.fields[0].stones)
