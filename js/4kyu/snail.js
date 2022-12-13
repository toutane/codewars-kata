function snail(array) {
  const output = [];
  // console.log(array)
  // array.splice(0,1)
  // console.log(array)
  const repeat = () => {
    if (array.length === 0) {
      return;
    }
    const len = array[0].length - 1;
    for (let i = 0; i <= len; i += 1) {
      output.push(...array[0].splice(0, 1));
    }
    // console.log(output)
    for (let i = 1; i <= len; i += 1) {
      output.push(...array[i].splice(len, 1));
    }
    for (let i = len - 1; i >= 0; i -= 1) {
      output.push(...array[len].splice(i, 1));
    }
    for (let i = len - 1; i > 0; i -= 1) {
      output.push(...array[i].splice(0, 1));
    }
    array.pop();
    array.shift();
    repeat(array);
  };
  repeat(array);
  return output;
}

console.log(snail([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
console.log(snail([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]));
// console.log(snail([[1, 2, 3, 1], [4, 5, 6, 4], [7, 8, 9, 7], [7, 8, 9, 7]]));
