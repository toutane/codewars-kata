function duplicateEncode(word) {
  word = word.toLowerCase();
  const hist = {};
  for (let i = 0; i < word.length; i++) {
    if (hist[word[i]] == null) {
      hist[word[i]] = 1;
    }
    else {
      hist[word[i]] = hist[word[i]] + 1;
    }
  }
  let res = "";
  for (let i = 0; i < word.length; i++) {
    if (hist[word[i]] <= 1) {
      res = res + "(";
    }
    else {
      res = res + ")";
    }
  }
  return res;
}
