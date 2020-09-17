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
            GameLogic game = new GameLogic(cleanBoard: true);
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

            // if (game.Draw) { Console.WriteLine("Game ended in a DRAW"); }
            // else if (game.Win) { Console.WriteLine($"Player {game.CurrentPlayer} WON the game"); }

            if (game.Win) { Console.WriteLine($"Player {game.CurrentPlayer} WON the game"); }
            else if (game.Draw) { Console.WriteLine("Game ended in a DRAW"); }

            Console.Write("\nPress Enter to Exit...");
            Console.ReadKey();
        }
    }
}
