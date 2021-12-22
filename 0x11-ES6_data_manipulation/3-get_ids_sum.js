export default function getStudentIdsSum(students) {
  const reducer = (x, y) => x + y.id;
  return students.reduce(reducer, 0);
}
