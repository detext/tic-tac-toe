using System;

namespace tictactoe
{
    class Program
    {
        static void Main(string[] args)
        {
            RunGame();
        }

        static void RunGame()
        {
            // edit the line below to disable numbered board
            // false == numbered board
            // true == clean board
            GameLogic game = new GameLogic(cleanBoard: false);
            string input;
            do
            {
                game.AlternatePlayer();
                Console.Clear();
                game.PrintGameBoard();

                do
                {
                    input = null;
                    Console.Write($"\nEnter a number between 0-8 ({game.CurrentPlayer}): ");
                    input = Console.ReadLine();
                } while (game.ProcessInput(input));
            } while (!game.GameFinished());

            Console.Clear();
            game.PrintWinnerBoard();
            Console.WriteLine();

            if (game.Win) { Console.WriteLine($"Player {game.CurrentPlayer} WON the game"); }
            else if (game.Draw) { Console.WriteLine("Game ended in a DRAW"); }

            Console.Write("\nPress Enter to Exit...");
            Console.ReadKey();
        }
    }
}
