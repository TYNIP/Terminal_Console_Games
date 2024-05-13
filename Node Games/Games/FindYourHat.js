/* 
GAME: FIND YOU HAT 

Move your character "*" where your hat is "^" to win, but be carefull, 
if you get out of the map or fall in a hole "O" you lose.
In order to move along the field, move by typing and entering up/down/left/right.
Type Exit if you want to leave the game.

*/

/*GAME CHARACTERS*/
const hat = '^';
const hole = 'O';
const fieldCharacter = '░';
const pathCharacter = '*';

/* SETUP */
const prompt = require('prompt-sync')();

// Game structure
class Field{
    constructor(field){
        this._field = field;
        this._currentPosition = {x: 0, y:0};
        this._field[this._currentPosition.x][this._currentPosition.y] = pathCharacter;
    };

    //Getters
    get field(){
        return this._field;
    };
    get currentPosition(){
        return this._currentPosition;
    };

    //Generate Random Play Field
    static generateField(height, width, percentHoles) {
        const field = new Array(height).fill(0).map(() =>
        new Array(width).fill(0).map(() => {
            const randomNum = Math.random();
            if (randomNum < percentHoles) {
                return hole;
            } else {
                return fieldCharacter;
            };
        })
        );
    
        // Place the hat randomly
        const hatX = Math.floor(Math.random() * height);
        const hatY = Math.floor(Math.random() * width);
        field[hatX][hatY] = hat;
    
        return field;
      }

    //Controls
    move(direction){
        const {x, y} = this._currentPosition;
        const originalState = this._field[x][y];
        this._field[x][y] = originalState;
        this._field[x][y] = fieldCharacter;

        switch(direction){
            case 'up':
                this._currentPosition.x -= 1;
                break;
            case 'down':
                this._currentPosition.x += 1;
                break;
            case 'left':
                this._currentPosition.y -= 1;
                break;
            case 'right':
                this._currentPosition.y += 1;
                break;
            case 'exit':
                console.log('Exit selected. See you soon!');
                process.exit(0);
                break;
            default:
                console.log('Invalid move. Please enter "up", "down", "left", or "right".');
                return;
        };
        //Check up 
            // If player is out of the map
            const { x: newX, y: newY } = this._currentPosition;
            if (newX < 0 || newX >= this._field.length || newY < 0 || newY >= this._field[0].length) {
                console.log('Game over! You moved outside the field. You lose!');
                process.exit(0);
            }
            // If player is in a hole of the hat
            const newPosition = this._field[newX][newY];
            if (newPosition === hole){
                console.log('Oops! You fell into a hole. You lose!');
                process.exit(0);
            } else if (newPosition === hat){
                console.log('Congratulations! You found your hat. You win!');
                process.exit(0); 
            }
        // Set New Position to pathCharacter
        this._field[newX][newY] = pathCharacter;
    };

    //Methods if player wins/losses/get out of the map
    checkWin(){
        const {x,y} = this._currentPosition;
        return this._field[x][y] === hat;
    };
    checkLoss(){
        const {x,y} = this._currentPosition;
        return this._field[x][y] === hole;
    };
    checkOutOfMap(){
        const {x,y} = this._currentPosition;
        return x < 0 || x >= this._field.length || y < 0 || y >= this._field[0].length;
    };

    //See The Game Field
    print(){
        for(let row of this._field){
            console.log(row.join(' '));
        };
    };
}

//Game settings
function playGame() {
    let gameHeight;
    let gameWidth;
    let gameLevel;
    function verifyCorrectSizeMap(){
        while (typeof gameHeight !== 'number'){
            const inputHeight = prompt('Enter The Height Of The Game Field (Recomended: 3-10): ');
            const numInput = Number(inputHeight);
            if (!isNaN(numInput)){
                gameHeight = numInput;
            } else {
                console.log('Invalid input. Select a number.');
            };
        };
        while (typeof gameWidth !== 'number'){
            const inputWidth = prompt('Enter The Width Of The Game Field (Recomended: 3-10): ');
            const numInput = Number(inputWidth);
            if (!isNaN(numInput)){
                gameWidth = numInput;
            } else {
                console.log('Invalid input. Select a number.');
            };
        };
    };

    function gameDifficulty() {
        while(gameLevel === undefined){
        const inputLevel = prompt('Enter The Level Of The Game (1-3): ');
        switch(Number(inputLevel)){
            case 1:
                gameLevel = 0.2;
                console.log('')
                console.log('> The Cool Level')
                break;
            case 2:
                gameLevel = 0.4;
                console.log('')
                console.log('> The Ahhh Level')
                break;
            case 3:
                gameLevel = 0.6;
                console.log('')
                console.log('> The Impossible Level')
                break;
            default:
                console.log('Invalid level of game.');   
        }};
    };
    console.log('~ FIND YOU HAT THE GAME  ~')
    console.log('GAME SETTINGS: ')
    console.log('');
    verifyCorrectSizeMap()
    gameDifficulty();
    const height = Number(gameHeight); 
    const width = Number(gameWidth);
    const percentHoles = Number(gameLevel); 
    const generatedField = Field.generateField(height, width, percentHoles);
    const myField = new Field(generatedField);
    console.log('');
    console.log('Instructions:');
    console.log('Move your character "*" where your hat is "^" to win, but be carefull, if you get out of the map or fall in a hole "O" you lose!');
    console.log('Move by typing and entering up/down/left/right.');
    console.log('Type Exit if you want to leave the game.');
    console.log('Good Luck!');
    console.log('');
    //Game Run
    while (true) {
      console.clear; 
      myField.print();
      const direction = prompt('Enter your move (up/down/left/right/exit): ');
      myField.move(direction);
  
      if (myField.checkWin()) {
        console.log('Congratulations! You found your hat. You win!');
        break;
      } else if (myField.checkLoss()) {
        console.log('Oops! You fell into a hole. You lose!');
        break;
      } else if (myField.checkOutOfMap()) {
        console.log('Game over! You moved outside the field. You lose!');
        break;
      }
    }
  }
  
  playGame();