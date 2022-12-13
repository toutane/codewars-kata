function squaresSumsRow(n) {
  const array = [];
  for (let i = 1; i < n + 1; i += 1) {
    array.push(i);
  }
  const data = {};
  function checkSquares(num) {
    for (let i = 1; i < n + 1; i += 1) {
      if (Math.sqrt(num + i) % 1 === 0 && num !== i) {
        if (data[num] === undefined) {
          data[num] = [i];
        } else {
          data[num].push(i);
          if (data[num].length > 2) {
            data[num].shift();
          }
        }
      }
    }
    return num;
  }
  array.forEach((element) => checkSquares(element));
  let firstItem = 1;
  let hello = null;
  Object.keys(data).map((x) => (data[x].length === 1 ? (hello = x) : null));
  Object.keys(data).map((x) => (data[x].find((e) => e === parseInt(hello, 10)) !== undefined
    ? (firstItem = parseInt(x, 10))
    : null));
  // console.log(firstItem);
  const output = [data[firstItem][0], firstItem, data[firstItem][1]];
  // while (output.length !== n) {
  let u = 0;
  while (u !== 100) {
    for (let i = 1; i < n + 1; i += 1) {
      // console.log(output.find((e) => e === i));
      const item = [output[0], output[output.length - 1]];
      // console.log(item);
      if (item.find((e) => e === i) !== undefined) {
        let result = data[i];
        for (let v = 0; v < output.length; v += 1) {
          result = result.filter((x) => x !== output[v]);
          // console.log(data[i], output[v], result);
        }
        // console.log(result);
        if (result.length !== 0) {
          const index = output.findIndex((e) => e === i);
          if (index === 0) {
            // result.concat(output)
            output.unshift(result[0]);
          } else {
            output.push(result[0]);
          }
        }
      }
    }
    u += 1;
  }
  console.log(data);
  console.log(output.length);
  return output;
}

console.log(squaresSumsRow(15));
// console.log(squaresSumsRow(25));
