function solve(arr) {
  const res = [];
  arr.map((x, i, arr) => {
    if (!arr.slice(i + 1).some((q) => q >= x)) {
      res.push(x);
      console.log(res);
    }
  });
  return res;
}
