function elevatorDistance(array) {
  return array.reduce((a, x) => {
    const res = [x, Math.abs( a[0] - x) + a[1]]
    return res
  }, [array[0], 0])[1]
};

