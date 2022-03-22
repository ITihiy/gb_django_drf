const ProjectItem = ({drf_project}) => {
  return (
    <tr>
      <td>{drf_project.name}</td>
      <td>{drf_project.repo}</td>
    </tr>
  )
};

export default ProjectItem;