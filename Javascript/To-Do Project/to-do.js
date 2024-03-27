const todo_array = [];

renderHtml();

function renderHtml(){
  let todo_Html = '';
  for(i = 0; i < todo_array.length; i++){
    
    let todoList = todo_array[i];
    todo_Html += `
      <div>${todoList.name}</div>
      <div> ${todoList.date}</div>
      <button onclick = "
          todo_array.splice(${i},1);
          renderHtml();"
          class = "delete-todo"
      >Delete</button>
    `;
  }
  console.log(todo_Html);
  document.querySelector('.js-todo-list')
    .innerHTML = todo_Html;
}

function addTodo(){

  const addElement = document.querySelector('.js-add-input');
  const todoname = addElement.value;

  const dateElement = document.querySelector('.js-date-input');
  const duedate = dateElement.value;

  todo_array.push({name:todoname,
    date : duedate});
  console.log(todo_array);

  addElement.value = ''; 
  renderHtml();
}