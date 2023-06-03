# Tic-Tac-Toe Game
A simple tic-tac-toe game written in Python using the Flask framework and VueJS on the frontend.

## Game Rules
The player plays against the computer. The player starts the game. The player selects a position on the board, then the computer selects a position on the board.

### Starting a Session
To start the game, create a new player by providing their name. After creating the player, the game can be started. To start the game, enter the name of the created player and click the "Start session" button.

### Gameplay
At the start, the player receives 10 credits, and each new game costs 3 credits to start. In case of winning, the player receives 4 credits. The game ends when the player doesn't have enough credits to start a new game.

### Adding Credits
When the number of credits is zero, the player can click the "Add credits" button to add 10 credits to the current session.

## Players Statistics
Clicking the "Players statistics" button will display a panel with players statistics.

## Technologies
- Python
- Flask
- TypeScript
- VueJS 

## Socket.io
The Socket.io library enables real-time communication between the client and the server. In the application, during the start of a game session, it is responsible for updating the game time.

## OpenAPI
The OpenAPI specification is used to describe the REST API. The specification is available at http://localhost:5002/openapi/

## Installation
Commands have been added to the repository to build Docker images with the project and run the containers. Simply execute the following commands:

```bash
make docker-build # build Docker images
```
Before running, update the variables in the .env file, especially the ports on which the containers will be running.

```bash
FRONTEND_PORT=3000 # port on which the frontend will run
BACKEND_PORT=5002 # port on which the backend will run
```
After setting these variables, you can run the containers:

```bash
make docker-run # run the containers
```
Once the containers are running, the application will be available at http://localhost:3000.

## Running Tests
To run the tests, execute the following command:

```bash
make run-backend-tests # run the tests
```