function humanReadable(num) {
  const hours = Math.floor(num / 3600);
  const minutes = Math.floor((num / 60) % 60);
  const seconds = num - (hours * 3600 + minutes * 60);
  return `${hours.toString().padStart(2, '0')}:${minutes
    .toString()
    .padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
}

console.log(humanReadable(60));
