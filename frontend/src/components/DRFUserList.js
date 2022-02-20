import DRFUserItem from './DRFUserItem'

const DRFUserList = ({drf_users}) => {
  return (
    <table>
      <thead>
      <tr>
        <th>Username</th>
        <th>First name</th>
        <th>Last name</th>
        <th>Email</th>
      </tr>
      </thead>
      <tbody>
      {drf_users.map(drf_user =>
        <DRFUserItem drf_user={drf_user} key={drf_user.email}/>)
      }
      </tbody>
    </table>
  )
};

export default DRFUserList