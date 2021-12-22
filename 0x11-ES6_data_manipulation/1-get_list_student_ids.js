export default function getListStudentIds(arrayObj) {
  if (Array.isArray(arrayObj)) {
    return arrayObj.map((x) => x.id);
  }

  return [];
}
