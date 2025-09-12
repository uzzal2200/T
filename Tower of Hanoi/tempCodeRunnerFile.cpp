#include<bits/stdc++.h>
using namespace std;

// Function to solve the Tower of Hanoi problem
void towerOfHanoi(int N, char source, char destination, char aux) {
    // Base case: If only one disc, move it directly from source to destination
    if (N == 1) {
        cout << "Move disc 1 from " << source << " to " << destination << endl;
        return;
    }

    // Move N-1 discs from source to auxiliary peg
    towerOfHanoi(N - 1, source, aux, destination);

    // Move the remaining disc from source to destination
    cout << "Move disc " << N << " from " << source << " to " << destination << endl;

    // Move the N-1 discs from auxiliary peg to destination
    towerOfHanoi(N - 1, aux, destination, source);
}

int main() {
    int N;
    char source, destination, auxiliary;

    // Taking input for the number of discs
    cout << "Enter the number of discs: ";
    cin >> N;

    // Taking input for the names of the pegs (source, destination, auxiliary)
    cout << "Enter the name of the source peg (e.g., A): ";
    cin >> source;
    cout << "Enter the name of the destination peg (e.g., C): ";
    cin >> destination;
    cout << "Enter the name of the auxiliary peg (e.g., B): ";
    cin >> auxiliary;

    // Call the function to solve Tower of Hanoi
    towerOfHanoi(N, source, destination, auxiliary);

    // Calculate and display total number of moves
    // int totalMoves = (1 << N) - 1;  // Equivalent to 2^N - 1
    int totalMoves = pow(2, N) - 1;

    cout << "Total number of moves: " << totalMoves << endl;



    return 0;
}
