from questions import question
from mdp import reward
from mdp import QuizProblem, valueIteration


def game():
    Q = question(N=10)
    pi = valueIteration(QuizProblem(11))
    print("Wellcome to our Video Games-Quiz".center(120, "-"))
    print('In this game you have to answer 10 questions in order from easy to hard'.center(120, "-"))
    print('For each right answer you will get a reward'.center(120, "-"))
    print('The reward depends on the level`s difficulty (of the question)'.center(120, "-"))
    print('in every level you can choose'.center(120, "-"))
    print('either to quit the game and take all the rewards you have earned so far'.center(120, "-"))
    print('or keep play to the next level and take the risk to lose all of the rewards have earned'.center(120, "-"))

    input('press any key to continue')
    for i in range(10):
        prompt = "question " + str(i + 1)
        print(prompt.center(120, "-"))
        q = Q.questionByLevel(i)
        print(q[0].center(120, "-"))
        print(q[2])
        answer = input()
        if answer == q[1]:
            print("You are correct!".center(120, "-"))
            print(q[3])
            print("Your reward is $", reward[i])
            if i < 9:
                while True:
                    print('Do you wish to continue ? Y/N (The MDP algorithm suggests to: ', pi[i + 1], ')')
                    nextMove = input()
                    if nextMove == 'Y':
                        break
                    if nextMove == 'N':
                        print("Your reward is $", sum(reward[0:i]))
                        print("Goodbye")
                        return
            else:
                print("Congratulation!".center(120, "-"))
                print("You have finished the game".center(120, "-"))
                prompt = "Your total prize is $" + str(sum(reward))
                print(prompt.center(120, "-"))
                return

        else:
            print("You are wrong!".center(120, "-"))
            print("The correct answer is ", q[1])
            print("You lost $", sum(reward[0:i + 1]))
            break


if __name__ == '__main__':
    game()