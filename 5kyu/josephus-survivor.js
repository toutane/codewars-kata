function josephusSurvivor(n, k) {
  const output = [];
  let arr = [];
  for (let i = 1; i <= n; i += 1) {
    arr.push(i);
  }
  let bef = 0;
  for (let u = 1; u <= n; u += 1) {
    output.push(arr[((bef + k) - 1) % arr.length]);
    bef = ((bef + k) - 1) % arr.length;
    arr = arr.filter((e, i) => i !== bef);
  }
  return output[output.length - 1];
}

console.log(josephusSurvivor(11, 19));
