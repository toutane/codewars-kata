function arrayEquals(a, b) {
  return Array.isArray(a)
    && Array.isArray(b)
    && a.length === b.length
    && a.every((val, index) => val === b[index]);
}
function gangs(arr, k) {
  let output = [];
  const array = [];
  for (let i = 1; i <= k; i += 1) {
    array.push(i);
  }
  const reducer = (acc, n) => {
    const res = arr.filter((e) => n % e === 0 || n % e === n / e);
    output = output.filter((e) => !arrayEquals(e, res));
    output.push(res);
  };
  array.reduce(reducer, output);
  return output.length;
}

console.log(gangs([2, 3, 6, 5], 15));
