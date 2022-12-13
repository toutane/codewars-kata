function solequa(n) {
  const x = (1 + n) / 2;
  const y = (n - 1) / 4;
  const result = [[Math.abs(x), y]];

  return result;
}

console.log(solequa(5));
