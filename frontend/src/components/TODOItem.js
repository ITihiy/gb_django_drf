const TODOItem = ({drf_todo}) => {
  return (
    <tr>
      <td>{drf_todo.todo_text}</td>
      <td>{drf_todo.author.username}</td>
      <td>{drf_todo.project.name}</td>
      <td>{drf_todo.created_at}</td>
      <td>{drf_todo.updated_at}</td>
      <td>{drf_todo.is_active}</td>
    </tr>
  )
};

export default TODOItem;