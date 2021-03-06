import BN from "bignumber.js"

function solve(ar) {
  let res = [];
  function calcul(a, b, c, d) {
    return [a * c + b * d, a * d - b * c];
  }
  let i = 0;
  while (ar.length !== i) {
    if (i === 0) {
      res = calcul(BigInt(ar[0]), BigInt(ar[1]), BigInt(ar[2]), BigInt(ar[3]));
      i += 4;
    } else {
      res = calcul(res[0], res[1], BigInt(ar[i]), BigInt(ar[i + 1]));
      i += 2;
    }
  }
  return res.map(num => BN(num).abs());
}

console.log(solve([2, 1, 3, 4]));
console.log(solve([1, 3, 1, 2, 1, 5, 1, 9]));
console.log(solve([3, 9, 8, 4, 6, 8, 7, 8, 4, 8, 5, 6, 6, 4, 4, 5]));
