#include <iostream>
using namespace std;

// Number of cities and distance matrix
int n=4, tsp_g[4][4] = {
    {12,30,33,10},  // Distances from city 1
    {56,22,9,15},   // Distances from city 2
    {29,13,8,5},    // Distances from city 3
    {33,28,16,10}   // Distances from city 4
};

int visited[4], cost=0; // visited array to track cities, cost stores total distance

// Recursive function for TSP using nearest neighbor heuristic
void tsp(int c){
    visited[c] = 1;            // Mark current city as visited
    cout << c+1 << " ";         // Print current city in path (1-indexed)

    int minc = 999, next = -1;  // Initialize min cost and next city

    // Find the nearest unvisited city from current city
    for(int k=0; k<n; k++){
        if(!visited[k] && tsp_g[c][k]<minc){
            minc = tsp_g[c][k]; // Update minimum distance
            next = k;           // Update next city to visit
        }
    }

    if(next == -1){  // Base case: all cities visited
        cout << "1";             // Return to start city
        cost += tsp_g[c][0];     // Add distance from last city to start city
        return;
    }

    cost += minc;       // Add distance to nearest city
    tsp(next);           // Recursive call to next city
}

int main(){
    cout << "Path: ";
    tsp(0);  // Start TSP from city 1 (index 0)

    cout << "\nMinimum Cost: " << cost;  // Print total cost
}
