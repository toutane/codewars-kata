function removeNb(n) {
  const result = [];
  const sum = (n * (n + 1)) / 2;
  for (let i = 1; i < n; i += 1) {
    const a = (sum - i) / (i + 1);
    if (a * i === (sum - (a + i)) && (a % 1 === 0) && a < n) {
      result.push([i, a]);
    }
  }
  return result;
}

console.log(removeNb(26));
