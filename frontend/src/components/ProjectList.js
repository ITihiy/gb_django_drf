import ProjectItem from "./ProjectItem";

const ProjectList = ({drf_projects}) => {
  return (
    <table>
      <thead>
      <tr>
        <th>Name</th>
        <th>Repository</th>
      </tr>
      </thead>
      <tbody>
      {drf_projects.map(drf_project =>
        <ProjectItem drf_project={drf_project} key={drf_project.name}/>)
      }
      </tbody>
    </table>
  )
};

export default ProjectList