using System;
using System.Linq;
using tictactoe;

namespace tictactoe
{
    class GameLogic
    {

        public GameLogic(bool cleanBoard = false)
        { this.cleanBoard = cleanBoard; }

        static private Player player = new Player();
        private int userInput = -1;
        private int[] winnerCombination;
        private char[] boardState = new char[9] { '0', '1', '2', '3', '4', '5', '6', '7', '8' };
        readonly private bool cleanBoard;
        readonly private int[][] winningCombinations = new int[8][]
        { new int[3] { 0, 1, 2 },
          new int[3] { 3, 4, 5 },
          new int[3] { 6, 7, 8 },
          new int[3] { 0, 3, 6 },
          new int[3] { 1, 4, 7 },
          new int[3] { 2, 5, 8 },
          new int[3] { 0, 4, 8 },
          new int[3] { 2, 4, 6 }
        };
        public char CurrentPlayer { get; private set; } = player.O;
        public bool Win { get; private set; }
        public bool Draw { get; private set; }

        public bool ProcessInput(string input)
        {
            if ((int.TryParse(input, out userInput)) && (userInput > -1) && (userInput < 9) && (boardState[userInput] != player.X) && (boardState[userInput] != player.O))
            {
                boardState[userInput] = CurrentPlayer;
                userInput = -1;
                return false;
            }
            Console.WriteLine("Invalid Input Or Value Already Filled");
            return true;
        }

        public bool GameFinished()
        {
            foreach (int[] x in winningCombinations)
            {
                (char, char, char) currentCombination = (boardState[x[0]], boardState[x[1]], boardState[x[2]]);
                (char, char, char) winningCombination = (CurrentPlayer, CurrentPlayer, CurrentPlayer);

                Win = currentCombination == winningCombination;
                if (Win) 
                { 
                	winnerCombination = x;
                	return true;
                }
            }

            winnerCombination = new int[3] { -1, -1, -1 };

            Draw = boardState.All(x => ((x == player.X) || (x == player.O))) && !Win;
            if (Draw)
            { return true; }
            return false;
        }

        public void AlternatePlayer()
        {
            if (CurrentPlayer == player.X) { CurrentPlayer = player.O; } else { CurrentPlayer = player.X; }
        }

        public void PrintGameBoard()
        { if (!cleanBoard) { PrintBoard(GetBoard(boardState)); } else { PrintCleanBoard(); } }

        public void PrintCleanBoard()
        {
            char[] cleanBoard = new char[boardState.Length];

            for (int i = 0; i < cleanBoard.Length; i++)
            {
                char val = (boardState[i] == player.X) || (boardState[i] == player.O) ? boardState[i] : ' ';
                cleanBoard[i] = val;
            }

            PrintBoard(GetBoard(cleanBoard));
        }

        public void PrintWinnerBoard()
        {
            if (Draw) { PrintGameBoard(); }
            else
            {
                char[] winnerBoard = new char[boardState.Length];

                for (int i = 0; i < winnerBoard.Length; i++) { winnerBoard[i] = ' '; }
                winnerBoard[winnerCombination[0]] = CurrentPlayer;
                winnerBoard[winnerCombination[1]] = CurrentPlayer;
                winnerBoard[winnerCombination[2]] = CurrentPlayer;

                PrintBoard(GetBoard(winnerBoard));
            }
        }

        private string[] GetBoard(char[] boardState)
        {
            string[] board = new string[9]
                {
                    "     |     |     ",
                    $"  {boardState[0]}  |  {boardState[1]}  |  {boardState[2]}  ",
                    "_____|_____|_____",
                    "     |     |     ",
                    $"  {boardState[3]}  |  {boardState[4]}  |  {boardState[5]}  ",
                    "_____|_____|_____",
                    "     |     |     ",
                    $"  {boardState[6]}  |  {boardState[7]}  |  {boardState[8]}  ",
                    "     |     |     ",
                };
            return board;
        }

        private void PrintBoard(string[] board)
        {
            foreach (string line in board) { Console.WriteLine(line); }
        }
    }
}
