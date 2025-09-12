#include<bits/stdc++.h>
using namespace std;

int total_solution = 0;  // Global variable to count the total number of solutions

// Function to print the chessboard with queens placed
void print(int q_position[], int n)
{
    cout<<"\nsolution"<<++total_solution<<":\n";

    // Loop through each row of the chessboard
    for(int row=0;row<n;row++)
    {
        // Loop through each column of the chessboard
        for(int col=0;col<n;col++)
        {
            // Print 'Q' if there's a queen in this position, else print '.'
            if(q_position[row] == col)
            {
                cout<<"Q ";
            }
            else
            {
                cout<<". ";
            }
        }
        cout<<endl;
    }
}

// Function to check if it is safe to place a queen at the given position
bool is_safe(int q_position[], int c_row, int c_col)
{
    // Check each row that has a queen already placed
    for(int p_row = 0; p_row<c_row; p_row++)
    {
        // Check if the queen in the current row (c_row) and column (c_col) is under attack
        // It is unsafe if another queen is in the same column or diagonally aligned
        if(q_position[p_row] == c_col ||
        abs(q_position[p_row] - c_col) == abs(p_row - c_row) )
       {
        return false;  // Not safe
       }
    }
    return true;  // Safe to place the queen
}

// Function to place queens on the board row by row using backtracking
void place_q(int q_position[], int c_row, int n )
{
    // If we've placed queens in all rows, print the solution
    if(c_row == n)
    {
        print(q_position, n);
        return;
    }

    // Try placing a queen in each column of the current row
    for(int c_col = 0; c_col < n; c_col++)
    {
        // Check if it's safe to place the queen in this column of the current row
        if(is_safe(q_position, c_row, c_col))
        {
          q_position[c_row] = c_col;  // Place queen
          place_q(q_position, c_row+1, n);  // Move to the next row
        }
    }
}

int main()
{
    int n;
    cout<<"Enter the queen: ";  // Prompt user for the size of the board

    cin>>n;  // Read the number of queens and the size of the board
    int q_position[n];  // Array to store the column position of queens in each row
    place_q(q_position, 0, n);  // Start placing queens from row 0

    // If no solution is found, display this message
    if (total_solution == 0)
        cout << "No solution exists for N = " << n << endl;

    return 0;  // End of the program
}
