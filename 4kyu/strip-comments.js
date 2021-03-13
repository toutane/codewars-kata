function strip(str, markers) {
  let array = [];
  for (let i = 0; i < str.length; i += 1) {
    array.push(str[i]);
  }
  const fc = [];
  const fv = [];
  markers.map((m) => fc.push(array.findIndex((e) => e === m) - 1));
  let state = false;
  function test(i) {
    fv.push(i);
    state = true;
  }
  for (let i = 0; i < fc.length; i += 1) {
    // eslint-disable-next-line no-loop-func
    array.map((e, index) => (e === '\n' && state === false ? test(index) : null));
  }
  if (fv.length !== fc.length) {
    array = array.slice(0, fc[fc.length - 1]);
    fc.pop();
  }
  for (let i = 0; i < fc.length; i += 1) {
    array.splice((fc[i]), fv[i] - fc[i]);
  }
  console.log(array);
  return array.join('').trim();
}

console.log(strip('apples, plums % and bananas\npears\noranges !applesauce', ['%', '!']));
