import TODOItem from "./TODOItem";

const TODOList = ({drf_todos}) => {
  return (
    <table>
      <thead>
      <tr>
        <th>Text</th>
        <th>Author</th>
        <th>Project</th>
        <th>Created at</th>
        <th>Updated at</th>
      </tr>
      </thead>
      <tbody>
      {drf_todos.map(drf_todo =>
        <TODOItem drf_todo={drf_todo} key={drf_todo.todo_text}/>)
      }
      </tbody>
    </table>
  )
};

export default TODOList