const DRFUserItem = ({drf_user}) => {
  return (
    <tr>
      <td>{drf_user.username}</td>
      <td>{drf_user.first_name}</td>
      <td>{drf_user.last_name}</td>
      <td>{drf_user.email}</td>
    </tr>
  )
};

export default DRFUserItem;
