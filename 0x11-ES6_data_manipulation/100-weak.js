export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  let times = 1;
  if (weakMap.has(endpoint)) {
    times = weakMap.get(endpoint);

    times += 1;

    weakMap.set(endpoint, times);
  } else {
    weakMap.set(endpoint, times);
  }

  if (times >= 5) {
    throw Error('Endpoint load is high');
  }
}
