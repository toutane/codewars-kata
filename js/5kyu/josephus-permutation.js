function josephus(array, k) {
  const output = [];
  let arr = array;
  let bef = 0;
  for (let u = 1; u <= array.length; u += 1) {
    output.push(arr[((bef + k) - 1) % arr.length]);
    bef = ((bef + k) - 1) % arr.length;
    arr = arr.filter((e, i) => i !== bef);
  }
  return output;
}

console.log(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2));
