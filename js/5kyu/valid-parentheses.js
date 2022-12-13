// function validParentheses(parens) {
//   const array = parens.split('');
//   const output = [];
//   array.map((x, i) =>
//     x === array[i + 1] ? output.push(array[i], array[i + 1]) : null
//   );
//   if (output.sort().length === 0) {
//     return true;
//   }
//   console.log(array);
//   console.log(output.sort());
//   console.log(output.sort().reverse());
//   let u = 0;
//   output.sort().map((x) => (x === '(' ? (u += 1) : null));
//   // console.log(u);
//   if (u > output.length / 2) {
//     return output.sort().reverse()[u - 1] === ')';
//   }
//   return !output.sort().reverse()[u - 1] === ')';
// }

// // console.log(validParentheses('()'));
// // console.log(validParentheses('(())()()()()(('));

function validParentheses(parens) {
  let opened = 0;
  for (let i = 0; i < parens.length; i += 1) {
    if (parens.charAt(i) === '(') {
      opened += 1;
    } else {
      opened -= 1;
    }
    if (opened < 0) {
      return false;
    }
  }
  if (opened === 0) {
    return true;
  }
  return false;
}

console.log(validParentheses('(())((()())())'));
