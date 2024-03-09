let score = JSON.parse(localStorage.getItem('score'))
|| {
  Wins : 0,
  Loses : 0,
  Tie : 0
  };

  para_score();

// if (score === null){
//   score ={
//   Wins : 0,
//   Loses : 0,
//   Tie : 0
//   }
// };

function playGame(playerMove){
  const computerMove = pickComputermove();

  let result = '';
  if (playerMove === 'Scissors'){
    if (computerMove === 'Rock'){
      result = 'You Lose';
    } else if (computerMove === 'Paper'){
      result = 'You Win'
    } else if (computerMove === 'Scissors'){
      result = 'Tie'
    } 
  } else if (playerMove === 'Paper'){
      if (computerMove === 'Rock'){
        result = 'You Win';
      } else if (computerMove === 'Paper'){
        result = 'Tie'
      } else if (computerMove === 'Scissors'){
        result = 'You Lose'
      }
  } else if(playerMove === 'Rock'){
      if (computerMove === 'Rock'){
        result = 'Tie';
      } else if (computerMove === 'Paper'){
        result = 'You Lose'
      } else if (computerMove === 'Scissors'){
        result = 'You Win'
      }
  }
  
  if (result === 'You Win'){
    score.Wins += 1;
  } else if (result === 'You Lose'){
    score.Loses += 1;
  } else if (result === 'Tie'){
    score.Tie += 1;
  }

  localStorage.setItem('score', JSON.stringify(score));

  para_score();
  
  document.querySelector('.js-result')
  .innerHTML = result;

  document.querySelector('.js-moves')
  .innerHTML = `You 
  <img src="rps-image/${playerMove}.jpeg" class="move-icon">
  <img src="rps-image/${computerMove}.jpeg" class="move-icon">
  Computer`;
  

//         alert(`You picked ${playerMove}.Computer picked ${computerMove}.${result}.
// Wins : ${score.Wins} Loses : ${score.Loses} Tie : ${score.Tie}`);

}

function para_score(){
  document.querySelector('.js-score')
  .innerHTML = `Wins : ${score.Wins} Loses : ${score.Loses} Tie : ${score.Tie}`;
}


function pickComputermove(){
  const randomMove = Math.random();
  let computerMove = '';
  
  if (randomMove > 0 && randomMove < 1 /3){
    computerMove = 'Rock';
  } else if (randomMove > 1/3 && randomMove < 2 / 3){
    computerMove = 'Paper';
  } else {
    computerMove = 'Scissors';
  }
  return computerMove;
}